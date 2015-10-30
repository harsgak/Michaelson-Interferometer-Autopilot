#'C:\\Users\\Harsh\\Videos\\VID_20150408_184717.mp4'
import cv2
import numpy as np
import pylab



videoname='VID_20150408_184425.mp4'
cap=cv2.VideoCapture('C:\\Users\\Harsh\\Videos\\'+videoname)
print cap.read()[1].shape
ret,img= cap.read()
#cv2.imshow('img',img)
print "mean img=",cv2.mean(img)
frameno=0

intensity=[]


while(cap.isOpened()):
    
    #read frameincrease frame count
    ret, frame = cap.read()
    if ret==True:
        frameno+=1
    #printing frame no
    print "frame no",frameno,
    
    
    #focussing on centre
    crop=frame[175:240,990:1070]
    
    #adding intensity of centre to list
    intensity.append(cv2.mean(crop))
    
    """if frameno>630:
        cv2.imshow('cropped',crop)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break"""
    if frameno==1680:
        break        
    print "\r"

crop=frame[180:250,990:1070]
"""(b,g,r)= cv2.split(full)
b[:][:]=0
full=cv2.merge((b,g,r))"""
cv2.imshow('cropped',crop)
cv2.imshow('frame',frame)
print cv2.mean(crop)
print intensity












#Plotting
intensityb=[point[0] for point in intensity]
intensityg=[point[1] for point in intensity]
intensityr=[point[2] for point in intensity]




pylab.figure(1)
pylab.plot(intensityb)
pylab.plot(intensityg)
pylab.plot(intensityr)
pylab.title(videoname)
pylab.xlabel('Time')
pylab.ylabel('Intensity')
pylab.show()