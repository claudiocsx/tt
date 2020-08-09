from flask import Flask
from ext import views

def create_app():
    
    
    app = Flask(__name__)
    views.init_app(app)

    return app
    
