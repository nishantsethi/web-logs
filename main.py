from time import sleep
from flask import Flask, render_template
from math import sqrt
from pathlib import Path
import json


app = Flask(__name__)


# class WebLogs:
#     def __init__(self, json_path: str):
#         self.json_path = json_path
#         current_working_dir = str(Path.cwd())


json_path = "data.json"
data_json = json.load(open(json_path))

logs_list = data_json['logs']    #List with all the logs info in each dict [{}{}]
print(logs_list)

tom = 1
for i in logs_list:
    i['ID'] = str(tom) + 'p'
    tom = tom + 1

print(logs_list)
no_of_logs = len(logs_list)

log_id = '2p'

# Run this when a person calls a function in their program
@app.route('/')
def index():
    # render the template (below) that will use JavaScript to read the stream
    global log_id
    log_id = '1p'
    return render_template('index.html', logs_list = logs_list, log_id = log_id)




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