#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import pandas
import os


# In[2]:


def certgen(imgpath, csvpath, destpath):
    
    imgpath = os.path.normpath(imgpath)
    csvpath = os.path.normpath(csvpath)
    destpath = os.path.normpath(destpath)
    
    data = pandas.read_csv(csvpath, names = ['id','names','mail'])
    
    idtxt = data.id.tolist() 
    nametxt = data.names.tolist()
    mailtxt = data.mail.tolist()

    print(nametxt)

    img = cv2.imread(imgpath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    colour = (0,0,0)

    thickness = 7

    fontscale = 3

    for i in range(1, len(nametxt)): #len(nametxt)
        
        xcor = 1815 - (round(len(nametxt[i])/2)*55)
        cor = (xcor, 1490)
  
        img1 = cv2.putText(img, nametxt[i], cor,font , fontscale, colour, thickness, cv2.LINE_AA)
        cv2.imwrite(os.path.join(destpath, str(idtxt[i]) + ".jpg"),img1)
        
        print(str(idtxt[i]) + " : " + str(nametxt[i]))
        img = cv2.imread(imgpath)

