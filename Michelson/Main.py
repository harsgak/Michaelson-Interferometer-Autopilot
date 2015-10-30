import cv2
import numpy as np
import pylab
from functions import *
import counter


interactive=True


######################################################
#(path,videoname)=getfile()
videoname='VID_20150408_184717.mp4'
path='C:\\Users\\Harsh\\Videos\\'
####################################################


intensity=processVideo(path,videoname)

plotIntensity(intensity)

#Counter
peaks=counter.counter(intensity)
print peaks.numpeaks
