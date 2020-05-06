# connectVPNOnStartUp

## It's just a script to start [Windscribe](https://windscribe.com/) vpn as a startup application for Ubuntu(it may work for other linux distros).

#### Guide

First clone this repo on any location of your system:
```
git clone https://github.com/programworld999/connectVPNOnStartUp
cd connectVPNOnStartUp

```
Then make sure that you have windscribe installed and account config. Now you need to just open your 'Startup Applications' and setup like this:
```
name: connectVPNOnStartUp
command: bash /home/sk/Startup Application/connectVPNOnStartUp/connectVPNOnStartUp.sh
I have my repo on '/home/sk/Startup Application/'. Basically you just have to run 'connectVPNOnStartUp.sh' as a bash
comment: connectVPNOnStartUp // you can just ignore this
```
and clicked on Add buttuon
