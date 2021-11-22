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
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/desimaniac>
            <img src=https://avatars.githubusercontent.com/u/5501908?v=4 width="100;"  alt=desimaniac/>
            <br />
            <sub style="font-size:14px"><b>desimaniac</b></sub>
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
        <a href=https://github.com/Superduper09>
            <img src=https://avatars.githubusercontent.com/u/17391966?v=4 width="100;"  alt=herp/>
            <br />
            <sub style="font-size:14px"><b>herp</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Migz93>
            <img src=https://avatars.githubusercontent.com/u/33037112?v=4 width="100;"  alt=Migz93/>
            <br />
            <sub style="font-size:14px"><b>Migz93</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/BluebonnetSK>
            <img src=https://avatars.githubusercontent.com/u/43162289?v=4 width="100;"  alt=BluebonnetSK/>
            <br />
            <sub style="font-size:14px"><b>BluebonnetSK</b></sub>
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
        <a href=https://github.com/satzisa>
            <img src=https://avatars.githubusercontent.com/u/54035525?v=4 width="100;"  alt=isa/>
            <br />
            <sub style="font-size:14px"><b>isa</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/RXWatcher>
            <img src=https://avatars.githubusercontent.com/u/14085001?v=4 width="100;"  alt=RXWatcher/>
            <br />
            <sub style="font-size:14px"><b>RXWatcher</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Kalroth>
            <img src=https://avatars.githubusercontent.com/u/6299049?v=4 width="100;"  alt=Martin Danielsen/>
            <br />
            <sub style="font-size:14px"><b>Martin Danielsen</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/paris-ci>
            <img src=https://avatars.githubusercontent.com/u/3063324?v=4 width="100;"  alt=Arthur/>
            <br />
            <sub style="font-size:14px"><b>Arthur</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/FML128>
            <img src=https://avatars.githubusercontent.com/u/33214722?v=4 width="100;"  alt=Merlin Jehli/>
            <br />
            <sub style="font-size:14px"><b>Merlin Jehli</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Banjer>
            <img src=https://avatars.githubusercontent.com/u/864725?v=4 width="100;"  alt=Bas/>
            <br />
            <sub style="font-size:14px"><b>Bas</b></sub>
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
        <a href=https://github.com/theotocopulitos>
            <img src=https://avatars.githubusercontent.com/u/1540135?v=4 width="100;"  alt=theotocopulitos/>
            <br />
            <sub style="font-size:14px"><b>theotocopulitos</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/sil3ntc>
            <img src=https://avatars.githubusercontent.com/u/55059643?v=4 width="100;"  alt=Sil3nt/>
            <br />
            <sub style="font-size:14px"><b>Sil3nt</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/fringillidaes>
            <img src=https://avatars.githubusercontent.com/u/57169808?v=4 width="100;"  alt=finch/>
            <br />
            <sub style="font-size:14px"><b>finch</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/atilling>
            <img src=https://avatars.githubusercontent.com/u/1081300?v=4 width="100;"  alt=Andrew Tillinghast/>
            <br />
            <sub style="font-size:14px"><b>Andrew Tillinghast</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/JackDallas>
            <img src=https://avatars.githubusercontent.com/u/3620144?v=4 width="100;"  alt=Dallas/>
            <br />
            <sub style="font-size:14px"><b>Dallas</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/stijnthurkow>
            <img src=https://avatars.githubusercontent.com/u/22298631?v=4 width="100;"  alt=Stijn/>
            <br />
            <sub style="font-size:14px"><b>Stijn</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/fuller882>
            <img src=https://avatars.githubusercontent.com/u/43045024?v=4 width="100;"  alt=fuller882/>
            <br />
            <sub style="font-size:14px"><b>fuller882</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/javi11>
            <img src=https://avatars.githubusercontent.com/u/3855051?v=4 width="100;"  alt=Javier Blanco/>
            <br />
            <sub style="font-size:14px"><b>Javier Blanco</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Thomvh>
            <img src=https://avatars.githubusercontent.com/u/1483055?v=4 width="100;"  alt=Thomvh/>
            <br />
            <sub style="font-size:14px"><b>Thomvh</b></sub>
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
        <a href=https://github.com/giosann>
            <img src=https://avatars.githubusercontent.com/u/10052873?v=4 width="100;"  alt=Giorgio/>
            <br />
            <sub style="font-size:14px"><b>Giorgio</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/RyanRadly>
            <img src=https://avatars.githubusercontent.com/u/1883477?v=4 width="100;"  alt=RyanRadly/>
            <br />
            <sub style="font-size:14px"><b>RyanRadly</b></sub>
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
        <a href=https://github.com/astrodad>
            <img src=https://avatars.githubusercontent.com/u/1663239?v=4 width="100;"  alt=astrodad/>
            <br />
            <sub style="font-size:14px"><b>astrodad</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/bonny1992>
            <img src=https://avatars.githubusercontent.com/u/1154368?v=4 width="100;"  alt=bonny1992/>
            <br />
            <sub style="font-size:14px"><b>bonny1992</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/zZebrahz>
            <img src=https://avatars.githubusercontent.com/u/11633690?v=4 width="100;"  alt=zZebrahz/>
            <br />
            <sub style="font-size:14px"><b>zZebrahz</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/EnorMOZ>
            <img src=https://avatars.githubusercontent.com/u/13998170?v=4 width="100;"  alt=EnorMOZ/>
            <br />
            <sub style="font-size:14px"><b>EnorMOZ</b></sub>
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
        <a href=https://github.com/primaxius>
            <img src=https://avatars.githubusercontent.com/u/20571191?v=4 width="100;"  alt=primaxius/>
            <br />
            <sub style="font-size:14px"><b>primaxius</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Silent-Remux>
            <img src=https://avatars.githubusercontent.com/u/16107603?v=4 width="100;"  alt=Silent/>
            <br />
            <sub style="font-size:14px"><b>Silent</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/AJohnsonCHC>
            <img src=https://avatars.githubusercontent.com/u/666617?v=4 width="100;"  alt=Andrew Johnson/>
            <br />
            <sub style="font-size:14px"><b>Andrew Johnson</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/luxus>
            <img src=https://avatars.githubusercontent.com/u/7449?v=4 width="100;"  alt=Kai/>
            <br />
            <sub style="font-size:14px"><b>Kai</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/KaiserBh>
            <img src=https://avatars.githubusercontent.com/u/41852205?v=4 width="100;"  alt=KaiserBh/>
            <br />
            <sub style="font-size:14px"><b>KaiserBh</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/KunaalKumar>
            <img src=https://avatars.githubusercontent.com/u/7245674?v=4 width="100;"  alt=Kunaal/>
            <br />
            <sub style="font-size:14px"><b>Kunaal</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Loomaanaatii>
            <img src=https://avatars.githubusercontent.com/u/10216384?v=4 width="100;"  alt=Loomaanaatii/>
            <br />
            <sub style="font-size:14px"><b>Loomaanaatii</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Minds3t>
            <img src=https://avatars.githubusercontent.com/u/20452868?v=4 width="100;"  alt=Minds3t/>
            <br />
            <sub style="font-size:14px"><b>Minds3t</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/rar0ch>
            <img src=https://avatars.githubusercontent.com/u/62119999?v=4 width="100;"  alt=Robin Rapp/>
            <br />
            <sub style="font-size:14px"><b>Robin Rapp</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Tr4il>
            <img src=https://avatars.githubusercontent.com/u/6537388?v=4 width="100;"  alt=Tr4il/>
            <br />
            <sub style="font-size:14px"><b>Tr4il</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/TheUltimateC0der>
            <img src=https://avatars.githubusercontent.com/u/3315612?v=4 width="100;"  alt=Ultimate/>
            <br />
            <sub style="font-size:14px"><b>Ultimate</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Visorask>
            <img src=https://avatars.githubusercontent.com/u/54461452?v=4 width="100;"  alt=Visorask/>
            <br />
            <sub style="font-size:14px"><b>Visorask</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/codsane>
            <img src=https://avatars.githubusercontent.com/u/12850297?v=4 width="100;"  alt=codsane/>
            <br />
            <sub style="font-size:14px"><b>codsane</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/l3uddz>
            <img src=https://avatars.githubusercontent.com/u/7897162?v=4 width="100;"  alt=l3uddz/>
            <br />
            <sub style="font-size:14px"><b>l3uddz</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/muplah>
            <img src=https://avatars.githubusercontent.com/u/12591932?v=4 width="100;"  alt=muplah/>
            <br />
            <sub style="font-size:14px"><b>muplah</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/no5tyle>
            <img src=https://avatars.githubusercontent.com/u/32665563?v=4 width="100;"  alt=no5tyle/>
            <br />
            <sub style="font-size:14px"><b>no5tyle</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/rbraunschweig>
            <img src=https://avatars.githubusercontent.com/u/8337331?v=4 width="100;"  alt=rbraunschweig/>
            <br />
            <sub style="font-size:14px"><b>rbraunschweig</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/crowquillx>
            <img src=https://avatars.githubusercontent.com/u/58858875?v=4 width="100;"  alt=tan/>
            <br />
            <sub style="font-size:14px"><b>tan</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/tarek369>
            <img src=https://avatars.githubusercontent.com/u/36159724?v=4 width="100;"  alt=tarek369/>
            <br />
            <sub style="font-size:14px"><b>tarek369</b></sub>
        </a>
    </td>
</tr>
</table>
