from flask import Flask, render_template
from flask_socketio import SocketIO
import cv2
import base64
from threading import Thread, Event

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = Flask(__name__, template_folder='FrontEnd', static_folder='FrontEnd')
socketio = SocketIO(app)
URL = "http://192.168.137.13"
cap = cv2.VideoCapture(URL + ":81/stream")  # 0 if you want to use the default camera
thread = Thread()
thread_stop_event = Event()

@app.route('/')
def index():
    return render_template('index.html')

def gen_frames():
    while not thread_stop_event.isSet():
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = base64.b64encode(buffer).decode('utf-8')
            socketio.emit('image', frame)
            socketio.sleep(0.001)  # Adjust this to your liking.

@socketio.on('connect')
def connected():
    global thread
    if not thread.is_alive():
        print("Starting Thread")
        thread = socketio.start_background_task(gen_frames)

@socketio.on('disconnect')
def disconnected():
    global thread_stop_event
    thread_stop_event.set()

def run_qt_app():
    app = QApplication([])
    view = QWebEngineView()

    # Set the window dimensions.
    view.setFixedSize(1024, 600)  # Replace these values with your desired dimensions.

    # Set the window flags to remove the title bar.
    view.setWindowFlags(Qt.FramelessWindowHint)

    url = QUrl("http://127.0.0.1:5000")

    view.setUrl(url)
    view.show()

    # Enter the application's main loop
    app.exec_()

if __name__ == '__main__':
    qt_thread = Thread(target=run_qt_app)
    qt_thread.start()

    socketio.run(app, allow_unsafe_werkzeug=True)
