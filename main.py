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
no_of_logs = len(logs_list)


# Run this when a person calls a function in their program
@app.route('/')
def index():
    # render the template (below) that will use JavaScript to read the stream
    return render_template('index.html', logs_list = logs_list)

@app.route('/stream_sqrt')
def stream():
    def generate():
        with open('example.log') as f:
            while True:
                yield f.read()
                sleep(1)

    return app.response_class(generate(), mimetype='text/plain')

app.run()