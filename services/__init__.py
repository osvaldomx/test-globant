from flask import Flask
from flask_cors import CORS

def create_app(config=None) -> Flask:
    '''Creates Flask App

    Args:
    -----
    config (): Configuration for app

    Returns:
    --------
    app (Flask): Flask App
    '''

    app = Flask(__name__,
                template_folder="../templates",
                instance_relative_config=True)
    
    app.config.from_object(config)

    CORS(app)

    #app.register_blueprint()

    return app