# Hacker-Target Reverse IP Lookup TOOL
A handy python based tool designed to find domains list from the IP address list file<br>

Usage:
-----

Simple as abc...
1. Make a file containing IP addresses (one IP per line).<br>
~~2. Open the script file and then type in the file name that you created now with having list of IP.~~
2. Now you can path the file containing IPs with argument ```-l OR --list```<br>
3. The rest of the works will be done by the program itself. You can find the collected domain list in the ~~grabbed.txt~~ reverse_result.txt file if there is any record found under certain IP addresses.<br>

Limitations:
-----------

At most 100 Look up per IP address(per day) is set by the hackertarget.com site.
You may use vpn to breach this limit.<br>

### PS: 
This Tool is taken from [@TheChoyon](https://github.com/TheChoyon/HackerTargetRevLookUP) and modified so it could run inside any
script or through terminal without user interaction.<br>
I traied to contact @TheChoyon to commit the changes to the master repo BUT no response.
