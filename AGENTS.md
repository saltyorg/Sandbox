# Sandbox Role Authoring Guidance

These repository-wide instructions apply to contributors and coding agents
working in this checkout.

## Before adding or changing a role

- Before creating a role, read and follow the contribution criteria in
  `README.md` and the new-role requirements in
  `.github/PULL_REQUEST_TEMPLATE.md`.
- Derive patterns from current, actively deployed roles. Deprecated, migration,
  alias, and `No CI` roles are exceptions and must not be used as templates for
  new roles.
- Before adding or renaming a role or tag, search both Sandbox and Saltbox for
  role and tag collisions. Do not introduce a Sandbox role that unintentionally
  shadows a Saltbox role through `roles_path` precedence.

## Role structure and registration

- Use `snake_case` for role directories, Ansible role names, and variable
  prefixes. Declare the user-facing install tag explicitly in `sandbox.yml`;
  every literal Ansible tag uses lowercase kebab-case. Role names and install
  tags do not need to be identical.
- Start Ansible source YAML under `defaults/`, `tasks/`, `handlers/`, and
  `vars/` with the repository's standard title, `Author(s): salty`, repository
  URL, GPL, and YAML-document header. Static YAML payloads under `files/` and
  templates are outside this source-header rule.
- New active application roles contain `defaults/main.yml` and
  `tasks/main.yml`. Add templates, files, or task subtasks only when the role
  uses them.
- Add new main and independently runnable roles under `Apps Start` in
  `sandbox.yml` with their install tags by default. Use `No CI` only when a
  role cannot participate in the install matrix or is not runnable by itself;
  non-runnable companion roles use `never`.
- When a role supports multiple instances, declare `<role>_instances`, keep the
  instance loop in `tasks/main.yml`, and put per-instance work in
  `tasks/main2.yml`. Set `<role>_name` from the loop item and use `instance` as
  the loop variable for new roles.

## General conventions

- Follow established role patterns; avoid custom/unusual implementations.
- Use the standard variable naming scheme: `<role>_name`, `<role>_role_*` with `lookup('role_var', ...)`.
- Every `lookup('role_var', ...)` in defaults must specify an explicit `role=` target; cross-role targets remain valid.
- When an empty string, list, or mapping should select a supplied fallback, use
  `default_if_empty=true` with a non-`None` `default`; do not repeat manual
  non-empty checks around `role_var`.
- Prefer simple, predictable defaults; leave optional values empty rather than inventing new behavior.
- Add plain-language comments for non-obvious user-facing settings and their
  constrained values. Describe the setting's purpose instead of restating an
  upstream environment-variable name.
- Keep configurable API endpoints, release-metadata endpoints, and reusable
  download bases in role defaults and resolve them through `role_var`. A fixed
  one-off upstream asset may remain in a task when no override is intended.
- When CI needs credentials that satisfy role validation, generate a compliant role-local variable with a `set_fact` task guarded by `continuous_integration` instead of changing workflows or global user credentials.
- Use generator options that guarantee required character classes instead of adding hardcoded character prefixes.
- Keep one-time database bridge releases in an explicit migration role and leave the regular role on the current release.
- Detect completed database migrations from database integrity and preserved records, not from marker files or file existence alone.
- Keep edits ASCII-only and minimal unless the repo already uses Unicode in the same file.
- Use plain action and domain wording in variables and task names.

## Defaults file patterns

- When present, order top-level sections as Basics → Settings → backend-specific sections → Paths → Web → DNS → Traefik → Ports → Docker → Dependencies. Keep the literal `Postgres` and `Redis` sections between Settings and Paths, and keep Ports immediately before Docker.
- Paths:
  - `<role>_role_paths_folder` defaults to `<role>_name`.
  - `<role>_role_paths_location` uses `{{ server_appdata_path }}/{{ <role>_role_paths_folder }}`.
  - `<role>_role_paths_folders_list` includes the appdata root and any subpaths the app needs.
  - Use `<role>_role_paths_recursive: true` when a role needs its folders recursively owned by the configured user. Recursive handling changes owner and group only; `_paths_permissions` applies to explicitly declared directories and existing child modes are preserved.
- Web/DNS/Traefik follow the standard Saltbox/Sandbox templates (subdomain/domain/port/url; DNS record/zone/proxy; traefik defaults).
- Keep port allocation inputs, assigned-port lookups, and allocation bounds in a dedicated top-level `Ports` section. The Docker `# Ports` subsection contains only actual container port-bind defaults, customizations, and their composed list.
- Remove a role's existing Docker container before assigning ports. The allocator treats every remaining running or stopped container binding as unavailable and never adopts an existing container port.
- Every role declaring `<role>_role_traefik_enabled` also declares the complete API router contract: middleware defaulted to `traefik_default_middleware_api`, an empty custom middleware layer, an API-enabled toggle, and an API endpoint. Use `false` and an empty endpoint when the role has no default API route.
- A parent role that exposes a namespaced web adapter through an included Traefik-enabled role declares the complete regular and API Traefik contract under the parent namespace and forwards every field into the included role's `*_role_traefik_*` variables.
- Canonical web URL defaults use `lookup('role_web', role='<role>', scheme='https')`; canonical host defaults omit `scheme`. Named endpoint families pass `endpoint='<family>'`.
- Keep local-service, credential-bearing, port/path, and URL-from-host variants explicit so existing override layering remains authoritative.
- Docker:
  - Define container, image-pull, image-repository, image-tag, composed-image,
    hostname, and restart-policy defaults for roles using the shared Docker
    container task. Define network alias/default/custom/composed defaults unless
    an explicit supported network mode replaces attached networks.
  - Container state is owned by the shared Docker container task, which creates
    containers in the started state. Do not add a role-local `_docker_state`
    default.
  - A computed Docker image must define `_docker_image_repo` and `_docker_image_tag` defaults and access both through explicit `lookup('role_var', ..., role='<role>')` calls.
  - Network aggregates must use either `docker_networks_common + _docker_networks_default + _docker_networks_custom` or the interface-pinned variant. The interface-pinned variant may add only `com.docker.network.endpoint.ifname` to common networks with `map('combine', ...)`, and the application network must pin a distinct interface. Both variants keep custom last.
  - Do not override network aliases or use other custom `map('combine', ...)` logic.
  - GPU-capable roles declare `<role>_role_docker_gpu_enabled: true` in defaults and rely on the shared Docker container task. Do not include `set_docker_gpu_variables.yml` from application role tasks. Global `use_intel` and `use_nvidia` remain mandatory gates; `_docker_nvidia_disabled` and `_docker_dev_dri_disabled` are optional per-container opt-outs.
  - When Docker hosts are used, compose only the role-local `_docker_hosts_default` and `_docker_hosts_custom` mappings; do not add `docker_hosts_common`.
  - Set `<role>_role_docker_networks_alias` to the role name variable (e.g., `{{ <role>_name }}`); avoid custom alias strings.
  - Only include the ports block if the app needs host‑published ports.
  - Define Docker healthcheck tests as an explicit block list beginning with
    `CMD`, `CMD-SHELL`, or `NONE`. Prefer `CMD`; when shell syntax requires
    `CMD-SHELL`, add the exact `# saltbox-lint allow cmd-shell` directive to the
    `test:` line.
  - Follow the Saltbox linter for parser-level Jinja formatting; do not
    duplicate its indentation algorithms in this guidance.
  - Avoid custom security/capability defaults unless there is a clear repo precedent.
  - Do not add `_role_docker_` sections with empty defaults. Networks are always
    defined for normally attached containers; omit them only when an explicit
    supported network mode replaces attached networks. Omit
    envs/volumes/ports/labels/etc. unless used.
  - Conditional ports may intentionally default to no host bindings; do not require `_docker_ports_custom` to be unconditional without first confirming the role's exposure semantics.
  - When an application data path has a matching environment setting, set it explicitly to the container-side volume path so an upstream default change cannot redirect persisted data.
  - Treat `<role>_role_docker_envs_custom` only as the final environment override layer; do not inspect it to compute first-class role defaults.
  - When an image ignores PUID/PGID but supports an arbitrary runtime user, use `{{ uid }}:{{ gid }}` as the Docker user and recursively normalize existing appdata ownership without changing file modes.
- Build `*_role_depends_on` from explicit container names or role-local
  variables. If you use `lookup('role_var', ...)` for another Sandbox role's
  container, ensure that role is listed in `sandbox.yml` so its defaults are
  loaded; its tag can be its own or `never`. Saltbox role defaults are supplied
  by `pre_tasks` and do not require Sandbox registration.
- For multi-role apps, keep all user-facing settings in the main role; imported roles should not define their own settings defaults.
- Keep PostgreSQL-specific defaults in a dedicated `Postgres` section; only the `<role>_role_postgres_deploy` toggle may remain in `Settings`.
- In sub-roles, environment variable lookups that rely on settings must target the main role (use `lookup('role_var', ..., role='<main_role>')`).
- Default initial application-administrator username, password, and email
  settings in the main role to `user.name`, `user.pass`, and `user.email`, and
  have sub-roles use those settings. Provider, SMTP, database, and service
  credentials require their own role-local settings.
- When an application imposes stricter credential rules than the global defaults, wrap the global value in a role-local setting and direct validation failures to that override so users do not have to change the global credential.
- Name internal computed defaults with a `_lookup` suffix instead of
  `_effective`, and place the appropriate directive immediately above each
  lookup variable. `# Do not edit or override using the inventory` is a hard
  prohibition for values that must never be changed through inventory.
  `# Skip docs` hides an internal variable from generated documentation because
  users are not expected to edit it, but it is not an absolute prohibition on
  inventory overrides. Preserve the stronger directive when it already exists,
  and never stack the two comments.

## Task file patterns

- Use `ansible.builtin.include_tasks` and `ansible.builtin.include_role` for
  task and role composition; do not introduce static imports. When wrapper tags
  must apply to included child tasks, keep the tags on the include and repeat
  them under `apply.tags`.
- Before changing a shared `resources/tasks` file's inputs, setup, or variable resolution, search Saltbox and Sandbox for every direct include. Treat multiple callers as a real interface: pass explicit inputs from every caller, exercise each distinct caller condition, and keep the shared task independent of stale host-level `set_fact` values.
- When a shared resource replaces a registered task, expose the effective underlying module result under a caller-named variable and preserve the caller's failure suppression and success/failure tests.
- Treat fixtures that pin computed facts as downstream-only. Shared-fact acceptance completes only when each real tagged playbook path resolves and schedules the intended producer through `roles_path`, including same-name shadow roles, and consumes the produced fact downstream.
- Before an application role imports a database or persistent-backend role, remove every existing application or worker container that can access that backend. Place these removals after non-mutating validation and fact resolution but before the first backend import; removing a legacy backend container does not satisfy this requirement.
- Common flow (as applicable): DNS → remove container → create directories → create container.
- Use `resources_tasks_path` helpers: `docker/remove_docker_container.yml`, `directories/create_directories.yml`, `docker/create_docker_container.yml`.
- Perform Git checkouts through `resources/tasks/git/clone_git_repo.yml`; do not
  call `ansible.builtin.git` directly from role tasks.
- Fetch GitHub API metadata through
  `resources/tasks/git/github_api_request.yml`; do not reference `svm`
  directly from role defaults or tasks, and keep archive downloads direct.
- For simple web installers with deterministic defaults, prefer completing the upstream installer with `ansible.builtin.uri` on fresh non-CI installs, protect submitted credentials with `no_log`, and verify the generated config; correct existing configs separately.
- Validate required settings with `ansible.builtin.fail` in the main role that imports other roles (do not put required-variable fails in sub-roles).
- Persist generated secrets that must remain stable across runs with `saltbox_facts`; expose a role setting defaulted to the registered fact and validate the resolved setting before container creation.
- In assertions, prefer boolean Jinja tests such as `is search(...)` or `is match(...)` over filters such as `regex_search` that return strings or `none`.
- When validating API keys derived from `get_info`, fail if the value is empty or equals the default `"not installed"` string.
- For multi‑service apps, include the backend/DB role first, then frontend.
- When defaulting service URLs or API keys from existing instances, include
  `resources/tasks/instances/get_info.yml` and pass an explicit `get_info_list`
  containing every service whose discovered information the role consumes.
- `sandbox.yml` runs Saltbox's `pre_tasks` role before application roles, and
  its variable-loading step imports every Saltbox role `defaults/main.yml` into
  the Sandbox play. Treat variables provided by Saltbox role defaults,
  including instance lists, as defined; do not add redundant existence guards,
  discovery, or duplicate defaults for them.

## Multi-role wiring

- If a parent role includes a backend role, pass settings explicitly in `include_role` vars.
- Keep backend appdata under the parent role’s appdata folder unless the repo shows a different pattern.
- When sharing appdata, set the backend role `*_paths_location` to the main role `*_paths_location` to avoid creating unused folders.
- If a backend role shares the main role appdata, omit the backend Paths section and skip `create_directories`; use the main role paths directly in the backend volume defaults.
- If the main role includes a backend role via `include_role`, do not give the backend the same tag in `sandbox.yml` (that would double‑run).
- If the backend is a companion role not meant to run by itself, tag it `never` and place it under the “No CI” section.
- If the backend is meant to run by itself, give it its own tag (not the main role’s) and keep it under Apps Start.
- If you do put the backend role in `sandbox.yml` with the same tag as the main role, remove the `include_role`.

## Validation

- Treat `.github/workflows/sandbox.yml` and the Saltbox linter as the current
  sources of truth for mechanically enforced checks; do not reproduce their
  complete rule sets here.
- Before handoff, run `ansible-lint`, the Saltbox linter against this checkout,
  and `git diff --check`. Run `./scripts/check_missing_entries.sh` when changing
  roles or `sandbox.yml`. Follow `.github/workflows/sandbox.yml` for the current
  Saltbox checkout and dependency setup.
- Run installation or behavior tests only on an explicitly designated
  disposable or test Saltbox host. Report static validation separately from
  live role validation, and state any coverage that could not be performed.
