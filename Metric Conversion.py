# Tehya Nowalski
# 1:00 pm
# October 2020
#
# The Metric Conversion program allows user to convert
# pounds to grams, inches to centimeters, and kilometers to miles.
# This conversion is also allowed both ways.
#
# Where
#   I ... Inches
#   C ... Centimeters
#   O ... Ounces
#   G ... Grams
#   K ... Kilometers
#   M ... Miles
# Then
#   O to G = unit * 28.3495231
#   G to O = unit / 28.3495231
#   I to C = unit * 2.54
#   C to I = unit / 2.54
#   M to K = unit * 1.609344
#   K to M = unit / 1.609344
#

# display welcome

print ('Created by Tehya Nowalski')
print()
print ('Metric Conversion will convert Inches/Centimeters,')
print ('Ounces/Grams, and Kilometers/Miles in either way that is entered.')
print()
print ('Enter I or C to convert from Inches or Centimeters.')
print ('Enter O or G to convert from Ounces or Grams.')
print ('Enter M or K to convert from Miles or Kilometers.')
print()

# user inputs what they want to convert
# assign values as variables
# initialize variables

terminate = False

while terminate == False:
    type = input('Enter a selection: ')
    type = type.upper();
    print()

    while type != 'I' and type != 'C' and type != 'O' and type != 'G' and type != 'M' and type != 'K':
        type = input('Please enter an I, C, O, G, M, or K: ')
        print()
    
    unit = int(input('Enter a unit to convert: '))
    print()

    # determine choice of unit then display results
    if type == 'I':
        converted_unit = unit * 2.54
        print(unit, 'inches equals', format(converted_unit, '.2f'), 'centimeters')
    elif type == 'C':
        converted_unit = unit / 2.54
        print(unit, 'centimeters equals', format(converted_unit, '.2f'), 'inches')
    elif type == 'O':
        converted_unit = unit * 28.3495231
        print(unit, 'ounces equals', format(converted_unit, '.2f'), 'grams')
    elif type == 'G':
        converted_unit = unit / 28.3495231
        print(unit, 'grams equals', format(converted_unit, '.2f'), 'ounces')
    elif type == 'M':
        converted_unit = unit * 1.609344
        print(unit, 'miles equals', format(converted_unit, '.2f'), 'kilometers')
    elif type == 'K':
        converted_unit = unit / 1.609344
        print(unit, 'kilometers equals', format(converted_unit, '.2f'), 'miles')
    print()

    # ask user again
    response = input('Would you like to convert again?: (Y/N): ')
    response = response.upper();
    print()

    while response != 'Y' and response != 'N':
        response = input('Please enter a Y or N: ')
        print()
    if response == 'N':
        terminate = True
