#!/usr/bin/python
import os
import sys
import argparse as a

cardmakerpath='./cardmaker_paul.py'
combinecommand='combine -M Asymptotic'
outfilename='grid_info'

parser=a.ArgumentParser(description='Make and run over grid of cards for pheno studies')
parser.add_argument('-i','--infile',required=True)
parser.add_argument('--xname',default='mS')
parser.add_argument('--yname',default='mZp')
args=parser.parse_args()

xvarname=args.xname
yvarname=args.yname
infilename=args.infile
path = os.path.split(infilename)[0]+'/'
print 'xvar: '+xvarname+' yvar: '+yvarname+' from '+infilename

infile=open(infilename)
points=infile.readlines()
vals=[]

for iPoint in range(len(points)):
    thisPoint=points[iPoint].split()
    if(len(thisPoint)!=3):
        print 'Error input format should be: xval yval yield, not '+points[iPoint]
    xvarval=thisPoint[0]
    yvarval=thisPoint[1]
    vals.append([yvarval,xvarval])
    yield_19_2fb=thisPoint[2]


    print(cardmakerpath+' -s '+yield_19_2fb+' -n '+xvarname+xvarval+yvarname+yvarval+' -b True')
    print(combinecommand+' -m '+xvarval+' -n '+yvarname+yvarval+'_'+xvarname+xvarval+' darkHiggs_'+xvarname+xvarval+yvarname+yvarval+'.txt')

    os.system(cardmakerpath+' -s '+yield_19_2fb+' -n '+xvarname+xvarval+yvarname+yvarval+' -b True')
    os.system(combinecommand+' -m '+xvarval+' -n '+yvarname+yvarval+'_'+xvarname+xvarval+' darkHiggs_'+xvarname+xvarval+yvarname+yvarval+'.txt')


#Check grid is complete
xvals=[]
yvals=[]
for i in range(len(vals)):
    print len(vals)
    if vals[i][1] not in xvals:
          xvals.append(vals[i][1])
    if vals[i][0] not in yvals:
          yvals.append(vals[i][0])
print 'xvals = '+str(xvals)
print  'yvals = '+str(yvals)
for i in range(len(xvals)):
    for j in range(len(yvals)):
        if [yvals[j],xvals[i]] not in vals:
            print 'Error: you must have a value for all points in the grid'
            print str(yvals[j])+' and '+str(xvals[i])+'are not in '
            print vals
#            exit() #disable this for not rectangular grids

#make input for exclusion plotter
outfilesyst=open(path+outfilename+'.txt','w')
for i in range(len(yvals)):
        outfilesyst.write(yvals[i]+' '+os.getcwd()+'/'+path+'/'+yvarname+yvals[i]+'combineresults.root\n')
        print('hadd -f '+yvarname+yvals[i]+'combineresults.root higgsCombine'+yvarname+yvals[i]+'_'+xvarname+'*.root')
        os.system('hadd -f '+yvarname+yvals[i]+'combineresults.root higgsCombine'+yvarname+yvals[i]+'_'+xvarname+'*.root')

os.system('mv higgsCombinem* '+path)
os.system('mv *.root '+path)
os.system('mv *.txt '+path)
