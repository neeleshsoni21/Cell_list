"""
Copyright (C) 2013 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>, <neeleshsoni03@gmail.com>
This file is part of celllist.

celllist is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

celllist is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with celllist.  If not, see <http://www.gnu.org/licenses/>.
"""'''
This function add the options to the interpreter from the command line

'''
def addoptions():
    
    import optparse
    
    parser = optparse.OptionParser()
    
    #Adding the options
    parser.add_option('-f', type="string", help='Input pdb file for distance calculation. For Example: -f ./input/1QJA.pdb' )
    parser.add_option('-o', type="string", help='Output file for storing the calculated distances. For example: -o ./output/distances.txt' )
    parser.add_option('--cutoff', type="float", help='Cutoff for the distance calculation');
    parser.add_option('--atomtypes', type="string", help='Atomtypes to consider for the distance calculations, for default type ALL');
    parser.add_option('--restypes', type="string", help='Residuetypes to consider for the distance calculations, for default type ALL');
    parser.add_option('--refchain', type="string", help='Reference chain to consider for distance calculations, for default type ALL');

    args, remainder = parser.parse_args()
    
    #Check if number of arguments are correct or not.
    if (args.f is None) or (args.o is None):
        parser.error("Not enough number of arguments\nUse -h for options")
    
    #Assigning the command line options to variables
    fname = args.f;
    oname = args.o;
    cutoff= args.cutoff;
    atomtypes= args.atomtypes.split(' ');
    restypes= args.restypes.split(' ');
    refchain= args.refchain.split(' ');

    #return the input and output files
    return fname,oname,cutoff,atomtypes,restypes,refchain

