

The research for this project consisted of research of wireless auditing tools, python scripting,
and other security utility tools, and how every part serves a purpose. The code for this project is
primarily centered off python’s subprocess module, and other common techniques associated
with python scripting. The general handling part of the script handles multiple parts of the
sequence of attacking a wireless network. For example, the beginning part manages sniffing for
wireless networks with WPA protocol in place and the process of selecting the target network.
There are other sections in the code that manage parts involved in cracking, accessing, and
miscellaneous processes in relation to entry to a wireless network. The main purpose behind this
project is to portray how easy it can be for attackers to access WPA/WPA2 personal wireless
networks due to improper/weak passwords. The ‘automation’ factor in the project is mainly for
speed and overall simplicity with the process of sniffing, cracking, and potentially accessing the
wireless network. Some aspects of automation would require much more coding to make it work,
so this project mainly puts automation into the essential parts of wireless network attacking.

The script uses the aircrack-ng suite, with most of the focus being placed on airodump-ng and aireplay-ng 
which handle the deatuhentication, disassociating, and sniffing processes. More explaination can come from the general 
description document in the repository which shows screenshots of the script and how it works. 

Note that certain parts of the beginning could not be automated due to the fact that the operator
of the script has to selectively target the network they are looking for, which cannot really be
automated in most cases. Also, some parts of the airodump-ng and aireplay-ng processes cannot
be automated as they require the operator to exit the process at the correct time.
