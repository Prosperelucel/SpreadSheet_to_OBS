# SpreadSheet_to_OBSv1

### Requirement :
- Windows 10
- [OBS Studio](https://obsproject.com/)
- [obs-websocket](https://github.com/Palakis/obs-websocket) from [@LePalakis](https://twitter.com/LePalakis)

### Setup : 
. [Follow step and create credentials in Google API Console](http://gspread.readthedocs.org/en/latest/oauth2.html)
. [Step by step screenshot](https://docs.google.com/document/d/1qJDR2kuIb8OVXNV4hnf2J3JbzXiie4aapHx2EnG3BQc/)
. Download the .json file, rename it service_account.json and copy into the script folder.

### Edit Config: 
Open config.ini
```
[DEFAULT]
url = https://docs.google.com/spreadsheets/d/url123456
timer_refresh = 5
max_row = 2
obswebsocket_ip = localhost
obswebsocket_port = 4444
obswebsocket_pw = password
```
. url : Replace URL with a spreadsheet host in your own Google Drive (currently doesn't work on a spreadsheet not owned by your account)
. timer_refresh : number of seconds beetween refresh (don't put a low value or you will be blocked by Google API)
. max_row : number of row/text fields sends to OBS
. obswebsocket_ip = IP/Localhost
. obswebsocket_port = Port
. obswebsocket_pw = Password 

## Usage :
Launch OBS
Launch Script or .exe
Edit the name of your text source in OBS to work properly with the script, must be 1_TXT / 2_TXT etc... (don't edit text name in the script)
Click Start

## Example : 
https://youtu.be/92Wwn0MfFHc
![](https://youtu.be/92Wwn0MfFHc)

## Follow me :
- [@Prosperelucel](https://twitter.com/ProspereLucel)
- [Prospere on Twitch](https://twitch.tv/prospere)
- [My Discord](https://discord.gg/ac2xDrJ)
- [Buy me a cofee](https://www.paypal.com/donate?hosted_button_id=UB9U2N2JKRA3A)

