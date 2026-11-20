#!/usr/bin/env python3

"""Check that role directories match the role entries in sandbox.yml.

Uses only the Python standard library, so it runs without installing anything.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

REPOSITORY_DIR = Path(__file__).resolve().parent.parent
START_MARKER = "# Apps Start"
END_MARKER = "# Apps End"
ROLE_ENTRY = re.compile(r"""^\s*-\s*(?:\{\s*)?role:\s*["']?([^\s,}"']+)""")
CONFIG_KEY = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*(?:#.*)?$")
CONFIG_ITEM = re.compile(r"""^\s*-\s+(["']?)([\w.-]+)\1\s*(?:#.*)?$""")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check that role directories match the entries in sandbox.yml."
    )
    parser.add_argument("--playbook", type=Path, default=REPOSITORY_DIR / "sandbox.yml")
    parser.add_argument("--roles-dir", type=Path, default=REPOSITORY_DIR / "roles")
    parser.add_argument(
        "--config",
        type=Path,
        default=REPOSITORY_DIR / ".github" / "ci-role-matrix.yml",
    )
    return parser.parse_args()


def display(path: Path) -> str:
    """Return the path relative to the repository when it is inside it."""
    try:
        return str(path.resolve().relative_to(REPOSITORY_DIR))
    except ValueError:
        return str(path)


def load_ignored_roles(config_path: Path) -> set[str]:
    """Return the names listed under the top-level ignored_roles key.

    The standard library has no YAML parser, so this reads only the form the
    list is written in: one "- name" entry per line. Anything else under the
    key is rejected instead of being guessed at.
    """
    ignored_roles: set[str] = set()
    in_ignored_roles = False
    lines = config_path.read_text(encoding="utf-8").splitlines()

    for number, line in enumerate(lines, start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        key = CONFIG_KEY.match(line)
        if key:
            in_ignored_roles = key.group(1) == "ignored_roles"
            supported = not in_ignored_roles or key.group(2) in ("", "[]")
        elif in_ignored_roles:
            item = CONFIG_ITEM.match(line)
            supported = item is not None
            if item:
                ignored_roles.add(item.group(2))
        else:
            supported = True

        if not supported:
            sys.exit(
                f"{display(config_path)}:{number}: unsupported ignored_roles "
                'syntax. Use one "- role_name" entry per line.'
            )

    return ignored_roles


def load_playbook_roles(playbook_path: Path) -> tuple[list[str], list[str]]:
    """Return the roles listed inside and outside the Apps markers."""
    matrix_roles: list[str] = []
    other_roles: list[str] = []
    markers: list[str] = []

    for line in playbook_path.read_text(encoding="utf-8").splitlines():
        if START_MARKER in line:
            markers.append(START_MARKER)
            continue
        if END_MARKER in line:
            markers.append(END_MARKER)
            continue
        if line.lstrip().startswith("#"):
            continue

        match = ROLE_ENTRY.match(line)
        if match:
            in_role_matrix = markers == [START_MARKER]
            (matrix_roles if in_role_matrix else other_roles).append(match.group(1))

    if markers != [START_MARKER, END_MARKER]:
        sys.exit(
            f"{display(playbook_path)}: expected one '{START_MARKER}' line "
            f"followed by one '{END_MARKER}' line."
        )

    return matrix_roles, other_roles


def main() -> int:
    args = parse_args()
    matrix_roles, other_roles = load_playbook_roles(args.playbook)
    ignored_roles = load_ignored_roles(args.config)
    role_dirs = {
        path.name
        for path in args.roles_dir.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    }
    matrix = set(matrix_roles)
    registrations = Counter(matrix_roles + other_roles)

    playbook = display(args.playbook)
    config = display(args.config)
    roles_dir = display(args.roles_dir)
    block = f"'{START_MARKER}' and '{END_MARKER}' in {playbook}"

    problems: list[tuple[str, set[str]]] = [
        (
            f"Listed between {block}, but {roles_dir}/ has no such directory",
            matrix - role_dirs,
        ),
        (
            (
                f"Directory in {roles_dir}/ without an entry between {block}. "
                f"Add the entry, or add the role to ignored_roles in {config}"
            ),
            role_dirs - matrix - ignored_roles,
        ),
        (
            (
                f"In ignored_roles in {config}, but {roles_dir}/ has no such "
                "directory. Remove the entry"
            ),
            ignored_roles - role_dirs,
        ),
        (
            (
                f"In ignored_roles in {config}, but also listed between {block}. "
                "Remove one of the two"
            ),
            ignored_roles & matrix,
        ),
        (
            f"Listed more than once in {playbook}",
            {role for role, count in registrations.items() if count > 1},
        ),
    ]

    failed = False
    for message, roles in problems:
        if not roles:
            continue
        failed = True
        print(f"{message}:", file=sys.stderr)
        for role in sorted(roles):
            print(f"  - {role}", file=sys.stderr)

    if failed:
        return 1

    print(
        f"{len(role_dirs)} role directories checked: {len(matrix)} listed between "
        f"the markers, {len(ignored_roles)} ignored."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
