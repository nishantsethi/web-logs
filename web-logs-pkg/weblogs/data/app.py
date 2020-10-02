from time import sleep
from flask import Flask, render_template, request
from math import sqrt
from pathlib import Path
import json
import os

app = Flask(__name__)


path_json = open("json_path.txt", "r")

json_path = path_json.read()
data_json = json.load(open(json_path))

logs_list = data_json['logs']    #List with all the logs info in each dict [{}{}]
print(logs_list)

tom = 1
for i in logs_list:
    i['ID'] = str(tom) + 'p'
    tom = tom + 1

print(logs_list)
no_of_logs = len(logs_list)

log_id = '1p'


# Run this when a person calls a function in their program
@app.route('/', methods=['GET', 'POST'])
def index():
    log_name = logs_list[0]['logName']
    # render the template (below) that will use JavaScript to read the stream
    if request.method == 'POST':
        text = request.form['text']
        global log_id
        log_id = text
        print("yolyo " + log_id)
        selected_dic =  next(item for item in logs_list if item["ID"] == log_id)
        log_name = selected_dic['logName']
    return render_template('index.html', logs_list = logs_list, log_id = log_id, log_name = log_name)




@app.route('/' + str(log_id))
def stream():
    def generate():
        selected_dic = next(item for item in logs_list if item["ID"] == log_id)
        log_path = selected_dic['logPath']
        print(log_id)
        with open(log_path) as f:
            while True:
                yield f.read()
                sleep(1)

    return app.response_class(generate(), mimetype='text/plain')

app.run()