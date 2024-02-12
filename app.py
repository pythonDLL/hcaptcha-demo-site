from flask import Flask, render_template
import logging, datetime, os
from colorama import Fore

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True
os.system("cls")
os.system("title listening at 127.0.0.1:5000")
os.system("start http://127.0.0.1:5000")

def log_msg(msg):
    print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {msg}')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)