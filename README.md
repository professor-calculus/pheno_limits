# pheno_limits

Example running:

first process a few files, toy yields are located in D5b_mchi_lambda800.txt
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
