"""
show to run:
python EFTlimits.py D5b

takes in a model and produces a hadded tree ready for input to the plotting script
"""
import sys
import os
import numpy as np

# get the model and lumi
model = sys.argv[1]

# import the yields script
infile = open(model+"/"+model+"_mchi.txt")
lines = infile.readlines()

treestring = ""
for line in lines:
    mchi = line.split()[0]
    val = line.split()[1]
    os.system("./cardmaker.py -s "+val+" -n mchi"+mchi+" --systlumiscale True")
    os.system("combine -M Asymptotic -m "+mchi+" ext_vbfhinv_mchi"+mchi+"_14TeV.txt")
    os.system("mv ext_vbfhinv_mchi"+mchi+"_14TeV.txt "+model+"/")
    os.system("mv higgsCombineTest.Asymptotic* "+model+"/combine_mchi"+mchi+".root")
    treestring = treestring+model+"/combine_mchi"+mchi+".root "

print("hadd -f "+model+"/combined_"+model+".root "+treestring)
os.system("hadd -f "+model+"/combined_"+model+".root "+treestring)
#os.system("hadd -f "+model+"/combined_"+model+"_.root "+treestring)
#os.system("rm roostats-*")
#os.system("rm "+model+"/combine_*")
#os.system("rm "+model+"/ext**")


