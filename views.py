from flask import Flask, request , render_template

def init_app(app: Flask):

    @app.route("/")
    def index():
        return render_template("index.html")


    @app.route("/login")    
    def login():
        return render_template("login.html")