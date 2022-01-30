#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import numpy as np
import cv2
import time


# In[ ]:


# Recording and coaching the background for each frame

cap=cv2.VideoCapture(0) #Read from the web cam

time.sleep(3) #for the system to sleep for 3 sec before the web cam start

retval,back=cap.read()
back=np.flip(back,axis=1)

## Detecting the red portion in each frame

while (cap.isOpened()): #read every frame from the webcam, until the camera is open
    ret,img=cap.read()
    if ret:
        img=np.flip(img,axis=1)
        
        #Convert the color space from BGR to HSV
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        
        #Generate masks to detect red color
        lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv,lower_red,upper_red)
        
        lower_red = np.array([170,20,70])
        upper_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv,lower_red,upper_red)
        mask1+mask2
        
        #Replacing the red portion with a mask image in each frame
        
        mask = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
        img[np.where(mask==255)]=back[np.where(mask==255)]
        
        #final output
        cv2.imshow("Harry Potter's invisible secret revealed",img)
    key = cv2.waitKey(1)
    if key==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
        


# In[ ]:





# In[ ]:




