"""
Copyright (C) 2013 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>, <neeleshsoni03@gmail.com>
This file is part of celllist.

celllist is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

celllist is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with celllist.  If not, see <http://www.gnu.org/licenses/>.
"""'''
This routine calculates the distance between all the atoms in the cell_list variable
'''
import math
def calculate_distance(cell_list,cmesh,nghdict,cutoff):
    
    #get the total number of cells in each dircetion and the total numbers
    cxn=cmesh[3]
    cyn=cmesh[4]
    czn=cmesh[5]
    cmax=cxn*cyn*czn
    
    #Calculates the square of the cutoff
    square_cutoff=cutoff*cutoff;
    outline=""
    counter=0;
    #Iterate through all cells in the Mesh
    for i in range(0,cmax):
        #Get the coordinate set 1
        coord_set1=cell_list[i];
        #get the neighbors indexs for the current cell
        for idx in nghdict[i]:
            #Get the current coordinate set 2
            coord_set2=cell_list[idx];
            
            #For each atom in the coordinate sets 1,2 calculate the distance
            for coord1 in coord_set1:
                for coord2 in coord_set2:
                    #Calculate the square of the distance
                    square_distance=compute_distance(coord1,coord2)
                    #If square of the distance is less than the square of the cutoff distnace, then calculate the distance by taking the square root.
                    if (square_distance < square_cutoff):
                        distance=math.sqrt(square_distance)
                        distance = round(distance,3)
                        #Format the string to right in the output file
                        outline+=str(coord1[3])+":"+str(coord1[4])+":"+str(coord1[5])+":"+str(coord1[6])+":"+str(coord1[7])+"\t"+str(coord2[3])+":"+str(coord2[4])+":"+str(coord2[5])+":"+str(coord2[6])+":"+str(coord2[7])+"\t"+str(distance)+"\n";
                
    #return the output line
    return outline


'''
This routione calculates the distance between any two coordinates
'''
def compute_distance(coord1,coord2):
    return ((coord1[0]-coord2[0])*(coord1[0]-coord2[0]) + (coord1[1]-coord2[1])*(coord1[1]-coord2[1]) + (coord1[2]-coord2[2])*(coord1[2]-coord2[2]))
    

