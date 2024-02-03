import os
import sys

def lint_ansible_defaults(content):
    errors = []
    lines = content.split('\n')
    
    multi_line_jinja_start = None
    within_multi_line_jinja = False

    for line_no, line in enumerate(lines, start=1):
        stripped_line = line.strip()

        if stripped_line == '---':
            continue

        if '{{' in stripped_line and not within_multi_line_jinja:
            multi_line_jinja_start = line.find('{{')
            within_multi_line_jinja = '}}' not in stripped_line

        elif within_multi_line_jinja:
            if 'if' in stripped_line or 'else' in stripped_line:
                if line.find('if') < multi_line_jinja_start and line.find('else') < multi_line_jinja_start:
                    errors.append(f"Line {line_no}: 'if/else' within Jinja expression should align with the start.")

            if '}}' in stripped_line:
                within_multi_line_jinja = False

        if '}}' in stripped_line and within_multi_line_jinja:
            within_multi_line_jinja = False

    return errors

def crawl_and_lint_ansible_roles(roles_dir):
    errors_found = False

    if not os.path.exists(roles_dir):
        print("Roles directory does not exist.")
        return

    for role_name in os.listdir(roles_dir):
        defaults_main_path = os.path.join(roles_dir, role_name, "defaults", "main.yml")
        if os.path.isfile(defaults_main_path):
            with open(defaults_main_path, 'r') as file:
                content = file.read()
                errors = lint_ansible_defaults(content)
                if errors:
                    errors_found = True
                    for error in errors:
                        print(f"{defaults_main_path}: {error}")

    sys.exit(1 if errors_found else 0)

# Check if the script was run with a directory argument
if len(sys.argv) < 2:
    print("Usage: python script.py /path/to/your/ansible/roles")
    sys.exit(1)

roles_directory_path = sys.argv[1]
crawl_and_lint_ansible_roles(roles_directory_path)
