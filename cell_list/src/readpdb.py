"""
Copyright (C) 2013 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>, <neelrocks4@gmail.com>
This file is part of celllist.

celllist is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

celllist is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with celllist.  If not, see <http://www.gnu.org/licenses/>.
"""
'''
This routine reads the pdb file given as input and then return the coordinates and corresponding atom identities.
'''
import sys
def parse_pdb(inf,atomtypes,restypes):
    
    #read the pdb file#
    lines=inf.readlines();
    
    #initializing the maximum variable with negative infinity and  minimum value as positive infinity
    minx=10000000.0
    maxx=-10000000.0
    miny=10000000.0
    maxy=-10000000.0
    minz=10000000.0
    maxz=-10000000.0
    
    #Initiallizing the atom_props variable
    atom_props=[]
    
    #Set flag for type of atom and residue types
    flag1=False;
    flag2=False;
    if atomtypes[0]=="ALL":
        flag1=True;
    if restypes[0]=="ALL":
        flag2=True;
    
    #Create a dictionary for type of code to run, Case 1 will return True always, 
    #Case 2 will check for the type and then return
    mycode={True:case1,False:case2}

    #Iterating through each line
    for l in lines:
        #if line starts with 'ATOM' identifier, then continue
        if ((l[0:4]=='ATOM')|(l[0:6]=='HETATM')):

            #Getting the coordinates from pdb files
            xc=float(l[30:38]);
            yc=float(l[38:46]);
            zc=float(l[46:54]);
            
            #Getting the corresponding atom properties. Atom name, residue name,number, chain id
            atom_type=l[12:16].strip();
            res_name=l[17:20].strip();
            res_num=l[22:26].strip();
            chain_num=l[21:22].strip();

            #check if current atom to consider or not
            code=mycode[flag1]
            atomflag=code(atom_type,atomtypes)
            #print atom_type,atomtypes,atomflag
            
            #check if current residue to consider or not
            code=mycode[flag2]
            resflag=code(res_name,restypes)
            
            
            #If both atom and residue are to be considered then execute
            if (atomflag & resflag) == True:

                #Getting the max, min of x direction
                if minx>xc:
                    minx=xc;
                if maxx<xc:
                    maxx=xc;
                
                #Getting the max, min of y direction
                if miny>yc:
                    miny=yc;
                if maxy<yc:
                    maxy=yc;
                
                #Getting the max, min of z direction
                if minz>zc:
                    minz=zc;
                if maxz<zc:
                    maxz=zc;
                
                #Append the atom_coord with each atom properties
                atom_props.append([xc,yc,zc,atom_type,res_name,res_num,chain_num]);
    
    if len(atom_props)==0:
        print ("Error: Atoms not found in the list.")
        print ("Make sure your PDB file is read properly.")
        sys.exit(0)
    #Return            
    return minx,maxx,miny,maxy,minz,maxz,atom_props


#Case 1 code which will return true everytime
def case1(item_type,listtypes):
    return True;

#Case 2 code which will return true if itemtype exist in list type
def case2(item_type,listtypes):
    if item_type in listtypes:
        return True
    else:
        return False
    return False