from flask import Flask, request

def create_app():
    app = Flask(__name__)
    return app
    
    @app.route("/")
    def index():
        return "claudos"