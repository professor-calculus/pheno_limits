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
import pandas as pd

from scipy import interpolate
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.colors as mcol



def makePlot():

  columns = ['M_sq', 'M_lsp', 'mu']
  for k in range(len(sys.argv)-1):
    infile = open(sys.argv[k+1],"r")
    filestoread=infile.readlines()
    yvalues=[]
    for i in range(len(filestoread)):
      thisline=filestoread[i].split()
      yvalues.append([float(thisline[0]),thisline[1]])
    yvalues.sort(key=lambda x: float(x[0]))

    #loop over y values getting tfiles and extracting x values and limits
    medianvalues = pd.DataFrame(columns=columns)
    observedvalues = pd.DataFrame(columns=columns)
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
        print([tree.mh, yvalues[i][0], tree.limit, tree.quantileExpected])
        
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
          if len(xvalues)>j+2 : medianvalues = medianvalues.append({'M_sq': xvalues[j][0], 'M_lsp': yvalues[i][0], 'mu': xvalues[j+2][1]}, ignore_index=True)
          else : medianvalues = medianvalues.append({'M_sq': xvalues[j][0],'M_lsp': yvalues[i][0],'mu': 10000}, ignore_index=True)
          if len(xvalues)>j+5 : observedvalues = observedvalues.append({'M_sq': xvalues[j][0], 'M_lsp': yvalues[i][0], 'mu': xvalues[j+5][1]}, ignore_index=True)
          else : observedvalues = observedvalues.append({'M_sq': xvalues[j][0],'M_lsp': yvalues[i][0],'mu': 10000}, ignore_index=True)

    medianvalues.to_csv('mu_expected.txt', sep='\t', index=False, header=False)
    observedvalues.to_csv('mu_observed.txt', sep='\t', index=False, header=False)
    print(medianvalues)

    #graph_exp=r.TGraph2D()


    xvalues=[]
    yvalues=[]
    values=[]
    matrix=[]
    
    #Populate TGraph with points
    n=0
    for j in range(len(ybincenters)):
      for i in range(len(xbincenters)):
        #with open("output.out", "a") as text_file:
	#    mystring='['+str(xbincenters[i])+', ' +str(ybincenters[j])+', '+str(round(medianvalues[j*len(xbincenters)+i][2],4))+'],'
        #    text_file.write("{}\n".format(mystring))
        #print '['+str(xbincenters[i])+', ' +str(ybincenters[j])+', '+str(round(medianvalues[j*len(xbincenters)+i][2],4))+'],'
        #xvalues.append(xbincenters[i])
        #yvalues.append(ybincenters[j])
        #values.append(round(medianvalues[j*len(xbincenters)+i][2],4))
        n=n+1

    #exp = np.array((xvalues, yvalues, values), dtype=float)

makePlot()
