from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'something to guess'

from app import view
