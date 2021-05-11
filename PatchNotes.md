# Patch Notes for Haruki bot.

5/8/2021 HarukiV1.2
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

> OWO whats this? - Haruki

5/9/2021 HarukiV1.3
--------------------------------------
* Modified check_url in Class YTDLSource to only extract data from search
* Modified view command to only allow up to first 5 songs to be searched to prevent overloading
* Added global variable loopsong
* Modified play command to use allow looping
* Added new loop command

### Minor changes
* Global nowplaying set to say No song playing when initialized
* Added help loop to help command

> Time to listen to the same music again! - Haruki
