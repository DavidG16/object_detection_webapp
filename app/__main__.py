from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app():
    app = Flask(__name__)

    from app.object_detection.routes import object_detection_blueprint
    app.register_blueprint(object_detection_blueprint)

    socketio.init_app(app)
    return app


daemon_app = create_app()


if __name__ == "__main__":
    daemon_app.run( port=8000)

