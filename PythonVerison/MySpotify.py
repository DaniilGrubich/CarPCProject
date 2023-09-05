import os

import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

import cloudscraper
from PIL import Image


SPOTIPY_CLIENT_ID='XXX'
SPOTIPY_CLIENT_SECRET='XXX'
SPOTIPY_REDIRECT_URI='https://www.google.com/'

username = 'XXX'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

token = None
spotifyObject = None

trackJSON = ""

albumPicLink = ""
lastSongName = ""
songName = ""
artist_name = ""
totalDuration = 0
currentProgress = 0



def openSpotify():
    global token, spotifyObject
    try:
        token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)

    spotifyObject = spotipy.Spotify(auth=token)

    print('Spotify Connected')

def updateTrackJSON():
    global trackJSON, songName, lastSongName, totalDuration, currentProgress, artist_name, albumPicLink
    try:
        trackJSON = spotifyObject.current_user_playing_track()

        if (trackJSON != None):
            artist_name = trackJSON['item']['artists'][0]["name"]
            # for entry in artist_name:
            #     artist_name = entry['name']

            lastSongName = songName
            songName = trackJSON['item']['name']

            currentProgress = int(trackJSON["progress_ms"])
            totalDuration = int(trackJSON["item"]["duration_ms"])

            albumPicLink = getSongImageURL("medium")

        else:
            songName = ""
            currentProgress = 0
            totalDuration = 10
    except:
        openSpotify()





#sizes: small (64), medium (300), large (640)
def getSongImageURL(size):
    url = ""

    try:
        if (trackJSON != None):
            if(size == "small"):
                url = trackJSON["item"]["album"]["images"][2]["url"]
            elif(size == "medium"):
                url = trackJSON["item"]["album"]["images"][1]["url"]
            elif(size == "large"):
                url = trackJSON["item"]["album"]["images"][0]["url"]
    except:
        url = trackJSON["item"]["album"]["images"][2]["url"]

    print(url)
    return url


def nextSong():
    spotifyObject.next_track()


def lastSong():
    spotifyObject.previous_track()

def isTrackUpdated():
    return lastSongName != songName