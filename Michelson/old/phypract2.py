#'C:\\Users\\Harsh\\Videos\\VID_20150408_184717.mp4'
import cv2
import numpy as np
import pylab



videoname='VID_20150408_184717.mp4'

#opening video file
cap=cv2.VideoCapture('C:\\Users\\Harsh\\Videos\\'+videoname)
print cap.read()[1].shape


ret,img= cap.read()
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
    crop=frame[120:228,980:1106]
    
    #adding intensity of centre to list
    intensity.append(cv2.mean(crop))
    
    #stopping when video over
    if frameno==1500:
        break        
    print "\r"



#preview of frame and crop area
crop=frame[120:228,980:1106]
cv2.imshow('cropped',crop)
cv2.imshow('frame',frame)
cv2.waitKey()
cv2.destroyAllWindows()
print cv2.mean(crop)



#Displaying the list for input/output
print intensity




#Plotting
intensityb=[point[0] for point in intensity]
intensityg=[point[1] for point in intensity]
intensityr=[point[2] for point in intensity]




pylab.figure(3)
pylab.plot(intensityb)
pylab.plot(intensityg)
pylab.plot(intensityr)
pylab.title(videoname)
pylab.xlabel('Time')
pylab.ylabel('Intensity')
pylab.show()

