import cv2
import pickle
import numpy as np

vagas = []
with open('vagas.pkl', 'rb') as arquivo:
    vagas = pickle.load(arquivo)

video = cv2.VideoCapture('assets/video.mp4')
kernel = np.ones((3,3), np.int8)

while True:
    check, img = video.read()
    imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    imgThold = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThold, 5)
    imgDilat = cv2.dilate(imgMedian, kernel)

    for x, y, w, h in vagas:
        cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0),2)
    cv2.imshow('Video', img)
    cv2.imshow('Video Thold', imgThold)
    cv2.imshow('Video Dilat', imgDilat)


    cv2.waitKey(10)