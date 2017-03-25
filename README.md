# pheno limits

##New update, for Paul
limits_contour/paul contains an example mass scan (2D) with predicted yields.

There's a few scripts which then give you an output which can be plotted.

##Setting up combine:
First setup combine tool in new CMSSW environment:

```
setenv SCRAM_ARCH slc6_amd64_gcc481
cmsrel CMSSW_7_1_5 ### must be a 7_1_X release  >= 7_1_5;  (7.0.X and 7.2.X are NOT supported either)
cd CMSSW_7_1_5/src
cmsenv
git cms-addpkg FWCore/Version
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
git fetch origin
git checkout v5.0.4   # try v5.0.1 if any issues occur
scramv1 b clean; scramv1 b
```

##Now setup the pheno limit code:



```
git clone git@github.com:bpenning/ pheno_limits
cd pheno_limits
```

There are two versions, one in 'limits_simple', one in 'limits_scaled'. Each contains example for limits setting. In 'scaled' we take a result based on existing results and scale them to 20, 300 and 300/fb. In the 'simple' example just one set of inputs is taken, procssesd and plotted. Example below for the slightly more complicated limit, the other example is clear then.

The following example creates card files for limit setting from a list of yields, performs the limit setting and finally plots the result:

```source run_example.sh```

In Detail. First process a few files, toy yields are located in D5b_mchi_lambda800.txt
```
for model in D5b
do
  for lumi in 20 300 3000
  do
   python EFTlimits.py $model $lumi
  done
done
```

Then merge the output of comibine tool for each luminosity projection:
```
hadd -f D5b/combined_D5b_20fb.root D5b/combine_mchi*20fb.root
hadd -f D5b/combined_D5b_300fb.root D5b/combine_mchi*300fb.root
hadd -f D5b/combined_D5b_3000fb.root D5b/combine_mchi*3000fb.root
```

and plot
```
python plot4EFTs.py D5b/combined_D5b_20fb.root D5b/combined_D5b_300fb.root D5b/combined_D5b_3000fb.root"
```
Example output

![example output](./D5_multilumi.png?raw=true "example")




##Setting in simple plot:

In ``D5b/D5b_mchi.txt`` we have the yield for each signal sample 

```
cat D5b/D5b_mchi.txt
1.0 30446.6
10.0 25000
20.0 10000
```

cardmaker.py contains the yields for background and relative signal and background systematics:

```
bkg_yield=445631
bkg_stat=0.099
bkg_syst=0.068
sig_syst=0.114
```

Just adap these numbers and run 'run_example.sh' in an enviroment with the combine tool setup. 
