from flask import Flask

from app.object_detection.routes import object_detection_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(object_detection_blueprint)
    return app


def _main():
    daemon_app = create_app()
    daemon_app.run(debug=True)

daemon_app = create_app()

if __name__ == "__main__":
    _main()

