# Saltbox Sandbox Repo
[![Discord](https://img.shields.io/discord/853755447970758686)](https://discord.gg/ugfKXpFND8)
[![CI](https://github.com/saltyorg/Sandbox/actions/workflows/sandbox.yml/badge.svg)](https://github.com/saltyorg/Sandbox/actions/workflows/sandbox.yml)
[![Ansible Lint](https://github.com/saltyorg/Sandbox/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/saltyorg/Sandbox/actions/workflows/ansible-lint.yml)
[![License:](https://img.shields.io/github/license/saltyorg/Sandbox)](LICENSE.md)

Sandbox Repository for Unofficial Saltbox Add-ons

Roles may get moved to the Community or main repo if they become maintained.

### Requirements

- [Saltbox](https://github.com/saltyorg/Saltbox/)

### Documentation

- Undetermined

### Roles

List of roles can be found by running
```
cd /opt/sandbox && sudo ansible-playbook sandbox.yml --list-tags 2>&1 | grep "TASK TAGS" | cut -d":" -f2 | awk '{sub(/\[/, "")sub(/\]/, "")}1' | sed -e 's/,//g' | xargs -n 1 | sort -u
```

### Contributors

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/saltydk>
            <img src=https://avatars.githubusercontent.com/u/6587950?v=4 width="100;"  alt=salty/>
            <br />
            <sub style="font-size:14px"><b>salty</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/maximuskowalski>
            <img src=https://avatars.githubusercontent.com/u/13492750?v=4 width="100;"  alt=Max Kowalski/>
            <br />
            <sub style="font-size:14px"><b>Max Kowalski</b></sub>
        </a>
    </td>
</tr>
</table>
