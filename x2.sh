for model in D5b
do
  for lumi in 20 300 3000
  do
    python EFTlimits.py $model $lumi
  done
done
hadd -f D5b/combined_D5b_20fb.root D5b/combine_mchi*20fb.root
hadd -f D5b/combined_D5b_300fb.root D5b/combine_mchi*300fb.root
hadd -f D5b/combined_D5b_3000fb.root D5b/combine_mchi*3000fb.root
rm D5b/combine_*.root D5b/ext_vbfhinv_mchi*.txt
echo "python plot4EFTs.py D5b/combined_D5b_20fb.root"