from flask import Blueprint, render_template, Response
from app.object_detection.video import gen_frames

object_detection_blueprint = Blueprint(
    "object_detection_blueprint", __name__, template_folder="templates")


@object_detection_blueprint.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")



@object_detection_blueprint.route("/camera", methods=["GET", "POST"])
def activate_camera():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


