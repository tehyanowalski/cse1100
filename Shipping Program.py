# Tehya Nowalski
# Lab 1:00 pm
# December 2020
#
# Shipping Program
# The Shipping Program allows the user to enter any number of items wished
# to be shipped then calculates the Subtotal, Tax, Shipping and Handling,
# and Total Due for the item.
#
# Where ... Sales Tax is 8% for CA.
#
# And ... Shipping is 25 cents per lb.
#
# Then ... Handling is based on the Box Weight
#       if ... < 10 lbs = $1
#       if ... > 100 lbs = $5
#       if ... 10-100 lbs = $3
#

# get user info of the item(s)
def getInfo():
    prodInfo = []
    more = True

    while more == True:
        qty = int(input('Enter quantity (enter 0 if done): '))

        if qty == 0:
            more = False
        else:
            itemWght = float(input('Enter weight of Item: '))
            itemCost = float(input('Enter cost of Item: '))
            print()
            prodInfo.append([qty, itemWght, itemCost])

    return prodInfo

# calculate all item info based on user input
def Calculation(prodInfoList):

    boxWght = 0
    subTtl = 0

    for k in range(len(prodInfoList)):
        qty, itemWght, itemCost = prodInfoList[k]

        boxWght = boxWght + (qty * itemWght)
        subTtl = subTtl + (qty * itemCost)

    shipping = boxWght * .25

    if boxWght < 10:
        handling = 1
    elif boxWght > 100:
        handling = 5
    else:
        handling = 3

    shipAndHand = shipping + handling

    return (subTtl, shipAndHand)

# --- main

# display program welcome
print('This program was created by Tehya Nowalski')
print()
print('This Shipping Program allows the user to enter any number of items')
print('wished to be shipped then calculates the Subtotal, Tax,')
print('Shipping and Handling, and Total Due for the item.')
print()


# user input state of shipping
state = input('Please enter the state abbreviation you are shipping to: ')
state = state.upper();
print()


prodInfoList = getInfo()

subTtl, shipAndHand = Calculation(prodInfoList)

# sales tax only calculated for California
if state == 'CA':
    salesTax = subTtl * .08
else:
    salesTax = 0.00

ttlDue = subTtl + shipAndHand + salesTax


# display results based on user input
print()
print(format('Subtotal:', '<25'), format(subTtl, '>10,.2f'))
print(format('Tax:', '<25'), format(salesTax, '>10,.2f'))
print(format('Shipping and Handling:', '<25'), format(shipAndHand, '>10,.2f'))
print(format('Total Due: ', '<25'), format(ttlDue, '>10,.2f'))
