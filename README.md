# smla-info

Chinese text segmentation.

### Installation

We use PyPI to distribute our software.
Only support Python3+ now.

```sh
$ sudo apt install python3-pip
$ pip3 install smla_cut
```

```sh
$ python3
Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from smla_cut import smla_cut
>>> smla_cut.cut("梅花鹿")
:) Load emit file: /usr/local/lib/python3.6/dist-packages/smla_cut/data/emit/emit.json
:) Total Hans number: 20950
{'梅': {'B': 0.2669902912621359, 'M': 0.21359223300970873, 'E': 0.5048543689320388, 'S': 0.014563106796116505}}
{'花': {'B': 0.3111986494091165, 'M': 0.14800225098480585, 'E': 0.24648283624085537, 'S': 0.29431626336522226}}
{'鹿': {'B': 0.1937984496124031, 'M': 0.13178294573643412, 'E': 0.5193798449612403, 'S': 0.15503875968992248}}
['梅', '花', '鹿', '/']
['B', 'M', 'E', '/']
(['梅', '花', '鹿', '/'], ['B', 'M', 'E', '/'])

```
