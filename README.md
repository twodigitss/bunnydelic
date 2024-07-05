# Bunnydelic
The purpose of this fetch alternative is create a fetch tool that does not need to be "static" all the time, 
printing just one set of colors and ascii art staying as the same until you change it manually. <br>
This tool `offers` to randomize the color set, randomizes the ascii art (if you do not change it manually of course)
each time the command is launched, between other functions found in the configuration file. <br>
You can customize the looks modifying some parameters in `config.py` <br>
<br>
![Colorschemes output example](/images/demonstration2.png)<br>

Highly inspired in bunnyfetch by Rosettea. <br>
https://github.com/Rosettea/bunnyfetch.

## Dependencies _(that you must install)_
1. Python
2. Make
3. awk (i believe)

## Instructions
1. Clone the repo locally using `git clone paste_repo_link_here`<br>
2. Change directory to the folder with `cd bunnydelic`<br>
3. Install as binary with  `make install`<br>
3.1. To uninstall use `make uninstall`<br>
4. Run as  `bunnydelic`<br>

## Supported distros _(hopefully)_
- Arch linux and derivated distros
- Debian and derivated distros
- Redhat and derivated distros


## Future plans 
+ make an aur package when it's stable
+ make an deb package when it's stable

## Author notes
This fetch uses colors of your system to colorize the output.
I recommend to use a colorscheme for your Xresources file, like rosepine, dracula, nord, etc. <br>
It also may look weird depending of the font, monospace looks weird. I recommend nerd fonts or some other.<br> 
https://www.nerdfonts.com/font-downloads
