import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from asgiref.wsgi import WsgiToAsgi
from app.main import app

application = WsgiToAsgi(app)