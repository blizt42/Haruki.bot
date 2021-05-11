# Haruki.bot
Music bot revamped
Any sensitive date are removed.
Bot created by bamb00#4632

Note
----------------------------
* The 3rd major version of the discord bot Haruki
* If you somehow managed to stumble across this page, hi I guess
* 'music' folder needs to be added for it to work
* some commands may not work as they contain sensitive data (Yes, which have been removed)
* Codes are tweaked to suit the bot haruki

> OWO what's this? - Haruki

Add bot to server
----------------------------
https://discord.com/api/oauth2/authorize?client_id=782151291634712586&permissions=0&scope=bot

How to install (raspberry pi fresh install) (my personal guide, may not be the same)
---------------------------
1. install required python modules
  * ffmpeg
  * dnspython
  * googlesearch
  * praw
  * discord.py 1.5.1
  * [libsodium-dev](https://pynacl.readthedocs.io/eb/stable/install/) sudo apt-install libsodium-dev
  * pynacl
2. download and extract haruki zip
3. add bot to service. [How](https://www.raspberrypi.org/documentation/linux/usage/systemmd.md/)

Remote ssh
---------------------------
1. sudo raspi-config
2. enable ssh
3. [On pc](https://www.raspberrypi.org/documentation/remote-access/ssh/)

Haruki.service
---------------------------
[Unit]
Description=My service
After=network.target

[Service]
ExecStart=/usr/bin/python3 -u main.py
WorkingDirectory=/home/pi/myscript
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
