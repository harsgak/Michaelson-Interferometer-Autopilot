import pdb
import cv2
import numpy as np
import pylab
from functions import *
from counter import Counter
from croppergui import Cropper



interactive=True


######################################################
#(path,videoname)=askfile()
videoname='VID_20150408_184717.mp4'
path='C:\\Users\\Harsh\\Videos\\'
####################################################


#run process video and get returned intensity data
intensitydata=processVideo(path,videoname)


#plot the data
plotIntensity(intensitydata)




#Counter
peaks=Counter(intensitydata  )
print peaks.numpeaks
