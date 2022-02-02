from flask import Blueprint, render_template

object_detection_blueprint = Blueprint(
    "object_detection_blueprint", __name__, template_folder="templates")


@object_detection_blueprint.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
