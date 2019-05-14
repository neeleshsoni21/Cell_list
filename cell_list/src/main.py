"""
Copyright (C) 2013 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>, <neelrocks4@gmail.com>
This file is part of celllist.

celllist is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

celllist is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with celllist.  If not, see <http://www.gnu.org/licenses/>.
"""'''
This is the main function. 
The routine will calculate the distance between all atoms in the input pdb file. 
Use -h option in the command line for giving the arguments to the program

'''
import sys

def run_cell_list(arguments):
    
    from readpdb import parse_pdb
    from mesh import create_mesh
    from assign_coord import assign_atomlist_to_mesh
    from assign_neighbor import assign_ngh
    from calculate_distance_matrix import calculate_distance

    #Getting the input file name#
    input_file=arguments[0];
    
    #Open the input file for parsing.#
    inf2=open(input_file,'r');
    
    print "Reading file: ",input_file

    #parse_pdb function returns the details of all atoms in the pdb file with maximum and minimum value of coordinates in each direction. All these values gets stored in the 'param' list#
    param=parse_pdb(inf2,arguments[3],arguments[4],arguments[5]);
    
    #close the file#
    inf2.close();
    
    #Set the distance cutoff#
    cutoff=float(arguments[2]);
    
    #Set the coarse mesh cell length in angstrom#
    cmesh_len=cutoff;
    
    
    #function 'create_mesh' creates a 3D mesh such that all atoms should be contained within this mesh. Extra 'cutoff' length is added in each direction for boundary cells#
    cmesh=create_mesh(param,cmesh_len,cutoff);
    
    
    #getting the all atom coordinates and their identities like atom type, residue name, residue number and chain identifier. All this are stored int he 6th element of param list#
    atom_props=param[6];
    
    
    #Getting the number of total number cell in the mesh#
    totcell=cmesh[3]*cmesh[4]*cmesh[5];
    
    
    #initializing the cell_list variable. This stores the list of all atoms in each cell of the mesh#
    cell_list=[ [] for n in range(0,totcell) ]
    
    
    #Assign the atoms in each cell of the mesh and store them in cell_list#
    cell_list=assign_atomlist_to_mesh(cmesh,atom_props,cell_list);
    
    
    #get the neighbors of each cell in the mesh and store them in the neighbor dictionary "nghdict" #
    ngh_dict=assign_ngh(cmesh);
    
    
    print "Calculating distances...\n"
    #Calculate the dictance of all the atoms that are withion cutoff distance. This function stores the distances with atom identities in the outline string.#
    outline=calculate_distance(cell_list,cmesh,ngh_dict,cutoff,arguments[5])
    
    
    #Getting the output file name#
    output_file=arguments[1];
    
    print "Writing the output file...\n"
    
    #Open the output file for writing the distances#
    fname=output_file
    outf=open(fname,'w');
    #Write the outline variable to the file#
    outf.writelines(outline);
    outf.close();

    return outline

def cell_list(inputfile=sys.path[-1]+'/input/1QJA.pdb', 
    outputfile=sys.path[-1]+'/output/output_distance.txt', 
    cutoff=8.0, atomtypes='CA', 
    residuetypes='ALL', refchain='ALL'):
    
    import time
    
    #Getting the start time#
    start_time=time.time()
    
    #Create argument list
    arguments=[inputfile,outputfile,float(cutoff),atomtypes.split(' '),residuetypes.split(' '),refchain.split(' ')]
    
    #Execute Cell_list function
    outlines=run_cell_list(arguments);
    
    #Get the total time elapsed#
    print 'Time elapsed = ', time.time() - start_time, 's'
    
    return outlines

def main():
    #Importing modules from the current directory#
    import sys
    import time
    from addoptions import addoptions
    
    #Getting the start time#
    start_time=time.time()
    
    #Parsing the inputs from the command line#
    arguments=addoptions()
    
    #Execute Cell_list function
    run_cell_list(arguments);

    #Get the total time elapsed#
    print 'Time elapsed = ', time.time() - start_time, 's'
    
    return
  

#execute the main function
if __name__ == "__main__":
    main()

