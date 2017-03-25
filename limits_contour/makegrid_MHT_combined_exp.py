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
parser.add_argument('-j8','--infile9',required=True)
parser.add_argument('-j9','--infile10',required=True)
parser.add_argument('-j10','--infile11',required=True)
parser.add_argument('-j11','--infile12',required=True)
parser.add_argument('-j12','--infile13',required=True)
parser.add_argument('-j13','--infile14',required=True)
parser.add_argument('-j14','--infile15',required=True)
parser.add_argument('-j15','--infile16',required=True)
parser.add_argument('-j16','--infile17',required=True)
parser.add_argument('-j17','--infile18',required=True)
parser.add_argument('-j18','--infile19',required=True)
parser.add_argument('-j19','--infile20',required=True)
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
infilename9=args.infile9
infilename10=args.infile10
infilename11=args.infile11
infilename12=args.infile12
infilename13=args.infile13
infilename14=args.infile14
infilename15=args.infile15
infilename16=args.infile16
infilename17=args.infile17
infilename18=args.infile18
infilename19=args.infile19
infilename20=args.infile20


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

infile9=open(infilename9)
points9=infile9.readlines()
vals9=[]

infile10=open(infilename10)
points10=infile10.readlines()
vals10=[]

infile11=open(infilename11)
points11=infile11.readlines()
vals11=[]

infile12=open(infilename12)
points12=infile12.readlines()
vals12=[]

infile13=open(infilename13)
points13=infile13.readlines()
vals13=[]

infile14=open(infilename14)
points14=infile14.readlines()
vals14=[]

infile15=open(infilename15)
points15=infile15.readlines()
vals15=[]

infile16=open(infilename16)
points16=infile16.readlines()
vals16=[]

infile17=open(infilename17)
points17=infile17.readlines()
vals17=[]

infile18=open(infilename18)
points18=infile18.readlines()
vals18=[]

infile19=open(infilename19)
points19=infile19.readlines()
vals19=[]

infile20=open(infilename20)
points20=infile20.readlines()
vals20=[]

for iPoint in range(len(points)):
    thisPoint=points[iPoint].split()
    thisPoint2=points2[iPoint].split()
    thisPoint3=points3[iPoint].split()
    thisPoint4=points4[iPoint].split()
    thisPoint5=points5[iPoint].split()
    thisPoint6=points6[iPoint].split()
    thisPoint7=points7[iPoint].split()
    thisPoint8=points8[iPoint].split()
    thisPoint9=points9[iPoint].split()
    thisPoint10=points10[iPoint].split()
    thisPoint11=points11[iPoint].split()
    thisPoint12=points12[iPoint].split()
    thisPoint13=points13[iPoint].split()
    thisPoint14=points14[iPoint].split()
    thisPoint15=points15[iPoint].split()
    thisPoint16=points16[iPoint].split()
    thisPoint17=points17[iPoint].split()
    thisPoint18=points18[iPoint].split()
    thisPoint19=points19[iPoint].split()
    thisPoint20=points20[iPoint].split()
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
    yield9_19_2fb=thisPoint9[2]
    yield10_19_2fb=thisPoint10[2]
    yield11_19_2fb=thisPoint11[2]
    yield12_19_2fb=thisPoint12[2]
    yield13_19_2fb=thisPoint13[2]
    yield14_19_2fb=thisPoint14[2]
    yield15_19_2fb=thisPoint15[2]
    yield16_19_2fb=thisPoint16[2]
    yield17_19_2fb=thisPoint17[2]
    yield18_19_2fb=thisPoint18[2]
    yield19_19_2fb=thisPoint19[2]
    yield20_19_2fb=thisPoint20[2]


    print(cardmakerpath+' -s '+yield_19_2fb+' -t '+yield2_19_2fb+' -n '+xvarname+xvarval+yvarname+yvarval+' -b True')
    print(combinecommand+' -m '+xvarval+' -n '+yvarname+yvarval+'_'+xvarname+xvarval+' darkHiggs_'+xvarname+xvarval+yvarname+yvarval+'.txt')

    os.system(cardmakerpath+' -s '+yield_19_2fb+' -t '+yield2_19_2fb+' -t2 '+yield3_19_2fb+' -t3 '+yield4_19_2fb+' -t4 '+yield5_19_2fb+' -t5 '+yield6_19_2fb+' -t6 '+yield7_19_2fb+' -t7 '+yield8_19_2fb+' -t8 '+yield9_19_2fb+' -t9 '+yield10_19_2fb+' -t10 '+yield11_19_2fb+' -t11 '+yield12_19_2fb+' -t12 '+yield13_19_2fb+' -t13 '+yield14_19_2fb+' -t14 '+yield15_19_2fb+' -t15 '+yield16_19_2fb+' -t16 '+yield17_19_2fb+' -t17 '+yield18_19_2fb+' -t18 '+yield19_19_2fb+' -t19 '+yield20_19_2fb+' -n '+xvarname+xvarval+yvarname+yvarval+' -b True')
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
