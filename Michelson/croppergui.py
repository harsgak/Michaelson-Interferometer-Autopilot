# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 01:50:10 2015

@author: Harsh
"""
# Thanks to Adrian Rosebrock for tutorial on pyimagesearch.com

import cv2
import pdb
class Cropper(object):
    """Cropper Class
    Needs to be attached to an image file while construction.
    """
    def __init__(self,image):
        import cv2
        self.refPt = []
        self.cropping = False
        self.cropcanvas=image.copy()
        self.backupimg=image.copy()
    
    
    def mouse_slave(self,event, x, y, flags, param):

 
        	# if the left mouse button was clicked, record the starting
        	# (x, y) coordinates and indicate that cropping is being
        	# performed
         if event == cv2.EVENT_LBUTTONDOWN:
             self.refPt = [(x, y)]
             self.cropping = True
             
          # check to see if the left mouse button was released
         elif event == cv2.EVENT_LBUTTONUP:
                 # record the ending (x, y) coordinates and indicate that
                 # the cropping operation is finished
                 self.refPt.append((x, y))
                 self.cropping = False
                 
                 #making refPt a proper rect format [(left,top)(right,bottom)]
                 (self.minX,self.minY)= (  min(self.refPt[0][0],self.refPt[1][0]), min(self.refPt[0][1],self.refPt[1][1])  )
                 (self.width,self.height) =(  abs(self.refPt[0][0]-self.refPt[1][0]), abs(self.refPt[0][1]-self.refPt[1][1])  ) 
                 self.refPt=[(self.minX,self.minY),(self.minX+self.width,self.minY+self.height)]
                 
                 # draw a rectangle around the region of interest
                 cv2.rectangle(self.cropcanvas, self.refPt[0], self.refPt[1], (0, 255, 0), 2)
                 cv2.imshow("cropcanvas", self.cropcanvas)
                 
  
  
    def runcrop(self):
        """
        Opens window for cropping
        Returns nothing. To get co-ords use getroi() after runcrop() .
        GUI Instructions:
        Click Drag and leave to make rectangle roi.
        Press 'c' to confirm or 'r' to reset.
        """
        cv2.namedWindow("cropcanvas")
        cv2.setMouseCallback("cropcanvas", self.mouse_slave)
 
        # keep looping until the 'c' key is pressed
        while True:
            # display the image and wait for a keypress
            cv2.imshow("cropcanvas", self.cropcanvas)
            key = cv2.waitKey(1) & 0xFF
 
            # if the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                self.cropcanvas= self.backupimg.copy()
 
            # if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                break
        cv2.destroyAllWindows()
        
    def getroi(self):
        return self.refPt
