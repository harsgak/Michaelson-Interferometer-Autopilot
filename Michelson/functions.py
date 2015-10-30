def getfile():
    """
    Asks the user for input file (location). Could be video,txt etc.
    returns tuple (path, filename)
    """




def processVideo(path,videoname="",interactive=True,cropto=[(120,980),(228,1106)],startframe=0,endframe=1500):
    import cv2
    #opening video file

    cap=cv2.VideoCapture(path+videoname)
    
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
        if frameno==endframe:
            cv2.destroyAllWindows()
            return intensity
            break
def plotIntensity(intensity):
    import pylab
    #Plotting
    intensityb=[point[0] for point in intensity]
    intensityg=[point[1] for point in intensity]
    intensityr=[point[2] for point in intensity]
    
    
    pylab.figure(3)
    pylab.plot(intensityb)
    pylab.plot(intensityg)
    pylab.plot(intensityr)
    pylab.title("FringeIntensity")
    pylab.xlabel('Time')
    pylab.ylabel('Intensity')
    pylab.show()
    #Add a peak plotter too . which plots the peak points detected in counter.

