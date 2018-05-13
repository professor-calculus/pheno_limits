#!/usr/bin/python
import os
import sys
import argparse as a

cardmakerpath='./cardmaker_MHT_combined_exp.py'
combinecommand='combine -M Asymptotic'
outfilename='grid_info2'

parser=a.ArgumentParser(description='Make and run over grid of cards for pheno studies')
parser.add_argument('-i','--infile',required=True)
parser.add_argument('-j','--infile2',required=True)
parser.add_argument('-j2','--infile3',required=True)
parser.add_argument('-j3','--infile4',required=True)
parser.add_argument('-j4','--infile5',required=True)
parser.add_argument('-j5','--infile6',required=True)
parser.add_argument('-j6','--infile7',required=True)
parser.add_argument('-j7','--infile8',required=True)
parser.add_argument('--xname',default='mS')
parser.add_argument('--yname',default='mZp')
args=parser.parse_args()

xvarname=args.xname
yvarname=args.yname
infilename=args.infile
infilename2=args.infile2
infilename3=args.infile3
infilename4=args.infile4
infilename5=args.infile5
infilename6=args.infile6
infilename7=args.infile7
infilename8=args.infile8


path = os.path.split(infilename)[0]+'/'
print 'xvar: '+xvarname+' yvar: '+yvarname+' from '+infilename

infile=open(infilename)
points=infile.readlines()
vals=[]

infile2=open(infilename2)
points2=infile2.readlines()
vals2=[]

infile3=open(infilename3)
points3=infile3.readlines()
vals3=[]

infile4=open(infilename4)
points4=infile4.readlines()
vals4=[]

infile5=open(infilename5)
points5=infile5.readlines()
vals5=[]

infile6=open(infilename6)
points6=infile6.readlines()
vals6=[]

infile7=open(infilename7)
points7=infile7.readlines()
vals7=[]

infile8=open(infilename8)
points8=infile8.readlines()
vals8=[]

for iPoint in range(len(points)):
    thisPoint=points[iPoint].split()
    thisPoint2=points2[iPoint].split()
    thisPoint3=points3[iPoint].split()
    thisPoint4=points4[iPoint].split()
    thisPoint5=points5[iPoint].split()
    thisPoint6=points6[iPoint].split()
    thisPoint7=points7[iPoint].split()
    thisPoint8=points8[iPoint].split()
    if(len(thisPoint)!=3):
        print 'Error input format should be: xval yval yield, not '+points[iPoint]
    xvarval=thisPoint[0]
    yvarval=thisPoint[1]
    vals.append([yvarval,xvarval])
    yield_19_2fb=thisPoint[2]
    yield2_19_2fb=thisPoint2[2]
    yield3_19_2fb=thisPoint3[2]
    yield4_19_2fb=thisPoint4[2]
    yield5_19_2fb=thisPoint5[2]
    yield6_19_2fb=thisPoint6[2]
    yield7_19_2fb=thisPoint7[2]
    yield8_19_2fb=thisPoint8[2]


    print(cardmakerpath+' -s '+yield_19_2fb+' -t '+yield2_19_2fb+' -n '+xvarname+xvarval+yvarname+yvarval+' -b True')
    print(combinecommand+' -m '+xvarval+' -n '+yvarname+yvarval+'_'+xvarname+xvarval+' darkHiggs_'+xvarname+xvarval+yvarname+yvarval+'.txt')

    os.system(cardmakerpath+' -s '+yield_19_2fb+' -t '+yield2_19_2fb+' -t2 '+yield3_19_2fb+' -t3 '+yield4_19_2fb+' -t4 '+yield5_19_2fb+' -t5 '+yield6_19_2fb+' -t6 '+yield7_19_2fb+' -t7 '+yield8_19_2fb+' -n '+xvarname+xvarval+yvarname+yvarval+' -b True')
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
