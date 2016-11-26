#'C:\\Users\\Harsh\\Videos\\VID_20150408_184717.mp4'
import cv2
import numpy as np
import pylab
import counter


interactive=True
#videoname='VID_20150408_184717.mp4'
#path='C:\\Users\\Harsh\\Videos\\'

videoname='Sample1.mp4'
path=''



#opening video file

cap=cv2.VideoCapture(path+videoname)

ret,img= cap.read()
print ret
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
    frno="frame no "+str(frameno)
    print '\r'+frno,
    
    #focussing on centre
    crop=frame[120:228,980:1106]
    
    if interactive==True:
    #preview of frame and crop area
        cv2.waitKey(1)
        cv2.imshow('frame',frame)
        cv2.imshow('Measuring cropped',crop)
        
    #adding intensity of centre to list
    intensity.append(cv2.mean(crop))
    
    #stopping when video over
    if frameno==1500:
        cv2.destroyAllWindows()
        break



#preview of frame and crop area
crop=frame[120:228,980:1106]
cv2.waitKey(1)
cv2.imshow('cropped',crop)
cv2.imshow('frame',frame)
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



#Counter
peaks=counter.counter(intensity)
s="\nRed peaks:\t"+str(peaks.countred())+"\nGreen peaks:\t"+str(peaks.countgreen())+"\nBlue peaks:\t"+str(peaks.countblue())
print s