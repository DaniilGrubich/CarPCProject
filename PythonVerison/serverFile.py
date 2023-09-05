import time
import random
import math

from flask import Flask, render_template
from flask_socketio import SocketIO

import cv2
import base64
import numpy as np

from threading import Thread, Event
from datetime import datetime, timedelta
import MySpotify as sp
import OBDMediator as obdM


def current_time():
    return datetime.now().strftime("%I:%M%p")

def ddm_to_ddd(ddm):
    degrees, minutes = divmod(ddm, 100)
    return degrees + minutes/60

def getSimulatedValue(range_start, range_end, time_offset):
    mid = (range_end - range_start) / 2.0 + range_start
    amplitude = (range_end - range_start) / 2.0
    return mid + amplitude * math.sin(time.time() + time_offset)



app = Flask("", template_folder='FrontEnd', static_folder='FrontEnd')
socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()

timeString = ''

cap = cv2.VideoCapture(1)

def createAndStartFlask():
    socketio.run(app, allow_unsafe_werkzeug=True, debug=False)



def mainClientThread():
    global timeString, cap
    print('Main Client Thread Started')





    firstRun = True
    lineCounter = 0
    time.sleep(3)
    song_start_time = datetime.now()
    gps_start_time = datetime.now()
    carData_start_time = datetime.now()
    while not thread_stop_event.isSet():

        # if((timeString != current_time()) or firstRun):
        #     timeString = current_time()
        #     print('Time sent')
        #     socketio.emit('setClock', timeString)

        # if datetime.now() - song_start_time >= timedelta(seconds=3):
        #     sp.updateTrackJSON()
        #     songName = sp.songName
        #     artistName = sp.artist_name
        #     picLink = sp.albumPicLink
        #     progreess = sp.currentProgress
        #     totalTime = sp.totalDuration
        #     songData = str(picLink) + "|" + str(songName) + "|" + artistName + "|" + str(progreess) + "|" + str(totalTime) + "|" + str(sp.isTrackUpdated())
        #     socketio.emit('songData', songData)

        #     song_start_time = datetime.now()  # reset the start time

        # if datetime.now() - gps_start_time >= timedelta(seconds=1):
        #     line = data[lineCounter]
        #     components = line.split()
        #     _, lat_str, long_str, speed = components
        #     lat, long = ddm_to_ddd(float(lat_str)), -ddm_to_ddd(float(long_str))
        #     print(f"{long}, {lat}, {speed}")
        #     lineCounter=lineCounter+2

        #     socketio.emit('newGPSPoint', str(long) + "|" + str(lat) + "|" + str(speed) + "|" + str(.5))

        #     gps_start_time = datetime.now()  # reset the start time

        # if datetime.now() - carData_start_time >= timedelta(seconds=.032):
            
        socketio.emit('carParameters', str(obdM.carParameters))

            # success, frame = cap.read()
            # if success:
            #     ret, buffer = cv2.imencode('.jpg', frame)
            #     frame = base64.b64encode(buffer).decode('utf-8')
            #     # cv2.imshow('Frame', frame)
            #     socketio.emit('image', frame)

            
            # carData_start_time = datetime.now()  # reset the start time

        


        socketio.sleep(1/60)

        firstRun = False

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connected():
    global thread
    print('hello')

    if not thread.is_alive():
        print("Starting Thread")
        thread = socketio.start_background_task(mainClientThread)


@socketio.on('disconnect')
def disconnected():
    global thread_stop_event
    thread_stop_event.set()