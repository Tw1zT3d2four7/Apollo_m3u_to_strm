I created this because I couldn't find any tools that would work with Apollo's M3U feeds. (apollogroup.tv)
PR's welcome as there are probably things that could be done a little more sanely.
(Especially error handling) 

I'm using Jellyfin and wrote this script so that it can be placed in the root of my media folder.  I then use separate sub-folders 
for strm file storage along side my media library.  This is why I have a subfolder variable declared and CD into it when generating
the folder structure and strm files. 

I truncate and re-write URLs to the strm files that already exist so that their last modified times are updated. 
The script then does a sweep to clean up any strm files that were not updated because they are no longer in the playlist, and any empty folders that are left behind as a result. 

You'll need to modify the script to match your folder structure along with the commands that change directories before files are created.
You'll also need to create/populate 2 text files that house your M3U URLs. There are currently 24 TV VOD URLs active, and 1 for movies.
In the TV file I just added 30 URLs for future expansion since the script checks to see if they exist before consuming them. 

This does not scrape sports VOD content but it is easy enough to copy the movies section to create a sports one. 
I only wanted items in my library that have full metadata. 

I would recommend starting with Movies and 1 TV URL, get those added to your library and then add 1 URL per day to be processed. 
As of writing this, their VOD library contains 12,025 movies and 2154 TV series totaling 115,721 episodes. 

#Caution, on my system this script seems to consume around 400MB of ram while running due to the size of the VOD library. 

You're going to need to install a few modules for the script to run.  Assuming you're on Ubuntu, install pip first, then:

pip install m3u-parser

pip install pathvalidate

pip install requests

pip install numpy

Download getstreams.py to a folder where you're going to create your library of .strm files. 

Create a subfolder named TV and another named Movies & one named LiveTv

Create a file in the same folder as getstreams.py named movie_vod_urls.txt that contains the following line:
https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/movies

Create a file in the same folder as getstreams.py named livetv_vod_urls.txt that contains the following line:
https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/livetv

Create a file in the same folder as getstreams.py named tv_vod_urls.txt that contains the following lines: 
https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/1
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/2
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/3
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/4
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/5
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/6
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/7
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/8
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/9
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/10
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/11
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/12
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/13
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/14
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/15
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/16
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/17
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/18
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/19
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/20
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/21
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/22
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/23
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/24
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/25
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/26
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/27
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/28
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/29
#https://tvnow.best/api/list/YOUR_USERNAME/YOUR_PASSWORD/m3u8/tvshows/30

You may use the preconfigured setup in the Apollo_m3u_2_strm.rar just unrar
and place the folder in the root of C:\ DRIVE AND PLACE THE .VBS IN THE shell:startup folder.
Access it with the windows key plus R key to being up the run tab. then type shell:startup and
hit enter. It will open the folder and place the .vbs in it. upon restart of the PC the program 
will run every twelve hr's in the background --noconsole. or you may follow the directions below.

Run the script by calling "python3 getstreams.py" 
Or, create a shebang line (#!/usr/bin/python3) at the start of your file, and then set is as executable and run it directly. 

Once it has run successfully you should see a bunch of files with .strm extension on disk.  Proceed to uncommend your TV vod urls in the text file and run the script again to add more shows to your library.  Use caution, when I ran this against all VOD items at once it took over 8 hours for jellyfin to add the content to my library and scrape the metadata. As of 5-18-23, Apollo is up to 27 M3u URLs for TV Shows but their documentation says 14 :)
