# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

with open('README.rst') as file:
    readme = file.read()

with open("VERSION.rst") as f:
    version = f.readline()
    f.close()
        
setup(
    name        =   'geonum',
    version     =   version,
    author      =   'Jonas Gliss',
    author_email=   'jg@nilu.no',
    license     =   'GPLv3',
    url         =   'https://github.com/jgliss/geonum',
    package_dir =   {'geonum'     :   'geonum'},
    packages    =   find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data    =   True,  
    install_requires        =   ["scipy",
                                 "LatLon",
                                 "srtm.py",
                                 "sphinxcontrib-images"],
    extras_require={
        'cv2':  ["opencv-python>=2.4.11"],
        'netCDF4': ["docutils>=0.3"]},

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later' 
        '(GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.,
        'Programming Language :: Python :: 2.7',
    ],
    
    #dependency_links    =   ["https://github.com/tkrajina/srtm.py/archive/v.0.3.1.zip#egg=srtm"],
    #package_data={'geonum':['suppl/*.dat']},
    description = 'Toolbox for 3D geonumerical calculations',
    long_description = readme,
    
    #requires=['python (>= 2.7)', 'numpy', 'astropy'],
)