from flask import Blueprint, render_template

bp = Blueprint("index_views", __name__, template_folder="templates")

@bp.route("/")
def index():
    return render_template("index.html")
