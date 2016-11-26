import cv2
import pdb
import time


def getfile():
    """
    Asks the user for input file (location). Could be video,txt etc.
    returns tuple (path, filename)
    """
    
    z = False
    while z == False :
        filename=raw_input("Please enter file name (whole address if possible)\nNote: You can drag and drop the file in too.\n")
        if filename.startswith('"') and filename.endswith('"'):
            filename = filename[1:-1]
        if filename.startswith("'") and filename.endswith("'"):
            filename = filename[1:-1]
        try:
            txt=open(filename,'r+')
            z = True
            txt.close()
        except IOError:
            print "Sorry couldnt find/open file"

    rev_file = filename[::-1]
    count = 0
    for i in rev_file :
        if i == '\\' :
            break_index = rev_file.index(i)
            count = 1
            break
    
    if count == 0 :
        path = ''
        videoname = filename
    else :
        path = rev_file[break_index:][::-1]        
        videoname = rev_file[:break_index][::-1]
    return (path, videoname)

    



def processVideo(path,videoname="",interactive=True,startframe=0,endframe=1500):
    import cv2
    import pdb
    from croppergui import Cropper
    #opening video file

    cap=cv2.VideoCapture(path+videoname)
    
    #pdb.run("print cap.read()[1].shape")
    
    frameno=0
    ret,img= cap.read()
    
    if ret == False:
        raise IOError('Could not read video. Try installing opencv_ffmpeg.dll')
    
    
    #Getting the coord of area to focus on
    roi=askFocusArea(img)
    print roi
    (x1,y1)=roi[0]
    (x2,y2)=roi[1]
    

    intensity=[]
    
    
    # Video  Processing loop.
    while(cap.isOpened()):
    
        #read frameincrease frame count
        ret, frame = cap.read()
        if ret==True:
            frameno+=1
        #printing frame no
        frno="frame no "+str(frameno)
        
    
        
        #focussing on centre
        crop=frame[y1:y2,x1:x2]
        
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

def askFocusArea(image):
    from croppergui import Cropper
    
    instructions = """
    You are going to cropper window...
    A cropcanvas window should open in the background.
    Select an area where you would like to place the virtual photodetector. (MouseDown...Drag....MouseRelease)
    When done:
                'c' to confirm.  'r' to reset 
    """
    print instructions
    time.sleep(5)
    
    roigenerator=Cropper(image)
    roigenerator.runcrop()
    roi=roigenerator.getroi()
    
    if len(roi) == 2:
        #pdb.run("""print "Got 2 points of roi rect" """)
        if roi[0]!=roi[1]:
            return roi
    else :
        #pdb.run("""print "Cropper.getroi() failed to return 2 pionts!!" """)
        print "Sorry couldnt get area from mouseclicks\n Refer "
        manual=raw_input ( "To enter manual focus mode reply 1 \nTo retry in cropper window reply 0.\nReply: ")
        if manual=="1":
            x1=input("Enter x1: ")
            y1=input("Enter y1: ")
            x2=input("Enter x2: ")
            y2=input("Enter y2: ")
            roi=[(x1,y1),(x2,y2)]
            print "Required area  is the rectangle bounded by "+str(roi)
            confirm=raw_input("To confirm:  enter 1\nTo retry:    enter 0\nReply: ")
            if confirm=="1":
                (minX,minY)= (  min(roi[0][0],roi[1][0]), min(roi[0][1],roi[1][1])  )
                (width,height) =(  abs(roi[0][0]-roi[1][0]), abs(roi[0][1]-roi[1][1])  ) 
                roi=[(minX,minY),(minX+width,minY+height)]
                
                return roi
            else:
                return askFocusArea(image)
        else:
            return askFocusArea(image)
            
