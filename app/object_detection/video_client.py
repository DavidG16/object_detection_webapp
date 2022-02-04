import cv2
from imageai import Detection

import numpy as np
import socket
import sys
import pickle
import struct

MODEL_PATH = f"./model/yolo.h5"
print(MODEL_PATH)

# cam = cv2.VideoCapture(0)
# yolo = Detection.ObjectDetection()
# yolo.setModelTypeAsYOLOv3()
# yolo.setModelPath(MODEL_PATH)
# yolo.loadModel()
#
# clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientsocket.connect(('localhost', 8089))
#
#
# def get_video_preds(frame):
#     frame, preds = yolo.detectCustomObjectsFromImage(input_image=frame,
#                                                      custom_objects=None, input_type="array",
#                                                      output_type="array",
#                                                      minimum_percentage_probability=70,
#                                                      display_percentage_probability=False,
#                                                      display_object_name=True)
#     return  frame, preds
#
def gen_frames_client():
    pass
#     while True:
#         success, frame = cam.read()  # read the camera frame
#         if not success:
#             break
#         else:
#             #frame, preds = get_video_preds(frame)
#             #ret, buffer = cv2.imencode('.jpg', frame)
#             #frame = buffer.tobytes()
#             #yield (b'--frame\r\n 'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#             data = pickle.dumps(frame)
#             message_size = struct.pack("L", len(data))
#             clientsocket.sendall(message_size + data)


