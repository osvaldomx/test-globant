import os

from config import DevelopConfig

from services import create_app

app = create_app(DevelopConfig)

TITLE = "Test Globant >"

@app.route('/')
def index():
    return TITLE

if __name__ == '__main__':
    app.run()