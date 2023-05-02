import os

from flask import render_template

from config import DevelopConfig

from services import create_app

app = create_app(DevelopConfig)

TITLE = "Test Globant >"

@app.route('/')
def index():
    return render_template('index.html',
                           title=TITLE), 200

if __name__ == '__main__':
    app.run()