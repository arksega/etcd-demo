#!/bin/python3
from flask import render_template
from flask import Flask
import urllib.request
import json

app = Flask(__name__)

def imleader():
    with urllib.request.urlopen('http://localhost:2379/v2/stats/self') as f:
        data = json.loads(f.read().decode('utf-8'))
    return data['state'] == 'StateLeader'

@app.route('/')
def index():
    return render_template('index.html', imleader=imleader())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# vim: ts=4 sw=4 et
