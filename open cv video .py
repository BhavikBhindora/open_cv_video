# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:10:12 2022

@author: Dell
"""

import cv2
import numpy as np
import datetime
vid = cv2.VideoCapture(0)
c = 1
while True:
    ret,frame = vid.read()
    
    cv2.imwrite('sample.jpg', frame)
    text = 'hello world'
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, str(datetime.datetime.now()), (10,450), font, 1, (10, 150, 101), 2, cv2.LINE_AA)
    
    cv2.putText(frame, str('Bhavik bhai'), (100,400), font, 1, (150, 150, 51), 2, cv2.LINE_AA)
    c=c+1
    
    frame = cv2.rectangle(frame, (400,100), (200,300), (0,255,0), 2)
    
    cv2.imshow('Bhavik', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()