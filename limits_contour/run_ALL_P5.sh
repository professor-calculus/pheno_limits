./makegrid_MHT_combined.py -i P5/MHT/2b_130.txt -j P5/MHT/2b_175.txt -j2 P5/MHT/2b_225.txt -j3 P5/MHT/2b_275.txt -j4 P5/MHT/2b_325.txt -j5 P5/MHT/2b_375.txt -j6 P5/MHT/2b_425.txt -j7 P5/MHT/2b_475.txt -j8 P5/MHT/2b_525.txt -j9 P5/MHT/2b_575.txt -j10 P5/MHT/2b_650.txt -j11 P5/MHT/2b_800.txt -j12 P5/MHT/ge3b_130.txt -j13 P5/MHT/ge3b_200.txt -j14 P5/MHT/ge3b_275.txt -j15 P5/MHT/ge3b_325.txt -j16 P5/MHT/ge3b_375.txt -j17 P5/MHT/ge3b_425.txt -j18 P5/MHT/ge3b_525.txt -j19 P5/MHT/ge3b_575.txt 
./extract_values.py P5/MHT/grid_info.txt
mv output.out /users/at1062/limits/P5_MHT_combined.out

./makegrid_2_2fb_2b.py -i P5/2b/yields.txt
./extract_values.py P5/2b/grid_info.txt
mv output.out /users/at1062/limits/output_P5_2b_obs.out

./makegrid_2_2fb_ge3b.py -i P5/ge3b/yields.txt
./extract_values.py P5/ge3b/grid_info.txt
mv output.out /users/at1062/limits/output_P5_ge3b_obs.out

./makegrid_2_2fb_combined.py -i P5/combined/yields2b.txt -j P5/combined/yieldsge3b.txt
./extract_values.py P5/combined/grid_info.txt
mv output.out /users/at1062/limits/output_P5_combined_obs.out
