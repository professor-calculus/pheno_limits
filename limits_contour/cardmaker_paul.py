#!/usr/bin/python
import sys
import math as m
import argparse as a


#Get options
parser=a.ArgumentParser(description='Make cards for pheno studies')
parser.add_argument('-s','--sig_yield_19_2fb',required=True)
#parser.add_argument('-l','--targetlumi',required=True)
#parser.add_argument('--systlumiscale',default=False)
parser.add_argument('-n','--name',default='125')
parser.add_argument('--sqrts',default=13)
parser.add_argument('-b','--batchmode',default=False)
args=parser.parse_args()


#Our example model: In the measurement we have 12 events (data), the bkg prediction is 6.6 +/- 1.3
data_yield=12
bkg_yield=6.6
sig_yield=args.sig_yield_19_2fb
bkg_stat=1.3
#we're ignoring statistical errors here -- with enough MC events they shouldn't matter much anyway
bkg_syst=0.
sig_syst=0.


#systlumiscale=args.systlumiscale
signalname=args.name

if(args.batchmode==False):
    print 'Model name is: '+str(signalname)
    if not systlumiscale:
        print 'Not scaling systematics assuming constant'
    else:
        print 'Scaling systematics with sqrt(L)'

scalef=1

#if systlumiscale:
#    bkg_syst=m.sqrt(scalef/float(targetlumi))*float(bkg_syst_19_2fb)
#    sig_syst=m.sqrt(scalef/float(targetlumi))*float(sig_syst_19_2fb)
#else:
 
#Open output file
cardname='darkHiggs_'+str(signalname)+'.txt'
if(args.batchmode==True):
    print cardname
card=open(cardname,'w')

card.write('# Invisible Higgs analysis for '+str(signalname)+'\n')#Next few lines are admin stuff at beginning of card
card.write('imax 1 number of bins\n')
card.write('jmax 1 number of backgrounds\n')
card.write('kmax * number of nuisance parameters (sources of systematic uncertainties)\n')
card.write('shapes * ch1 FAKE\n')
card.write('bin ch1\n')
card.write('observation '+str(data_yield)+'\n')#set observation equal to data_yield or expected background
card.write('------------\n')
card.write('bin\t\t\tch1\tch1\n')
card.write('process\t\t\tsig\tbkg\n')
card.write('process\t\t\t0\t1\n')
card.write('rate\t\t\t'+str(sig_yield)+'\t'+str(bkg_yield)+'\n')
card.write('------------\n')
card.write('bkg_stat\tlnN\t-\t'+str(bkg_stat+1)+'\n')
card.write('bkg_syst\tlnN\t-\t'+str(bkg_syst+1)+'\n')
card.write('sig_syst\tlnN\t'+str(sig_syst+1)+'\t-\n')
