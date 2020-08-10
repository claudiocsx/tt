from flask import request, render_template
from flask import Blueprint

bp = Blueprint("site",__name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/login")    
def login():
    return render_template("login.html")

@bp.route("/base")
def base():
    return render_template("base.html")        