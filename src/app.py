from flask import Flask, render_template, url_for

from config import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def pageNotFound(eror):
    return render_template('404.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(host='0.0.0.0')