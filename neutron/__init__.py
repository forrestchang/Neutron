from flask import Flask
from .config import config
import os


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    return app

app = create_app(os.getenv('NEUTRON_CONFIG_NAME') or 'default')
from . import view
