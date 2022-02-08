from flask import Flask
from flask_socketio import SocketIO, emit


from app.object_detection.video import get_video_preds

socketio = SocketIO()


def create_app():
    app = Flask(__name__)

    from app.object_detection.routes import object_detection_blueprint
    app.register_blueprint(object_detection_blueprint)

    socketio.init_app(app)
    return app


daemon_app = create_app()


@socketio.on('image')
def image(data_image):
    sbuf = StringIO()
    print(sbuf)
    sbuf.write(data_image)

    # decode and convert into image
    b = io.BytesIO(base64.b64decode(data_image))
    pimg = Image.open(b)

    ## converting RGB to BGR, as opencv standards
    frame = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

    # Process the image frame
    frame = imutils.resize(frame, width=700)
    frame = cv2.flip(frame, 1)
    #frame, preds = get_video_preds(frame)
    imgencode = cv2.imencode('.jpg', frame)[1]
    print(imgencode)

    # base64 encode
    stringData = base64.b64encode(imgencode).decode('utf-8')
    b64_src = 'data:image/jpg;base64,'
    stringData = b64_src + stringData

    # emit the frame back
    emit('response_back', stringData)


if __name__ == "__main__":
    daemon_app.run( port=5000)

