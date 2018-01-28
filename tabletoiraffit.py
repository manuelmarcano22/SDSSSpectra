#!/usr/bin/env python

from astropy.io import fits
from pyraf import iraf
import os
import sys

#filename = 'spec-0266-51602-0051.fits'
filename = sys.argv[1]


#import fits
ob = fits.open(filename)
#Get data and save wavelenft in x, and flux on y
dataob = ob[1].data
x = 10**(dataob['loglam'])
y = dataob['model']

#save to a .txt file
namenewfits = '{name}.txt'.format(name=filename.split('.')[0])
with open(namenewfits,'w') as file:
	for i in zip(x,y):
		file.write('{}\t{}\n'.format(i[0],i[1]))
#Create fits file from text file interpolation. 
iraffitsname = 'iraf'+filename.split('.')[0]
if os.path.exists(iraffitsname+'.fits'):
	os.remove(iraffitsname+'.fits')
	
iraf.noao.onedspec()
iraf.dataio()
iraf.rspectext(namenewfits,iraffitsname,dtype='interp')




