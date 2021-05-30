# Switchblade Score-Tesseract OCR
CLI Local Environment
by reyzeal (Rizal Ardhi Rahmadani)

## About Project
This is documentation of my [Freelancer project](https://www.freelancer.co.id/projects/php/Image-text-OCR-using-tesseract-26533030/details). The goal of this project is to extract all information on the scoreboard from Switchblade games using Tesseract OCR as the core technology.

## About Switchblade
Switchblade is an arena-based 5v5 vehicle action game that combines high-octane combat with an ever shifting selection of strategic choices.\
https://www.switchbladegame.com/

## Requirements / Preparation
### Python 3 Installation
Python >= 3.6 is working fine
#### MacOS
Using Homebrew : `brew install python3`\
or\
Using installer, select Stable Releases, download it and install : https://www.python.org/downloads/mac-osx/ \
or\
Follow this instruction : https://docs.python-guide.org/starting/install3/osx/

#### Ubuntu
Using apt-get : `sudo apt-get install python3 python3-pip`
#### Windows
Download and Install : https://www.python.org/downloads/windows/ \
Make sure you checked the option for add Python3 to your computer Environment.

#### Testing Python3
Make sure your Python 3 is installed properly:
1. Open your command line
2. Type `python3`
3. It must be look like this:\
 
![Image](https://github.com/reyzeal/score-tesseract/raw/master/docs/python3.png)

### Tesseract-OCR Installation
#### MacOS
Using MacPorts : `sudo port install tesseract`\
or\
Using Brew : `brew install tesseract`
#### Ubuntu
Using apt-get : `sudo apt-get install tesseract-ocr`
#### Windows
Follow this instruction, download link provided here : https://github.com/UB-Mannheim/tesseract/wiki

#### Testing Tesseract
Make sure your tesseract is installed properly:
1. Open your command line
2. Type `tesseract -v`
3. It must be look like this:\
 
![Image](https://github.com/reyzeal/score-tesseract/raw/master/docs/tesseract.png)

### Mysql Connector
Mysql Connector is required to connect python to mysql server. You must know which mysql server that you're using in this project.\
Check it here https://dev.mysql.com/downloads/connector/python/
Connector/Python Version|MySQL Server Versions|Supported Python Versions
------------------------|---------------------|-------------------------
8.0|8.0, 5.7, 5.6, 5.5|3.6, 3.5, 3.4, 2.7
2.2|5.7, 5.6, 5.5|3.5, 3.4, 2.7
2.1|5.7, 5.6, 5.5|3.5, 3.4, 2.7, 2.6
2.0|5.7, 5.6, 5.5|3.5, 3.4, 2.7, 2.6
1.2|5.7, 5.6, 5.5 (5.1, 5.0, 4.1)|3.4, 3.3, 3.2, 3.1, 2.7, 2.6
## Instruction
1. Download this project using git or download zip [here](https://github.com/reyzeal/score-tesseract/archive/master.zip)
2. Unzip the file and open the project's folder
3. Rename `.env.example` to `.env`
4. Edit the env file based on your mysql server credentials
5. Install requirements: `pip3 install -r requirements.txt`
6. Run the cli.py : `python3 cli.py Folder`

## CLI Commands Manual
```bash
usage: cli.py [-h] [-a [ALL]] [-l [LEVEL]] [-e [ELIMINATIONS]] [-t [DEATHS]] [-m [MOBS]] [-g [GOLD]] [-x [XP]] [-d [DAMAGE]][-n [HEALING]]
```
### Scan all files in the folder but only to get the username
```bash
    python3 cli.py PATH_TO_FOLDER
```
### Scan all files in the folder and get all information [level, deaths, etc]
```bash
    python3 cli.py PATH_TO_FOLDER -a
```
### Scan all files in the folder but only get level
```bash
    python3 cli.py PATH_TO_FOLDER -l
```
### The other options
```bash
    -a  : all details
    -l  : level
    -e  : eliminations
    -m  : mobs
    -t  : deaths
    -g  : gold
    -x  : xp
    -d  : damage
    -n  : healing
    -r  : replace mode, overwrite all data in database. Just in case that if you need to rescan information from partial detail to all full detail.
```

### Example
```bash
    python3 cli.py tester -a
```

## Mysql Table Schema
This script will create a table named `scoreboard` with 3 fields as primary keys, known as composite key. There are Filename, Team, and Username.
Name|Datatype
----|--------
filename|varchar(50)
team|varchar(20)
username|varchar(20)
level|INT NULL
deaths|INT NULL
mobs|INT NULL
eliminations|INT NULL
xp|INT NULL
gold|INT NULL
damage|INT NULL
healing|INT NULL

## Result
![img](https://github.com/reyzeal/score-tesseract/raw/master/docs/first.png)
![img](https://github.com/reyzeal/score-tesseract/raw/master/docs/second.png)