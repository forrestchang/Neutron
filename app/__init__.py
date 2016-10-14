# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'not to tell you'

from app import view

