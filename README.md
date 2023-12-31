## Introduction
For GIT (Github) testing only! DCSS Saver is small Python GUI application to save your character in __Dungeon Crawl Stone Soup__ game!<br />

![Screenshot](Screenshot.png)
## Current Releases
__0.1__ - Initial commit;<br />
__0.1a__ - Added Mac OS support;<br />
## Platforms
Tested on a Fedora Workstation 39 and Mac OS Sonoma. `Python3` and `pip` required. And `tkinter` library:
 - For Debian-based distros:
 > apt install python3-tk
 - For RPM-based distros:
 > dnf install python3-tkinter
 - For mac OS:
 > brew install python-tk
## Usage
Just launch it! <br />
Typical launch:
> *python3 saver.py*

When you need to save your character's progress, close game, press on a character and then press `Save character`. It will be copied to saves directory. When you need to restore your character from save file (usually it happens when you die), do not press ESC after morgue message! Press `Load save` and press ESC in game. Voila! You can continue now.
## Plans
 - Windows support
 - Read description from save file to know character's class, level, etc;
## Licenses
Use and modify on your own risk.