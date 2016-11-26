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
        self.cropping = False
        self.cropcanvas=image.copy()
        self.backupimg=image.copy()
        self.dragging_rect_endpoints = [(0, 0),(1, 1)]
        self.refPt = [] # alias for proper dragging_rect_endpoints
    
    
    def mouse_slave(self,event, x, y, flags, param):

 
        	# if the left mouse button was clicked, record the starting
        	# (x, y) coordinates and indicate that cropping is being
        	# performed
         if event == cv2.EVENT_LBUTTONDOWN:
             self.refPt = [(x, y),(x, y)]
             self.cropping = True
             
             self.dragging_rect_endpoints = [(x, y), (x, y)]
             
          # check to see if the left mouse button was released
         elif event == cv2.EVENT_LBUTTONUP:
                 # record the ending (x, y) coordinates and indicate that
                 # the cropping operation is finished
                 self.dragging_rect_endpoints[1] = (x, y)
                 self.cropping = False
                 
                 #making refPt a proper rect format [(left,top)(right,bottom)]
                 
                 self.refPt = self.dragging_rect_endpoints #needs to be made proper
                 (self.minX,self.minY)= (  min(self.refPt[0][0],self.refPt[1][0]), min(self.refPt[0][1],self.refPt[1][1])  )
                 (self.width,self.height) =(  abs(self.refPt[0][0]-self.refPt[1][0]), abs(self.refPt[0][1]-self.refPt[1][1])  ) 
                 self.refPt=[(self.minX,self.minY),(self.minX+self.width,self.minY+self.height)]
                 
                 # draw a rectangle around the region of interest
                 cv2.rectangle(self.cropcanvas, self.refPt[0], self.refPt[1], (0, 255, 0), 2)
                 cv2.imshow("cropcanvas", self.cropcanvas)
                 
         elif event == cv2.EVENT_MOUSEMOVE and self.cropping:
             self.dragging_rect_endpoints[1] = (x, y)       
  
  
    def runcrop(self):
        """
        Opens window for cropping
        Returns nothing. To get co-ords use getroi() after runcrop() .
        GUI Instructions:
        Click Drag and leave to make rectangle roi.
        Press 'c' to confirm or 'r' to reset.
        """
        
        instructions  = "Select an area where you would like to place the virtual photodetector."
        instructions2 = "When done:  'r' to reset , 'c' to confirm." 
                    
        cv2.namedWindow("cropcanvas")
        cv2.setMouseCallback("cropcanvas", self.mouse_slave)
        
 
        # keep looping until the 'c' key is pressed
        while True:
            # display the image and wait for a keypress
            
            if not self.cropping:
                cv2.putText(self.cropcanvas, instructions,  (10,21), cv2.FONT_HERSHEY_PLAIN, fontScale= 1, color = (255,155,155))
                cv2.putText(self.cropcanvas, instructions2, (10,42), cv2.FONT_HERSHEY_PLAIN, fontScale= 1, color = (255,155,155))
                
                cv2.imshow("cropcanvas", self.cropcanvas)
                
            elif self.cropping and self.dragging_rect_endpoints:
                self.cropcanvas = self.backupimg.copy()
                cv2.rectangle(self.cropcanvas, self.dragging_rect_endpoints[0], self.dragging_rect_endpoints[1], (0, 255, 0), 1)
                
                cv2.imshow('cropcanvas', self.cropcanvas)
            
            
            
            key = cv2.waitKey(1) & 0xFF
 
            # if the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                self.cropcanvas= self.backupimg.copy()
                self.dragging_rect_endpoints = [(0, 0),(0, 0)]
                self.refPt = [] # alias for proper dragging_rect_endpoints
 
            # if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                break
            
        cv2.destroyAllWindows()
        
    def getroi(self):
        return self.refPt
