This is a template. For "how to make a linter", please check [the HOWTO](HOWTO.md).

-----------------------------------------------------------------

SublimeLinter-contrib-flog
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-flog.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-flog)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [flog](https://github.com/seattlerb/flog). It will be used with files that have the “ruby” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `flog` is installed on your system.

In order for `flog` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-contrib-flog settings:

|Setting|Description    |
|:------|:--------------|
|threshold | (float) Limit above which a method is marked with error. |

Example:

```json
  "flog": {
    "disable": false,
    "threshold": 12.0,
    "styles": [
      {
        "scope": "region.redish markup.warning.sublime_linter",
        "types": ["error"]
      },
      {
        "scope": "region.yellowish markup.warning.sublime_linter",
        "types": ["warning"]
      },
      {
        "priority": 1,
        "icon": "triangle",
        "mark_style": "fill",
        "annotation": "{linter}:{msg}",
      }
    ]
  },
```
