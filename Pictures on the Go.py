# Tehya Nowalski
# Lab 1:00 pm
# October 2020

# Pictures on the Go
#
# This program calculates how many images can be stored on a 
# particular size USB (flash) drive. The user must enter the size
# of the USB in gigabytes (GB). The number of images that can be stored
# are then calculated for GIF, JPEG, PNG, and TIFF image file formats.
#
# Where
#   Resolution ... 12 MP (4000 * 3000)
#   GB ... 1,000,000,000 bytes
#   USB ... user input of how many gigabytes their USB holds
# Then
#   Resolution * Color Depth // Compression = size
#   GB * USB // size = how many images can be stored
#

# display welcome

print ('Created by Tehya Nowalski')

print ('Welcome to Pictures on the Go!')
print ('This program will determine how many images can be stored on a')
print ('USB (flash) drive. The number of images that can be stored are')
print ('calculated for GIF, JPEG, PNG, and TIFF image file formats.')
print ('All images have a resolution of 12 MP (4000 * 3000).')
print ('The input must be the size of the USB in gigabytes (GB).')
print ()
       
# get the size of the USB by user
# assign values as variables

USB = float(input('Please enter the Flash Drive size in Gigabytes: '))
print ()
print ('Your Flash Drive can store: ')
       
# calculate results

Resolution = 4000 * 3000
GB = 1000000000

GIFsize = Resolution // 5
JPEGsize = Resolution * 3 // 10
PNGsize = Resolution * 3 // 8
TIFFsize = Resolution * 6

GIF = GB // GIFsize
JPEG = GB // JPEGsize
PNG = GB // PNGsize
TIFF = GB // TIFFsize

# display results

print (format(GIF, '.0f'), 'images in GIF format.')
print (format(JPEG, '.0f'), 'images in JPEG format.')
print (format(PNG, '.0f'), 'images in PNG format.')
print (format(TIFF, '.0f'), 'images in TIFF format.')
