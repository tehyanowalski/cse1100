# Tehya Nowalski
# Lab 1:00 pm
# November 2020
#
# The Morse Code program developed by Tehya Nowalski
# allows the user to type in a message and
# have it converted into Morse code, or enter Morse code and 
# have it converted back to the original message.
#

# init
stop = False
morseOut = ''

morseKey = (('a','.-'), ('b','-...'), ('c','-.-.'), ('d', '-..'), ('e', '.'),
            ('f','..-.'), ('g','--.'), ('h','....'), ('i','..'), ('j','.---'),
            ('k','-.-'), ('l','.-..'), ('m','--'), ('n','-.'), ('o','---'),
            ('p','.--.'), ('q','--.-'), ('r','.-.'), ('s','...'), ('t','-'),
            ('u','..-'), ('v','...-'), ('w','.--'), ('x','-..-'), ('y','-.--'),
            ('z','--..'))

# display welcome
print ('created by Tehya Nowalski')

print('Welcome to the Morse Code program that allows you')
print('to translate your message to and from Morse Code.')
print('When entering Morse Code put a space between the characters.')
print()

while stop == False:

    # get user input to encrypt/decrypt
    which = input('Enter (m) to translate to Morse Code or (a) to translate from Morse Code: ')

    while which != 'm' and which != 'a':
        which = input("Enter 'm' or 'a': ")
        
    toMorse = (which == 'm') # evaluate condition True/False

    # get translation
    morseInput = input('Enter what you want to translate: ')
    print ()
    # perform encryption or decryption
    if toMorse == True:

        morseInput = morseInput.lower();
        
        fromIndex = 0
        toIndex = 1
    else:

        morseInput = morseInput.split()
        
        fromIndex = 1
        toIndex = 0


    for char in morseInput: # iterates over input
        letterFound = False # set to False

        if which == 'm':

            for mainIndex in morseKey: # iteration over the pairs of letters in morseKey
                if char == mainIndex[fromIndex]:
                    morseOut = morseOut + ' ' + mainIndex[toIndex]
                    letterFound = True
        else:
            for mainIndex in morseKey:
                if char == mainIndex[fromIndex]:
                    morseOut = morseOut + mainIndex[toIndex]
                    letterFound = True

    if toMorse == True:
        print(morseInput, 'is', morseOut, 'in Morse Code.')
        print ()
    else:
        print(morseInput, 'is', morseOut, 'in English.')
        print ()

    # reset
    morseOut = ''

    # continue
    response = input('Would you like to translate again? (y/n): ')
    response = response.lower();
    print ()
    while response != 'y' and response != 'n':
        response = input("Please enter a 'y' or 'n': ")
        response = response.lower();

    if response == 'n':
        stop = True
