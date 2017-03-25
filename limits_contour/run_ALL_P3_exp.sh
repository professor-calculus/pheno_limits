./makegrid_MHT_combined_exp.py -i P3/MHT_exp/2b_130.txt -j P3/MHT_exp/2b_175.txt -j2 P3/MHT_exp/2b_225.txt -j3 P3/MHT_exp/2b_275.txt -j4 P3/MHT_exp/2b_325.txt -j5 P3/MHT_exp/2b_375.txt -j6 P3/MHT_exp/2b_425.txt -j7 P3/MHT_exp/2b_475.txt -j8 P3/MHT_exp/2b_525.txt -j9 P3/MHT_exp/2b_575.txt -j10 P3/MHT_exp/2b_650.txt -j11 P3/MHT_exp/2b_800.txt -j12 P3/MHT_exp/ge3b_130.txt -j13 P3/MHT_exp/ge3b_200.txt -j14 P3/MHT_exp/ge3b_275.txt -j15 P3/MHT_exp/ge3b_325.txt -j16 P3/MHT_exp/ge3b_375.txt -j17 P3/MHT_exp/ge3b_425.txt -j18 P3/MHT_exp/ge3b_525.txt -j19 P3/MHT_exp/ge3b_575.txt 
./extract_values2.py P3/MHT_exp/grid_info2.txt
mv output2.out /users/at1062/limits_exp/P3_MHT_combined_exp.out

./makegrid_2_2fb_2b_exp.py -i P3/2b_exp/yields.txt
./extract_values2.py P3/2b_exp/grid_info2.txt
mv output2.out /users/at1062/limits_exp/output_P3_2b_exp.out

./makegrid_2_2fb_ge3b_exp.py -i P3/ge3b_exp/yields.txt
./extract_values2.py P3/ge3b_exp/grid_info2.txt
mv output2.out /users/at1062/limits_exp/output_P3_ge3b_exp.out

./makegrid_2_2fb_combined_exp.py -i P3/combined_exp/yields2b.txt -j P3/combined_exp/yieldsge3b.txt
./extract_values2.py P3/combined_exp/grid_info2.txt
mv output2.out /users/at1062/limits_exp/output_P3_combined_exp.out
