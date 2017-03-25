# Hey Paul, here's a quick example using the combined limits code.
# For this we'll just use one measurement bin, with one bkg prediction.
# We can then compare these with the predicted yields for each mass point
# in our signal scan.
./makegrid_paul.py -i paul/yields.txt
./extract_values.py paul/grid_info.txt > output_paul.txt
