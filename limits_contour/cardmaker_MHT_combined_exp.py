#!/usr/bin/python
import sys
import math as m
import argparse as a


#Get options
parser=a.ArgumentParser(description='Make cards for pheno studies')
parser.add_argument('-s','--sig_yield_19_2fb',required=True)
parser.add_argument('-t','--sig2_yield_19_2fb',required=True)
parser.add_argument('-t2','--sig3_yield_19_2fb',required=True)
parser.add_argument('-t3','--sig4_yield_19_2fb',required=True)
parser.add_argument('-t4','--sig5_yield_19_2fb',required=True)
parser.add_argument('-t5','--sig6_yield_19_2fb',required=True)
parser.add_argument('-t6','--sig7_yield_19_2fb',required=True)
parser.add_argument('-t7','--sig8_yield_19_2fb',required=True)
#parser.add_argument('-l','--targetlumi',required=True)
#parser.add_argument('--systlumiscale',default=False)
parser.add_argument('-n','--name',default='125')
parser.add_argument('--sqrts',default=13)
parser.add_argument('-b','--batchmode',default=False)
args=parser.parse_args()

#2b
data_yield=0
bkg_yield=2.509093
sig_yield=args.sig_yield_19_2fb
bkg_syst=1.021211/bkg_yield

data2_yield=0
bkg2_yield=1.645531
sig2_yield=args.sig2_yield_19_2fb
bkg2_syst=0.444197/bkg2_yield

data3_yield=2
bkg3_yield=0.618039
sig3_yield=args.sig3_yield_19_2fb
bkg3_syst=0.317244/bkg3_yield

data4_yield=0
bkg4_yield=0.192437
sig4_yield=args.sig4_yield_19_2fb
bkg4_syst=0.174512/bkg4_yield

data5_yield=1
bkg5_yield=0.398526
sig5_yield=args.sig5_yield_19_2fb
bkg5_syst=0.164178/bkg5_yield

data6_yield=0
bkg6_yield=0.248091
sig6_yield=args.sig6_yield_19_2fb
bkg6_syst=0.077614/bkg6_yield

data7_yield=1
bkg7_yield=0.085507
sig7_yield=args.sig7_yield_19_2fb
bkg7_syst=0.038463/bkg7_yield

data8_yield=0
bkg8_yield=0.023877
sig8_yield=args.sig8_yield_19_2fb
bkg8_syst=0.021558/bkg8_yield

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
card.write('imax 8 number of bins\n')
card.write('jmax * number of backgrounds\n')
card.write('kmax * number of nuisance parameters (sources of systematic uncertainties)\n')
#card.write('shapes * * FAKE\n')
card.write('bin\tch1\tch2\tch3\tch4\tch5\tch6\tch7\tch8\n')
card.write('observation '+str(bkg_yield)+' '+str(bkg2_yield)+' '+str(bkg3_yield)+' '+str(bkg4_yield)+' '+str(bkg5_yield)+' '+str(bkg6_yield)+' '+str(bkg7_yield)+' '+str(bkg8_yield)+'\n')#set observation equal to data_yield or expected background
card.write('----------------------------------------------------------------------------\n')
card.write('bin\t\t\tch1\tch1\tch2\tch2\tch3\tch3\tch4\tch4\tch5\tch5\tch6\tch6\tch7\tch7\tch8\tch8\n')
card.write('process\t\t\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\n')
card.write('process\t\t\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\n') 
card.write('rate\t\t\t'+str(sig_yield)+'\t'+str(bkg_yield)+'\t'+str(sig2_yield)+'\t'+str(bkg2_yield)+'\t'+str(sig3_yield)+'\t'+str(bkg3_yield)+'\t'+str(sig4_yield)+'\t'+str(bkg4_yield)+'\t'+str(sig5_yield)+'\t'+str(bkg5_yield)+'\t'+str(sig6_yield)+'\t'+str(bkg6_yield)+'\t'+str(sig7_yield)+'\t'+str(bkg7_yield)+'\t'+str(sig8_yield)+'\t'+str(bkg8_yield)+'\n')
card.write('----------------------------------------------------------------------------\n')
card.write('bkg_syst\tlnN\t-\t'+str(bkg_syst+1)+'\t-\t'+str(bkg2_syst+1)+'\t-\t'+str(bkg3_syst+1)+'\t-\t'+str(bkg4_syst+1)+'\t-\t'+str(bkg5_syst+1)+'\t-\t'+str(bkg6_syst+1)+'\t-\t'+str(bkg7_syst+1)+'\t-\t'+str(bkg8_syst+1)+'\n')
#card.write('bkg_stat\tlnN\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\n')
#card.write('sig_syst\tlnN\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\n')
