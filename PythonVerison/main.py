import cv2
import base64

import inbededBrowerWindow as brw
import serverFile as srf
import MySpotify as sp
import OBDMediator as obdM

import time


if __name__ == '__main__':
    print('Main function starting the server')

    #  # Open Spotify
    # sp.openSpotify()

     # Launch browser (commented out for now)
    # brw.launchBrowser()
    
    obdM.startOBDColletor()

     # Create and start Flask server
    srf.createAndStartFlask()






# URL = "http://192.168.137.13"
# cap = cv2.VideoCapture(URL + ":81/stream")  # 0 if you want to use the default camera















# success, frame = cap.read()
        # if not success:
        #     break
        # else:
        #     ret, buffer = cv2.imencode('.jpg', frame)
        #     frame = base64.b64encode(buffer).decode('utf-8')
        #     socketio.emit('image', frame)
        #     socketio.sleep(0.001)  # Adjust this to your liking.