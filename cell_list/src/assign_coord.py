"""
Copyright (C) 2013 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>, <neeleshsoni03@gmail.com>
This file is part of celllist.

celllist is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

celllist is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with celllist.  If not, see <http://www.gnu.org/licenses/>.
"""'''
This routine assigns each atom in the 3D mesh. This is done through binary search on the x,y and z arrays of mesh points
'''

#from binary_search import bsearch
def assign_atomlist_to_mesh(mesh,atom_props,cell_lst):
    
    #get the total number of mesh points in each direction#
    xn=mesh[3];
    yn=mesh[4];
    zn=mesh[5];

    loc=mesh[7]
    origin=mesh[6]

    #print loc,origin
    #storing coordinates in x-y-z major. ie. z coordinates first then y then x
    for c in atom_props:
        #Do a binary search of current x,y,z coordinates in the corresponding x,y,z array of points#
        #ix=bsearch(c[0],mesh[0])
        #iy=bsearch(c[1],mesh[1])
        #iz=bsearch(c[2],mesh[2])
        
        ix=int((c[0]-origin[0])/loc)
        iy=int((c[1]-origin[1])/loc)
        iz=int((c[2]-origin[2])/loc)
        
        #print (xn-ix),(yn-iy), (zn-iz), c[6], ix, iy, iz
        if ((ix < 0) | (ix >= xn)):
            continue;
        if ((iy < 0) | (iy >= yn)):
            continue;
        if ((iz < 0) | (iz >= zn)):
            continue;
        #z-y-x major
        index=zn*yn*ix + iy*zn +iz;
        #print index
        #append the mesh cell with coordinate & its properties
        cell_lst[index].append(c);
        #Return cell list
    return cell_lst
