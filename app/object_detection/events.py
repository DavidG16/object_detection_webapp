from flask_socketio import  emit
from io import StringIO
import io
import base64
from PIL import Image
import cv2
import numpy as np
from app.object_detection.video import get_video_preds


from ..__main__ import socketio



@socketio.on('image')
def image(data_image):
    sbuf = StringIO()
    sbuf.write(data_image)
    print(sbuf)

    # decode and convert into image
    b = io.BytesIO(base64.b64decode(data_image))
    pimg = Image.open(b)

    ## converting RGB to BGR, as opencv standards
    frame = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

    # get predictions
    frame, preds = get_video_preds(frame)
    print(preds)
    imgencode = cv2.imencode('.jpg', frame)[1]

    # base64 encode
    stringData = base64.b64encode(imgencode).decode('utf-8')
    b64_src = 'data:image/jpg;base64,'
    stringData = b64_src + stringData
    # emit the frame back
    emit('response_back', stringData)
