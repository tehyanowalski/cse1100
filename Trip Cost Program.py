# Tehya Nowalski
# Lab 1:00 pm
# September 2020

# Trip Cost Program
#
# The Trip Cost Program developed by Tehya Nowalski attempts to estimate the
# distance your car travels, along with
# its cost per gallon, and the miles per gallon.

# display welcome

print ('Created by Tehya Nowalski')

print ('Welcome to the Trip Cost Program!')
print ('The Trip Cost Program attempts to estimate the distance your car travels,')
print ('along with its cost per gallon, and the miles per gallon.')
print ()

# get user input
# assign values as variables

DistanceTraveled = float(input('How much distance have you traveled?: '))
MilesPerGallon = float(input('How many miles per gallon did you get?: '))
CostPerGallon = float(input('How much does gas cost per gallon?: '))

# calculate results

GallonsUsed = DistanceTraveled / MilesPerGallon
TripCost = GallonsUsed * CostPerGallon

#display result

print()
print('Based on the values entered...')
print('Your trip cost is: $', format(TripCost,'.2f'))
