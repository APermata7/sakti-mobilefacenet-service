import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from a2wsgi import ASGIMiddleware
from app.main import app

application = ASGIMiddleware(app)