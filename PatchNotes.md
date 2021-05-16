# Patch Notes for Haruki bot.

@ 5/8/2021 HarukiV1.2
--------------------------------------
* Added check_url method under YTDLSource class
* Removed inside global variable
* Modified change_status()
* Modified help command
* Reworked dma command to only allow 3 msg max
* Reworked view command to show now playing and searched song based on input
* Reworked music player part of play command to allow pausing of song
* Added pause command
* modified shutdown command (untested)

> OWO whats this? ~Haruki

@ 5/9/2021 HarukiV1.3
--------------------------------------
* Modified check_url in Class YTDLSource to only extract data from search
* Modified view command to only allow up to first 5 songs to be searched to prevent overloading
* Added global variable loopsong
* Modified play command to use allow looping
* Added new loop command

### Minor changes
* Global nowplaying set to say No song playing when initialized
* Added help loop to help command

> Time to listen to the same music again! ~Haruki

@ 5/11/2021 HarukiV1.4 Organization Update
--------------------------------------
* Complete rework of the haruki's frame work (one main script into mulitple scripts)
* Removed global variables
* Usage of OOP instead of modular programming
* Usage of cogs to separate command category
* Commands have been separated nto individual file in the new cogs folder
* Music has been reworked yet again (3rd version) (Using asyncio)
* Added cogs folder
* Added misc folder
* Added Admin command cog

### Music rework
* MusicPlayer class is added (allows multiple server to listen at once)
* Playing a playlist is now done using asyncio task, event and loop function
* Added resume command
* Removed queue command

### Minor changes
* Haruki.jpg moved to misc folder
* Added yeetball.txt to misc folder
* Modified yeetball command to access responses from yeetball.txt

> WoAh TEcHnOLogy ~Haruki

@ 5/16/2021 HarukiV1.5
--------------------------------------
### Haruki.py
* Discord token moved to LaunchHaruki.py
* Added cooldown error 

### LaunchHaruki.py
* Discord token is inserted here

### Admin
* Added reboot command (Linux only)
* Added shutdown command (Linux only)

### Communicate
* Replaced time.sleep with asyncio.sleep
* Added cooldown to at, dm, dma (all 10 seconds)

### Fun
* Added minigame called: Guess the Number
* Added command action, aliases=act
* Added command emote, aliases=emt
* Added json and requests modules
* Added Class guesstn as the gameplayer
* Added a requirement for tenor api key
* Added cooldown to about(10s), reddit(3s), randompicture(5s), yeetball(3s)
* Tweaked reddit command

### Help
* Added help for action, emote and gtn

### Music
* Added check_url(new) to YTDLSource 
* Tweaked from_url in YTDLSource
* Renamed check_url to check_title in YTDLSource
* Added comments and debug prints to make it easier to understand
* Added cooldown to play, loop, skip, view (all 2 seconds)
* Tweaked play command to search source using the new check_url in YTDLSource

#### check_url in YTDLSource class
* Is used to check if the searched query brings back a suitable song
* Song must be at most 30 mins long
* Handles cases where there is no results returned after searched

> Guessing simulator 2k21 ~Haruki
