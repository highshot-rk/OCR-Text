# Switchblade Score-Tesseract OCR
Debian 8 Server Environment\
by reyzeal (Rizal Ardhi Rahmadani)

## About Project
This is documentation of my [Freelancer project](https://www.freelancer.co.id/projects/php/Image-text-OCR-using-tesseract-26533030/details). The goal of this project is to extract all information on the scoreboard from Switchblade games using Tesseract OCR as the core technology.

## About Switchblade
Switchblade is an arena-based 5v5 vehicle action game that combines high-octane combat with an ever shifting selection of strategic choices.
https://www.switchbladegame.com/

![Example](https://github.com/reyzeal/score-tesseract/raw/master/tester/Switchblade_20200608185314.jpg)

## Instruction
1. Install core dependency
```bash
apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git libsm6
```
2. Install Tesseract-ocr
```bash
apt-get install tesseract-ocr
```
3. Install the python 3.6.11 through pyenv
```bash
curl https://pyenv.run | bash
```
4. Add this following lines to ~/.bashrc so your command line can run pyenv. You can use nano/vim or any other cli text editor.
```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
5. Restart shell using: `exec $SHELL`
6. Install python 3.6.11: `pyenv install 3.6.11`
7. Make python as global : `pyenv global 3.6.11`
8. Update the pip : `pip3 install --upgrade pip`
9. Download my source code to your specified server directory. Install git if it's not installed yet `apt-get install git`.
```bash
cd ~
git clone https://github.com/reyzeal/score-tesseract
cd score-tesseract
```
10. Create virtualenv to make python environment for this project
```bash
python3 -m virtualenv venv
```
11. Activate the environment
```bash
source venv/bin/activate
```
12. Install all requirements library using requirements.txt
```bash
pip3 install -r requirements.txt
```
13. you can try to run it:
```bash
venv/bin/gunicorn -b 127.0.0.1:5000 app:app
```
![Image of server](https://github.com/reyzeal/score-tesseract/raw/master/server/first.png)

14. Done, if you prefer to run it as server service, stop the execution and do the following steps
    below.

## Deploy as Systemd Service

1. You can use the template file that I’ve put in the folder server > score.service. If you know
    how to use vim / nano, you can directly create new file in
    **/etc/systemd/system/score.service** using this command : “sudo nano
    **/etc/systemd/system/score.service** ”.
```  
[Unit]
Description=Reyzeal Score Tesseract Gunicorn daemon
After=network.target

[Service]
User= ubuntu
Group= ubuntu
WorkingDirectory=/home/ubuntu/score-tesseract
ExecStart=/home/ubuntu/score-tesseract/ venv/bin/gunicorn -w 3 -b
127.0.0.1:5000 app:app

[Install]
WantedBy=multi-user.target
```
2. Change all variables, focus on the red mark:
```bash
User= **<your username>**
Group= **<your username>**
WorkingDirectory= **/path/to/project**
ExecStart= **/path/to/project/**venv/bin/gunicorn -w 3 -b 127.0.0.1:5000 app:app
```
3. Save the file on **/etc/systemd/system/score.service.** Just save and close it if you already
    using vim / nano directly.
4. Enable and start:
```bash
    sudo systemctl enable score.service
    sudo systemctl start score.service
```
5. Check the status, it must be look like this:
```bash
sudo systemctl status score.service
```
![Image of server](https://github.com/reyzeal/score-tesseract/raw/master/server/second.png)

## Apache2 Configuration

If you want to make proxy through apache2 (make it public), you can add this following lines to
your current site config file.
```bash
ProxyPreserveHost On
ProxyPass / [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
ProxyPassReverse / [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
```
**Note : Make sure you have these mod enabled:**
```bash
sudo a2enmod proxy
sudo a2enmod proxy_http
```
## Preview
### Input File
![Example](https://github.com/reyzeal/score-tesseract/raw/master/tester/Switchblade_20200608185314.jpg)
### Server Page
![Server](https://github.com/reyzeal/score-tesseract/raw/master/server/example.png)
### Json Result
```json
{
   "data":{
      "LIONS":{
         "Grandpots69":{
            "damage":26969,
            "deaths":11,
            "eliminations":0,
            "gold":6514,
            "healing":1734,
            "level":9,
            "mobs":70,
            "xp":16253
         },
         "HulkSmash122787":{
            "damage":19232,
            "deaths":13,
            "eliminations":5,
            "gold":5555,
            "healing":5,
            "level":8,
            "mobs":65,
            "xp":12455
         },
         "True_Killer221":{
            "damage":21497,
            "deaths":7,
            "eliminations":13,
            "gold":5403,
            "healing":8275,
            "level":9,
            "mobs":58,
            "xp":17541
         },
         "loco__kevin0707":{
            "damage":23814,
            "deaths":9,
            "eliminations":6,
            "gold":5817,
            "healing":42,
            "level":8,
            "mobs":64,
            "xp":12951
         },
         "quangzone":{
            "damage":51585,
            "deaths":3,
            "eliminations":22,
            "gold":8670,
            "healing":5,
            "level":10,
            "mobs":85,
            "xp":21891
         }
      },
      "SHARKS":{
         "Dragon__Webs":{
            "damage":35494,
            "deaths":10,
            "eliminations":15,
            "gold":6992,
            "healing":0,
            "level":9,
            "mobs":78,
            "xp":16839
         },
         "JDMlinkup":{
            "damage":13635,
            "deaths":7,
            "eliminations":11,
            "gold":5176,
            "healing":5,
            "level":8,
            "mobs":28,
            "xp":11070
         },
         "Mathias-BY":{
            "damage":6977,
            "deaths":15,
            "eliminations":4,
            "gold":4815,
            "healing":0,
            "level":8,
            "mobs":56,
            "xp":10114
         },
         "mode-87-h":{
            "damage":49704,
            "deaths":3,
            "eliminations":28,
            "gold":9258,
            "healing":0,
            "level":10,
            "mobs":119,
            "xp":22814
         },
         "sophie-ann":{
            "damage":22977,
            "deaths":1,
            "eliminations":16,
            "gold":7633,
            "healing":14324,
            "level":10,
            "mobs":63,
            "xp":23954
         }
      }
   },
   "filename":"Switchblade_20200608185314.jpg",
   "request":{
      "damage":"on",
      "deaths":"on",
      "eliminations":"on",
      "gold":"on",
      "healing":"on",
      "level":"on",
      "mobs":"on",
      "xp":"on"
   },
   "time":"26.051788091659546 seconds"
}
```
