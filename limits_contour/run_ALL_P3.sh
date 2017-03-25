./makegrid_MHT_combined.py -i P3/MHT/2b_130.txt -j P3/MHT/2b_175.txt -j2 P3/MHT/2b_225.txt -j3 P3/MHT/2b_275.txt -j4 P3/MHT/2b_325.txt -j5 P3/MHT/2b_375.txt -j6 P3/MHT/2b_425.txt -j7 P3/MHT/2b_475.txt -j8 P3/MHT/2b_525.txt -j9 P3/MHT/2b_575.txt -j10 P3/MHT/2b_650.txt -j11 P3/MHT/2b_800.txt -j12 P3/MHT/ge3b_130.txt -j13 P3/MHT/ge3b_200.txt -j14 P3/MHT/ge3b_275.txt -j15 P3/MHT/ge3b_325.txt -j16 P3/MHT/ge3b_375.txt -j17 P3/MHT/ge3b_425.txt -j18 P3/MHT/ge3b_525.txt -j19 P3/MHT/ge3b_575.txt 
./extract_values.py P3/MHT/grid_info.txt
mv output.out /users/at1062/limits/P3_MHT_combined.out

./makegrid_2_2fb_2b.py -i P3/2b/yields.txt
./extract_values.py P3/2b/grid_info.txt
mv output.out /users/at1062/limits/output_P3_2b_obs.out

./makegrid_2_2fb_ge3b.py -i P3/ge3b/yields.txt
./extract_values.py P3/ge3b/grid_info.txt
mv output.out /users/at1062/limits/output_P3_ge3b_obs.out

./makegrid_2_2fb_combined.py -i P3/combined/yields2b.txt -j P3/combined/yieldsge3b.txt
./extract_values.py P3/combined/grid_info.txt
mv output.out /users/at1062/limits/output_P3_combined_obs.out
