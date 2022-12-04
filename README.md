# Saltbox Sandbox Repo
[![Discord](https://img.shields.io/discord/853755447970758686)](https://discord.gg/ugfKXpFND8)
[![CI](https://github.com/saltyorg/Sandbox/actions/workflows/sandbox.yml/badge.svg)](https://github.com/saltyorg/Sandbox/actions/workflows/sandbox.yml)
[![License:](https://img.shields.io/github/license/saltyorg/Sandbox)](LICENSE.md)

Sandbox Repository for Unofficial Saltbox Add-ons

Roles may get moved to the main repo if they become officially maintained.

### Requirements

- [Saltbox](https://github.com/saltyorg/Saltbox/)

### Install

Install Sandbox using the Saltbox installer.
```
sb install sandbox
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
        <a href=https://github.com/owine>
            <img src=https://avatars.githubusercontent.com/u/4283702?v=4 width="100;"  alt=owine/>
            <br />
            <sub style="font-size:14px"><b>owine</b></sub>
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
        <a href=https://github.com/JigSawFr>
            <img src=https://avatars.githubusercontent.com/u/5781907?v=4 width="100;"  alt=JigSaw/>
            <br />
            <sub style="font-size:14px"><b>JigSaw</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/BeansIsFat>
            <img src=https://avatars.githubusercontent.com/u/24848012?v=4 width="100;"  alt=BeansIsFat/>
            <br />
            <sub style="font-size:14px"><b>BeansIsFat</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/RaneyDazed>
            <img src=https://avatars.githubusercontent.com/u/95461636?v=4 width="100;"  alt=CHAIR/>
            <br />
            <sub style="font-size:14px"><b>CHAIR</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/keldian>
            <img src=https://avatars.githubusercontent.com/u/953679?v=4 width="100;"  alt=keldian/>
            <br />
            <sub style="font-size:14px"><b>keldian</b></sub>
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
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/hereisderek>
            <img src=https://avatars.githubusercontent.com/u/839795?v=4 width="100;"  alt=Derek Zhu/>
            <br />
            <sub style="font-size:14px"><b>Derek Zhu</b></sub>
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
        <a href=https://github.com/kxzaon>
            <img src=https://avatars.githubusercontent.com/u/46218?v=4 width="100;"  alt=kxzaon/>
            <br />
            <sub style="font-size:14px"><b>kxzaon</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/8a8al00ey>
            <img src=https://avatars.githubusercontent.com/u/109389709?v=4 width="100;"  alt=8a8al00ey/>
            <br />
            <sub style="font-size:14px"><b>8a8al00ey</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Cajs>
            <img src=https://avatars.githubusercontent.com/u/6383356?v=4 width="100;"  alt=Cameron Stephen/>
            <br />
            <sub style="font-size:14px"><b>Cameron Stephen</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/jolbol1>
            <img src=https://avatars.githubusercontent.com/u/5064896?v=4 width="100;"  alt=James Shopland/>
            <br />
            <sub style="font-size:14px"><b>James Shopland</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/javi11>
            <img src=https://avatars.githubusercontent.com/u/3855051?v=4 width="100;"  alt=Javier Blanco/>
            <br />
            <sub style="font-size:14px"><b>Javier Blanco</b></sub>
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
        <a href=https://github.com/kungfoome>
            <img src=https://avatars.githubusercontent.com/u/421589?v=4 width="100;"  alt=Matt Martinez/>
            <br />
            <sub style="font-size:14px"><b>Matt Martinez</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/nickstarkloff>
            <img src=https://avatars.githubusercontent.com/u/51816213?v=4 width="100;"  alt=Nick Starkloff/>
            <br />
            <sub style="font-size:14px"><b>Nick Starkloff</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/addbee>
            <img src=https://avatars.githubusercontent.com/u/4490516?v=4 width="100;"  alt=adbe/>
            <br />
            <sub style="font-size:14px"><b>adbe</b></sub>
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
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/markschrik>
            <img src=https://avatars.githubusercontent.com/u/56775030?v=4 width="100;"  alt=markschrik/>
            <br />
            <sub style="font-size:14px"><b>markschrik</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/tipdec-siblyn>
            <img src=https://avatars.githubusercontent.com/u/99356862?v=4 width="100;"  alt=~tipdec-siblyn/>
            <br />
            <sub style="font-size:14px"><b>~tipdec-siblyn</b></sub>
        </a>
    </td>
</tr>
</table>
