from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from recognizer import proceed as p
from recognizer import proceedList as pl
import os
from PIL import Image
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def proceed():
    if 'file' not in request.files:
        return jsonify({'error':'no file uploaded'})
    img = Image.open(request.files['file'].stream)
    
    config={
        "level" : request.form.get("level",False), 
        "deaths" : request.form.get("deaths",False), 
        "mobs" : request.form.get("mobs",False), 
        "eliminations" : request.form.get("eliminations",False), 
        "xp" : request.form.get("xp",False), 
        "gold" : request.form.get("gold",False), 
        "damage" : request.form.get("damage",False), 
        "healing" : request.form.get("healing",False)
    }
    return jsonify(p(img, request.files['file'].filename, config=config))

@app.route('/table')
def index2():
    return render_template('index.html')
@app.route('/table', methods=['POST'])
def proceed2():
    if 'file' not in request.files:
        return jsonify({'error':'no file uploaded'})
    img = Image.open(request.files['file'].stream)
    
    config={
        "level" : request.form.get("level",False), 
        "deaths" : request.form.get("deaths",False), 
        "mobs" : request.form.get("mobs",False), 
        "eliminations" : request.form.get("eliminations",False), 
        "xp" : request.form.get("xp",False), 
        "gold" : request.form.get("gold",False), 
        "damage" : request.form.get("damage",False), 
        "healing" : request.form.get("healing",False)
    }
    data = pl(img, request.files['file'].filename, config=config)
    List = ['level','eliminations','deaths','mobs','gold','xp','damage','healing']
    List = [i for i in List if config[i]!=False]
    # return jsonify(data)
    return render_template('table.html', data=data, List=List)
if __name__ == "__main__":
    app.run("0.0.0.0",port=5000, debug=True)