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
parser.add_argument('-t8','--sig9_yield_19_2fb',required=True)
parser.add_argument('-t9','--sig10_yield_19_2fb',required=True)
parser.add_argument('-t10','--sig11_yield_19_2fb',required=True)
parser.add_argument('-t11','--sig12_yield_19_2fb',required=True)
parser.add_argument('-t12','--sig13_yield_19_2fb',required=True)
parser.add_argument('-t13','--sig14_yield_19_2fb',required=True)
parser.add_argument('-t14','--sig15_yield_19_2fb',required=True)
parser.add_argument('-t15','--sig16_yield_19_2fb',required=True)
parser.add_argument('-t16','--sig17_yield_19_2fb',required=True)
parser.add_argument('-t17','--sig18_yield_19_2fb',required=True)
parser.add_argument('-t18','--sig19_yield_19_2fb',required=True)
parser.add_argument('-t19','--sig20_yield_19_2fb',required=True)
#parser.add_argument('-l','--targetlumi',required=True)
#parser.add_argument('--systlumiscale',default=False)
parser.add_argument('-n','--name',default='125')
parser.add_argument('--sqrts',default=13)
parser.add_argument('-b','--batchmode',default=False)
args=parser.parse_args()

#2b
data_yield=2
bkg_yield=0.718
sig_yield=args.sig_yield_19_2fb
bkg_syst=0.331/0.718

data2_yield=0
bkg2_yield=0.958
sig2_yield=args.sig2_yield_19_2fb
bkg2_syst=0.347/0.958

data3_yield=2
bkg3_yield=1.26
sig3_yield=args.sig3_yield_19_2fb
bkg3_syst=0.401/1.26

data4_yield=5
bkg4_yield=1.38
sig4_yield=args.sig4_yield_19_2fb
bkg4_syst=0.444/1.38

data5_yield=3
bkg5_yield=0.821
sig5_yield=args.sig5_yield_19_2fb
bkg5_syst=0.292/0.821

data6_yield=2
bkg6_yield=0.755
sig6_yield=args.sig6_yield_19_2fb
bkg6_syst=0.294/0.755

data7_yield=1
bkg7_yield=0.314
sig7_yield=args.sig7_yield_19_2fb
bkg7_syst=0.126/0.314

data8_yield=1
bkg8_yield=0.0619
sig8_yield=args.sig8_yield_19_2fb
bkg8_syst=0.0311/0.0619

data9_yield=0
bkg9_yield=0.147
sig9_yield=args.sig9_yield_19_2fb
bkg9_syst=0.067/0.147

data10_yield=0
bkg10_yield=0.161
sig10_yield=args.sig10_yield_19_2fb
bkg10_syst=0.0853/0.161

data11_yield=0
bkg11_yield=0.436
sig11_yield=args.sig11_yield_19_2fb
bkg11_syst=0.246/0.436

data12_yield=0
bkg12_yield=0.146
sig12_yield=args.sig12_yield_19_2fb
bkg12_syst=0.0757/0.146

#ge3b
data13_yield=0
bkg13_yield=0.0989
sig13_yield=args.sig13_yield_19_2fb
bkg13_syst=0.0847/0.0989

data14_yield=1
bkg14_yield=0.194
sig14_yield=args.sig14_yield_19_2fb
bkg14_syst=0.104/0.194

data15_yield=0
bkg15_yield=0.18
sig15_yield=args.sig15_yield_19_2fb
bkg15_syst=0.0964/0.18

data16_yield=1
bkg16_yield=0.202
sig16_yield=args.sig16_yield_19_2fb
bkg16_syst=0.105/0.202

data17_yield=1
bkg17_yield=0.0961
sig17_yield=args.sig17_yield_19_2fb
bkg17_syst=0.0587/0.0961

data18_yield=0
bkg18_yield=0.0427
sig18_yield=args.sig18_yield_19_2fb
bkg18_syst=0.0305/0.0427

data19_yield=0
bkg19_yield=0.00615
sig19_yield=args.sig19_yield_19_2fb
bkg19_syst=0.0061/0.00615

data20_yield=0
bkg20_yield=0.0808
sig20_yield=args.sig20_yield_19_2fb
bkg20_syst=0.0521/0.0808


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
card.write('imax 20 number of bins\n')
card.write('jmax * number of backgrounds\n')
card.write('kmax * number of nuisance parameters (sources of systematic uncertainties)\n')
#card.write('shapes * * FAKE\n')
card.write('bin\tch1\tch2\tch3\tch4\tch5\tch6\tch7\tch8\tch9\tch10\tch11\tch12\tch13\tch14\tch15\tch16\tch17\tch18\tch19\tch20\n')
card.write('observation '+str(data_yield)+' '+str(data2_yield)+' '+str(data3_yield)+' '+str(data4_yield)+' '+str(data5_yield)+' '+str(data6_yield)+' '+str(data7_yield)+' '+str(data8_yield)+' '+str(data9_yield)+' '+str(data10_yield)+' '+str(data11_yield)+' '+str(data12_yield)+' '+str(data13_yield)+' '+str(data14_yield)+' '+str(data15_yield)+' '+str(data16_yield)+' '+str(data17_yield)+' '+str(data18_yield)+' '+str(data19_yield)+' '+str(data20_yield)+'\n')#set observation equal to data_yield or expected background
card.write('----------------------------------------------------------------------------\n')
card.write('bin\t\t\tch1\tch1\tch2\tch2\tch3\tch3\tch4\tch4\tch5\tch5\tch6\tch6\tch7\tch7\tch8\tch8\tch9\tch9\tch10\tch10\tch11\tch11\tch12\tch12\tch13\tch13\tch14\tch14\tch15\tch15\tch16\tch16\tch17\tch17\tch18\tch18\tch19\tch19\tch20\tch20\n')
card.write('process\t\t\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\tsig\tbkg\n')
card.write('process\t\t\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\t0\t1\n')
card.write('rate\t\t\t'+str(sig_yield)+'\t'+str(bkg_yield)+'\t'+str(sig2_yield)+'\t'+str(bkg2_yield)+'\t'+str(sig3_yield)+'\t'+str(bkg3_yield)+'\t'+str(sig4_yield)+'\t'+str(bkg4_yield)+'\t'+str(sig5_yield)+'\t'+str(bkg5_yield)+'\t'+str(sig6_yield)+'\t'+str(bkg6_yield)+'\t'+str(sig7_yield)+'\t'+str(bkg7_yield)+'\t'+str(sig8_yield)+'\t'+str(bkg8_yield)+'\t'+str(sig9_yield)+'\t'+str(bkg9_yield)+'\t'+str(sig10_yield)+'\t'+str(bkg10_yield)+'\t'+str(sig11_yield)+'\t'+str(bkg11_yield)+'\t'+str(sig12_yield)+'\t'+str(bkg12_yield)+'\t'+str(sig13_yield)+'\t'+str(bkg13_yield)+'\t'+str(sig14_yield)+'\t'+str(bkg14_yield)+'\t'+str(sig15_yield)+'\t'+str(bkg15_yield)+'\t'+str(sig16_yield)+'\t'+str(bkg16_yield)+'\t'+str(sig17_yield)+'\t'+str(bkg17_yield)+'\t'+str(sig18_yield)+'\t'+str(bkg18_yield)+'\t'+str(sig19_yield)+'\t'+str(bkg19_yield)+'\t'+str(sig20_yield)+'\t'+str(bkg20_yield)+'\n')
card.write('----------------------------------------------------------------------------\n')
card.write('bkg_syst\tlnN\t-\t'+str(bkg_syst+1)+'\t-\t'+str(bkg2_syst+1)+'\t-\t'+str(bkg3_syst+1)+'\t-\t'+str(bkg4_syst+1)+'\t-\t'+str(bkg5_syst+1)+'\t-\t'+str(bkg6_syst+1)+'\t-\t'+str(bkg7_syst+1)+'\t-\t'+str(bkg8_syst+1)+'\t-\t'+str(bkg9_syst+1)+'\t-\t'+str(bkg10_syst+1)+'\t-\t'+str(bkg11_syst+1)+'\t-\t'+str(bkg12_syst+1)+'\t-\t'+str(bkg13_syst+1)+'\t-\t'+str(bkg14_syst+1)+'\t-\t'+str(bkg15_syst+1)+'\t-\t'+str(bkg16_syst+1)+'\t-\t'+str(bkg17_syst+1)+'\t-\t'+str(bkg18_syst+1)+'\t-\t'+str(bkg19_syst+1)+'\t-\t'+str(bkg20_syst+1)+'\n')
#card.write('bkg_stat\tlnN\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\n')
#card.write('sig_syst\tlnN\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\t0.\t-\n')
