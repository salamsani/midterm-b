# -*- coding: utf-8 -*-
"""
Created on Thu May  2 04:35:03 2019

@author: salam
"""

import numpy as np
import matplotlib.pyplot as plt

Afname = input(str('Name of airfoil:')) 
    
Airfoil = np.loadtxt(Afname+'.dat', skiprows=1)

xarray = []
yarray = []
xlist = np.append(xarray, Airfoil[:,0])
ylist = np.append(yarray, Airfoil[:,1])


# Construct airfoil geometry===================================================

def airfoil_name():    
    airfoil_geo = plt.plot(xlist,ylist,'-')
    plt.axes().set_aspect(1, 'datalim')
    plt.title(Afname)
    
    return airfoil_geo

# MEAN CAMBER LINE AND CHORDLINE==============================================

def mean_camber_line():
    
    y_mcpoints = []
    x_mcpoints = []
     
    for points, xcoord in enumerate(xlist):
        if points == int(xlist.size/2):
            break
        x_mcpoints = np.append(x_mcpoints, xcoord)
    
    for points, ycoord in enumerate(ylist):
        if points == int(ylist.size/2):
            break
        a = ylist[ylist.size-1-points]
        y_mcpoints = np.append(y_mcpoints, (ycoord+a)/2)
    
    return plt.plot(x_mcpoints,y_mcpoints, label='Mean camberline')

def chordline():
    a = int((len(xlist))/2)
    x_chordline = [xlist[-1],xlist[a]]
    y_chordline = [0,0]
    
    return plt.plot(x_chordline, y_chordline, label='Chordline')
    
    
# MAXIMUM THICKNESS AND POSITION ==============================================
    
def max_thickness():

    ymax = np.max(ylist)
    ymin = np.min(ylist)
    maxthickness = ymax + abs(ymin)
    
    xpoint = [xlist[ylist.argmax()], xlist[ylist.argmax()]] 
    ypoint = [ymax, ymin]
    
    print('Max y-point:',ymax)
    print('Min y-point:',ymin)
    print('Maximum thickness:',maxthickness)
    
    return plt.plot(xpoint, ypoint, label='Maximum thickness : '+ str(float(maxthickness)))

plt.figure(figsize=(10,5))
plt.xlabel('x-coordinates', fontsize=15)
plt.ylabel('y-coordinates', fontsize=15)      
plt.grid()


airfoil_name()
mean_camber_line()
max_thickness()
chordline()
plt.legend()
#save_results_to = '/H:/utaa/8th sem/python/midterm project/airfoil_project/airfoil graphics/'
#plt.savefig(save_results_to + Afname, dpi = 300)
plt.savefig(Afname+'.jpg')
plt.show()
plt.close()
