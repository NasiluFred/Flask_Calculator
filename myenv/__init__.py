import os
from flask import Flask
from .config import Config

#Inject Flask magic
app = Flask(__name__)

#load configurations
app.config.from_object( config)

# import routing to render the pages

from myflaskapp import views
