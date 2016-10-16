import numpy as np
import cv2
import time
import requests
import json
import threading
import time
#import pyglet
#import sys


#IP = "127.0.0.1"
IP = "121.201.24.49"

cap = cv2.VideoCapture(0)
classfier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
color = (0, 0, 0)

success, frame = cap.read()

emotion = "neutral"

playMusicFlag = False
stopMusicFlag = False
musicPlayState = "idle"
faceDectectedFlag = False

musicFile = "~/default.music"

def main():
    #global variable
    global frame
    global faceDectectedFlag
    global emotion

    #i is used to control the upload frequency
    i = 0

    #decide the min detection size
    size = frame.shape[:2]
    divisor=16
    h, w = size
    minSize=(w/divisor, h/divisor)

    #start music play thread
    threading.Thread(target=backgroundMusic, args=()).start()

    #main loop start
    while True:

        success, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.equalizeHist(gray, gray)
        faceRects = classfier.detectMultiScale(gray, 1.3, 5,cv2.CASCADE_SCALE_IMAGE, minSize)
        if len(faceRects) > 0:
            faceDectectedFlag = True
            lastFace = frame
            for faceRect in faceRects:
                x, y, w, h = faceRect
                #cv2.rectangle(frame, (x, y), (x+w, y+h), color)
                cv2.circle(frame, (x+w/2, y+h/2), w/2, color, 2, 8, 0)
        cv2.putText(frame, emotion, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
        cv2.imshow("face", frame)

        if i==0 and faceDectectedFlag == True:
            cv2.imwrite("face.jpg", lastFace)
            file = {'image': open("face.jpg", "rb")}
            threading.Thread(target=check_image, args=(file,)).start()
        i = (i + 1) % 80

        #key handling
        key = cv2.waitKey(10)
        c = chr(key & 255)
        if c in ['q', 'Q', chr(27)]:
            break
        if c in ['t', 'T']:
            handler_emotion("sadness")
    cv2.destroyAllWindows()


def check_image(file):
    global emotion
    print "uploading image..."
    resp = requests.post(
        "http://" + IP + ":5000/upload_image",
        files=file
    )
    json_resp = json.loads(resp.content)
    emotion = json_resp['emotion']
    handler_emotion(emotion)
    print "upload done."


def handler_emotion(emotion):
    global frame

    print emotion
    cv2.putText(frame, emotion, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    if emotion == "sadness":
        if musicPlayState == "idle":
                musicFile = "~/three_little_bird.mp3"
                musicStart = True


    elif emotion == "happiness":
        pass
    elif emotion == "neutral":
        pass
    else:
        pass

def backgroundMusic():
    global playMusicFlag
    global stopMusicFlag
    global musicPlayState

    while(True):
        if musicPlayState == "idle" :
            if playMusicFlag == True:
                #music = pyglet.resource.media(musicFile)
                #music.play()
                #pyglet.app.run()

                playMusicFlag = False
                musicPlayState == "playing"
        elif musicPlayState == "playing":
            if stopMusicFlag == True:
                pass


    #play music here


if __name__ == '__main__':
    main()

