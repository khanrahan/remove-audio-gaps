# Remove Audio Gaps

Plugin for [Autodesk Flame software](http://www.autodesk.com/products/flame).

Remove silent audio gaps from selected sequences.  These are created, for example, when using Desktop > Tools > Utilities > Desktop Utilities > Copy/Duplicate > Audio.

![screenshot](screenshot.png)

## Compatibility
|Release Version|Flame Version|
|---|---|
|v2.X.X|Flame 2022 and up|
|v1.X.X|Flame 2021 up to 2021.2|

## Installation

### Flame 2025 and newer
To make available to all users on the workstation, copy `remove_audio_gaps.py` to `/opt/Autodesk/shared/python/`

For specific users, copy `remove_audio_gaps.py` to the appropriate path below...
|Platform|Path|
|---|---|
|Linux|`/home/<user_name>/flame/python/`|
|Mac|`/Users/<user_name>/Library/Preferences/Autodesk/flame/python/`|

### Flame 2022 up to 2024.2
To make available to all users on the workstation, copy `remove_audio_gaps.py` to `/opt/Autodesk/shared/python/`

For specific users, copy `remove_audio_gaps.py` to `/opt/Autodesk/user/<user name>/python/`

### Last Step
Finally, inside of Flame, go to Flame (fish) menu `->` Python `->` Rescan Python Hooks

## Menus
- Right-click selected sequences on the Desktop `->` Edit... `->` Remove Audio Gaps
- Right-click selected sequences in the Media Panel `->` Edit... `->` Remove Audio Gaps

## Acknowledgements
Many thanks to [pyflame.com](http://www.pyflame.com)
