./makegrid_MHT_combined_exp.py -i P1/MHT_exp/2b_130.txt -j P1/MHT_exp/2b_175.txt -j2 P1/MHT_exp/2b_225.txt -j3 P1/MHT_exp/2b_275.txt -j4 P1/MHT_exp/2b_325.txt -j5 P1/MHT_exp/2b_375.txt -j6 P1/MHT_exp/2b_425.txt -j7 P1/MHT_exp/2b_475.txt -j8 P1/MHT_exp/2b_525.txt -j9 P1/MHT_exp/2b_575.txt -j10 P1/MHT_exp/2b_650.txt -j11 P1/MHT_exp/2b_800.txt -j12 P1/MHT_exp/ge3b_130.txt -j13 P1/MHT_exp/ge3b_200.txt -j14 P1/MHT_exp/ge3b_275.txt -j15 P1/MHT_exp/ge3b_325.txt -j16 P1/MHT_exp/ge3b_375.txt -j17 P1/MHT_exp/ge3b_425.txt -j18 P1/MHT_exp/ge3b_525.txt -j19 P1/MHT_exp/ge3b_575.txt 
./extract_values2.py P1/MHT_exp/grid_info2.txt
mv output2.out /users/at1062/limits_exp/P1_MHT_combined_exp.out

./makegrid_2_2fb_2b_exp.py -i P1/2b_exp/yields.txt
./extract_values2.py P1/2b_exp/grid_info2.txt
mv output2.out /users/at1062/limits_exp/output_P1_2b_exp.out

./makegrid_2_2fb_ge3b_exp.py -i P1/ge3b_exp/yields.txt
./extract_values2.py P1/ge3b_exp/grid_info2.txt
mv output2.out /users/at1062/limits_exp/output_P1_ge3b_exp.out

./makegrid_2_2fb_combined_exp.py -i P1/combined_exp/yields2b.txt -j P1/combined_exp/yieldsge3b.txt
./extract_values2.py P1/combined_exp/grid_info2.txt
mv output2.out /users/at1062/limits_exp/output_P1_combined_exp.out
