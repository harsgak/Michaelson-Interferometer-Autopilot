import pdb
import cv2
import numpy as np
import pylab
from functions import *
from counter import Counter
from croppergui import Cropper



interactive=True



(path,videoname)=getfile()


#run process video and get returned intensity data
intensitydata=processVideo(path,videoname)


#plot the data
plotIntensity(intensitydata)




#Counter
peaks=Counter(intensitydata  )
print peaks.numpeaks
