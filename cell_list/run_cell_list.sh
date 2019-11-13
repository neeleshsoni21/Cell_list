#Example run of the program with default input file. Or just run this file using the following command.
#bash run_cell_list.sh

#To run the software for only CA and NZ atoms
python ./src/main.py -f ./input/1QJA.pdb -o ./output/output_distance.txt --cutoff 8.0 --atomtypes "CA CB" --restypes "MET LYS"

