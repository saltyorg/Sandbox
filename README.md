# Saltbox Sandbox Repo
[![Discord](https://img.shields.io/discord/853755447970758686)](https://discord.gg/ugfKXpFND8)
[![CI](https://github.com/saltyorg/Sandbox/actions/workflows/sandbox.yml/badge.svg)](https://github.com/saltyorg/Sandbox/actions/workflows/sandbox.yml)
[![Ansible Lint](https://github.com/saltyorg/Sandbox/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/saltyorg/Sandbox/actions/workflows/ansible-lint.yml)
[![License:](https://img.shields.io/github/license/saltyorg/Sandbox)](LICENSE.md)

Sandbox Repository for Unofficial Saltbox Add-ons

Roles may get moved to the main repo if they become officially maintained.

### Requirements

- [Saltbox](https://github.com/saltyorg/Saltbox/)

### Install

Install Sandbox using the Saltbox installer.
```
saltbox install sandbox
```

### Documentation

- [Sandbox](https://docs.saltbox.dev/sandbox/basics/)

### Roles

List of roles can be found by running
```
cd /opt/sandbox && sudo ansible-playbook sandbox.yml --list-tags 2>&1 | grep "TASK TAGS" | cut -d":" -f2 | awk '{sub(/\[/, "")sub(/\]/, "")}1' | sed -e 's/,//g' | xargs -n 1 | sort -u
```
or
```
sb list
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
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/owine>
            <img src=https://avatars.githubusercontent.com/u/4283702?v=4 width="100;"  alt=owine/>
            <br />
            <sub style="font-size:14px"><b>owine</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/chazlarson>
            <img src=https://avatars.githubusercontent.com/u/3865541?v=4 width="100;"  alt=Chaz Larson/>
            <br />
            <sub style="font-size:14px"><b>Chaz Larson</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/TABLE272>
            <img src=https://avatars.githubusercontent.com/u/11992630?v=4 width="100;"  alt=TABLE272/>
            <br />
            <sub style="font-size:14px"><b>TABLE272</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/grostim>
            <img src=https://avatars.githubusercontent.com/u/3714755?v=4 width="100;"  alt=grostim/>
            <br />
            <sub style="font-size:14px"><b>grostim</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/hackmonker>
            <img src=https://avatars.githubusercontent.com/u/46002790?v=4 width="100;"  alt=ハックモンカー/>
            <br />
            <sub style="font-size:14px"><b>ハックモンカー</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/TurboCheetah>
            <img src=https://avatars.githubusercontent.com/u/19479111?v=4 width="100;"  alt=Turbo/>
            <br />
            <sub style="font-size:14px"><b>Turbo</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/dvsmasta>
            <img src=https://avatars.githubusercontent.com/u/14364893?v=4 width="100;"  alt=dvsmasta/>
            <br />
            <sub style="font-size:14px"><b>dvsmasta</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/keldian>
            <img src=https://avatars.githubusercontent.com/u/953679?v=4 width="100;"  alt=keldian/>
            <br />
            <sub style="font-size:14px"><b>keldian</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/JohnClementine>
            <img src=https://avatars.githubusercontent.com/u/52635735?v=4 width="100;"  alt=JohnClementine/>
            <br />
            <sub style="font-size:14px"><b>JohnClementine</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/ayykamp>
            <img src=https://avatars.githubusercontent.com/u/32194363?v=4 width="100;"  alt=ayykamp/>
            <br />
            <sub style="font-size:14px"><b>ayykamp</b></sub>
        </a>
    </td>
</tr>
</table>
