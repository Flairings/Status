# Status
Advanced discord status

Using this script will require a few things, 5 minutes, a discord account, a brain, and python & pip installed on your computer.
First open a commandline and type "pip install pypresence", "pip install colorama"
Second go to https://discord.com/developers/applications and click "New Application"
give your application a name you would like to display at the top of the status for instance "my balls itch"
once the application is created go to the tab named "Rich Presence" and add an image of your choosing and remember the name.
(NOTE: images can take up to 30 minutes to upload, it might not show it on the page for a little while)
Third download the files from the git repository, copy them to a folder, and open the file "config.json"
go the the discord developer page and click the tab named "OAuth2" and copy the "CLIENT ID" into the "client.id" field in the "config.json"
change the "large_image" field to the name of the image you uploaded and change the other configuration fields to your choosing
run the "presence.py" script and wait 15 seconds for your discord status to enable.


P.S. if you find a way to get the same thing to work on a vps please reply on the issues tab
