import cv2
import os
import sys
import argparse
from recognizer import proceed
import mysql.connector
from mysql.connector import Error
from tqdm import tqdm
from dotenv import load_dotenv
import logging
from datetime import datetime
LOG_FILENAME = 'event.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
load_dotenv()

# Create the parser
parser = argparse.ArgumentParser(description='Execute OCR from the list images of a folder')

# Add the arguments
parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list of images')
parser.add_argument('-a','--all', action='store', nargs='?', default=False, dest='all')
parser.add_argument('-l','--level', action='store', nargs='?', default=False, dest='level')
parser.add_argument('-e','--eliminations', action='store', nargs='?', default=False, dest='eliminations')
parser.add_argument('-t','--deaths', action='store', nargs='?', default=False, dest='deaths')
parser.add_argument('-m','--mobs', action='store', nargs='?', default=False, dest='mobs')
parser.add_argument('-g','--gold', action='store', nargs='?', default=False, dest='gold')
parser.add_argument('-x','--xp', action='store', nargs='?', default=False, dest='xp')
parser.add_argument('-d','--damage', action='store', nargs='?', default=False, dest='damage')
parser.add_argument('-n','--healing', action='store', nargs='?', default=False, dest='healing')
parser.add_argument('-r','--replace', action='store', nargs='?', default=False, dest='replace')

# Execute the parse_args() method
args = parser.parse_args()

input_path = args.Path
args = parser.parse_args()
if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()
config = {
    "level" : args.level,
    "deaths" : args.deaths,
    "mobs" : args.mobs,
    "eliminations" : args.eliminations,
    "xp" : args.xp, 
    "gold" : args.gold,
    "damage" : args.damage,
    "healing" : args.healing,
}
logging.info("Start New CLI :"+datetime.now().isoformat())
total = 10
if args.all != False:
    logging.info("mode all")
    for i in config.keys():
        config[i] = True
        if config[i]:
            total += 10
else:
    logging.info("mode partial")
    for i in config.keys():
        config[i] = config[i] != False
        logging.debug(f"mode {i}:{config[i]}")
        if config[i]:
            total += 10

try:
    connection = mysql.connector.connect(host=os.getenv('hostname'),
                                         database=os.getenv('database'),
                                         user=os.getenv('username'),
                                         password=os.getenv('password'))
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor(prepared=True)
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record[0])
        cursor.execute("""create table if not exists scoreboard(
            filename VARCHAR(50),
            team VARCHAR(20),
            username VARCHAR(20),
            level INT NULL,
            deaths INT NULL,
            mobs INT NULL,
            eliminations INT NULL,
            xp INT NULL,
            gold INT NULL,
            damage INT NULL,
            healing INT NULL,
            primary key (filename, team, username)
        );""")
        cursor.close()
except Error as e:
    print("Error while connecting to MySQL", e)
    logging.error(f"Error while connecting to MySQL {e}")

cursor = connection.cursor(prepared=True)
change = False
tqdm_list = ["Team 1 Name","Team 2 Name"]
for i in range(2):
    for j in range(10):
        tqdm_list.append(f"Username slot {j+1}")
        for k in config.keys():
            if config[k]:
                tqdm_list.append(f"{k} slot {j+1}")
for filename in os.listdir(input_path):
    
    try:
        img_name = os.path.basename(filename)
        img = cv2.imread(os.path.join(input_path,filename))
        
        cursor.execute("select count(*) from scoreboard where filename=%s;",(filename,))
        x = cursor.fetchone()[0]
        
        if x == 0 or (x>0 and args.replace != False):
            change = True
            logging.info(f'{datetime.now().isoformat()} processing {filename}')
            print(f'Processing {filename}')
            t = tqdm(total=total,unit='OCR')
            
            data = proceed(img, img_name, config, tqdm=t, tqdm_list=tqdm_list)
            for team in data['data'].keys():
                for username in data['data'][team].keys():
                    tuple_prepared = (
                    filename, 
                    team,
                    username,
                    data['data'][team][username].get('level',None), 
                    data['data'][team][username].get('deaths',None), 
                    data['data'][team][username].get('mobs',None),
                    data['data'][team][username].get('eliminations',None),
                    data['data'][team][username].get('xp',None),
                    data['data'][team][username].get('gold',None),
                    data['data'][team][username].get('damage',None),
                    data['data'][team][username].get('healing',None),
                    data['data'][team][username].get('level',None), 
                    data['data'][team][username].get('deaths',None), 
                    data['data'][team][username].get('mobs',None),
                    data['data'][team][username].get('eliminations',None),
                    data['data'][team][username].get('xp',None),
                    data['data'][team][username].get('gold',None),
                    data['data'][team][username].get('damage',None),
                    data['data'][team][username].get('healing',None)
                    )
                    cursor.execute("""INSERT INTO scoreboard(filename,team,username,level,deaths,mobs,eliminations,xp,gold,damage,healing) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE level=%s, deaths=%s, mobs=%s,eliminations=%s,xp=%s,gold=%s,damage=%s,healing=%s""", tuple_prepared)
            padding = " ".join(["" for i in range(21)])
            t.set_description("DONE"+padding)
            t.close()
            connection.commit()
            logging.info(f'done {filename}')
        else:
            print(f'Skip file {filename}... ')
            logging.info(f'Skip file {filename}')
    except Error as e:
        cursor = connection.cursor(prepared=True)
        logging.error(f"Error while scanning file {filename}, {e}")
    except Exception as e:
        logging.error(f"Error , {e}")
