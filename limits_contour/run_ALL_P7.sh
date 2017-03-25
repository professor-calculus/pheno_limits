./makegrid_MHT_combined.py -i P7/MHT/2b_130.txt -j P7/MHT/2b_175.txt -j2 P7/MHT/2b_225.txt -j3 P7/MHT/2b_275.txt -j4 P7/MHT/2b_325.txt -j5 P7/MHT/2b_375.txt -j6 P7/MHT/2b_425.txt -j7 P7/MHT/2b_475.txt -j8 P7/MHT/2b_525.txt -j9 P7/MHT/2b_575.txt -j10 P7/MHT/2b_650.txt -j11 P7/MHT/2b_800.txt -j12 P7/MHT/ge3b_130.txt -j13 P7/MHT/ge3b_200.txt -j14 P7/MHT/ge3b_275.txt -j15 P7/MHT/ge3b_325.txt -j16 P7/MHT/ge3b_375.txt -j17 P7/MHT/ge3b_425.txt -j18 P7/MHT/ge3b_525.txt -j19 P7/MHT/ge3b_575.txt 
./extract_values.py P7/MHT/grid_info.txt
mv output.out /users/at1062/limits/P7_MHT_combined.out

./makegrid_2_2fb_2b.py -i P7/2b/yields.txt
./extract_values.py P7/2b/grid_info.txt
mv output.out /users/at1062/limits/output_P7_2b_obs.out

./makegrid_2_2fb_ge3b.py -i P7/ge3b/yields.txt
./extract_values.py P7/ge3b/grid_info.txt
mv output.out /users/at1062/limits/output_P7_ge3b_obs.out

./makegrid_2_2fb_combined.py -i P7/combined/yields2b.txt -j P7/combined/yieldsge3b.txt
./extract_values.py P7/combined/grid_info.txt
mv output.out /users/at1062/limits/output_P7_combined_obs.out
