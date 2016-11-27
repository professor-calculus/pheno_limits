#!/usr/bin/env python
"""
run exactly the same way as './plotContour.py' but gives only list of values needed for fancy limit plotter
"""
import ROOT as r
import sys
import math as m
import numpy as np
from array import array
import random
from array import array

from scipy import interpolate
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.colors as mcol



def makePlot():


  for k in range(len(sys.argv)-1):
    infile = open(sys.argv[k+1],"r")
    filestoread=infile.readlines()
    yvalues=[]
    for i in range(len(filestoread)):
      thisline=filestoread[i].split()
      yvalues.append([float(thisline[0]),thisline[1]])
    yvalues.sort(key=lambda x: float(x[0]))

    #loop over y values getting tfiles and extracting x values and limits
    medianvalues=[]
    ybincenters=[]
    xbincenters=[]

    for i in range(len(yvalues)):
      ybincenters.append(float(yvalues[i][0]))
      tf = r.TFile(yvalues[i][1])
      tree = tf.Get('limit')
      xvalues=[]
      for j in range(tree.GetEntries()):
        tree.GetEntry(j)
        xvalues.append([tree.mh, tree.limit])
        xvalues.sort(key=lambda x: float(x[0]))
      
        
      xs = []
      for item in xvalues:
            if item[0] not in xs: xs.append(item[0])

      # get how many of them are there in the list
      for x in xs:
            check = [item for item in xvalues if x in item]
            
            if i==0:
                  xbincenters.append(x)
            
      # get limits for all x values for this y value
      for j in range(len(xvalues)):
        if (j%6==0):
          if len(xvalues)>j+2 : medianvalues.append([xvalues[j][0],yvalues[i][0],xvalues[j+2][1]])
          else : medianvalues.append([xvalues[j][0],yvalues[i][0],10000])

    graph_exp=r.TGraph2D()


    xvalues=[]
    yvalues=[]
    values=[]
    matrix=[]
    
    #Populate TGraph with points
    n=0
    for j in range(len(ybincenters)):
      for i in range(len(xbincenters)):
        print '['+str(xbincenters[i])+', ' +str(ybincenters[j])+', '+str(round(medianvalues[j*len(xbincenters)+i][2],4))+'],'
        xvalues.append(xbincenters[i])
        yvalues.append(ybincenters[j])
        values.append(round(medianvalues[j*len(xbincenters)+i][2],4))
        n=n+1


    exp = np.array((xvalues, yvalues, values), dtype=float)
    
makePlot()

 

