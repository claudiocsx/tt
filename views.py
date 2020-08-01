from flask import Flask, request

def init_app(app: Flask):

    @app.route("/")
    def index():
        return "claudio codigo"