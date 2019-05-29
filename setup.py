"""
Copyright (C) 2013 Neelesh Soni <neelesh.soni@alumni.iiserpune.ac.in>, <neelrocks4@gmail.com>
This file is part of celllist.

celllist is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

celllist is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with celllist.  If not, see <http://www.gnu.org/licenses/>.
"""
from setuptools import setup

setup(name='cell_list_v4.3',
      version='4.3',
      description='Cell_list code to determine the distances between neighbors',
      url='http://192.168.8.252:8080/Neelesh_cell_list',
      author='Neelesh Soni',
      author_email='neelrocks4@gmail.com',
      license='LGPL',
      packages=['cell_list'],
      package_data={'cell_list': ['input/*.pdb','output/*.*',],},
      include_package_data=True,
      install_requires=[""],
      zip_safe=False)
