# Saltbox Community Repo
[![Discord](https://img.shields.io/discord/853755447970758686)](https://discord.gg/ugfKXpFND8)
[![Docs:](https://img.shields.io/badge/docs-docs.saltbox.dev-blue)](https://docs.saltbox.dev)
[![CI](https://github.com/saltyorg/Community/actions/workflows/community.yml/badge.svg)](https://github.com/saltyorg/Community/actions/workflows/community.yml)
[![Ansible Lint](https://github.com/saltyorg/Community/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/saltyorg/Community/actions/workflows/ansible-lint.yml)
[![License:](https://img.shields.io/github/license/saltyorg/Community)](LICENSE.md)

Community Repository for Unofficial Saltbox Add-ons

### Requirements

- [Saltbox](https://github.com/saltyorg/Saltbox/)

### Documentation

- [Docs](https://docs.saltbox.dev) (WIP)

### Roles

List of roles can be found by running
```
cd /opt/community && sudo ansible-playbook community.yml --list-tags 2>&1 | grep "TASK TAGS" | cut -d":" -f2 | awk '{sub(/\[/, "")sub(/\]/, "")}1' | sed -e 's/,//g' | xargs -n 1 | sort -u
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
</tr>
</table>
