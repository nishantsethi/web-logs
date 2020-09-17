from time import sleep
from flask import Flask, render_template
from math import sqrt

app = Flask(__name__)

@app.route('/')
def index():
    # render the template (below) that will use JavaScript to read the stream
    return render_template('index.html')

@app.route('/stream_sqrt')
def stream():
    def generate():
        with open('example.log') as f:
            while True:
                yield f.read()
                sleep(1)

    return app.response_class(generate(), mimetype='text/plain')

app.run()