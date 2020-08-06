#!/usr/bin/env python
# cc.py

import sys

INVALID = -1
VISA = 0
MASTERCARD = 1
AMERICAN_EXPRESS = 2
EN_ROUTE = 3
DINERS_CLUB = 4
DISCOVER = 5

cardNames = ['Visa', 'Mastercard', 'American Express', 'En Route',
             'Diners Club/Carte Blanche', 'Discover']

def validCCNumber(numStr):
    cardID = getCardID(numStr)
    if cardID != -1:
        # LUHN formula (mod10)
        try:
            ss = [s1 for s1 in numStr]
            chksm = 0
            i = len(ss) - 1
            while i >= 0:
                k = 0
                if i > 0:
                    k = int(ss[i-1]) * 2
                    if k > 9:
                        s = str(k)
                        k = int(s[:1]) + int(s[1:])
                    chksm = chksm + int(ss[i]) + k
                else:
                    chksm = chksm + int(ss[0])
                i = i - 2
            return not(chksm % 10)
        except Exception, ex:
            print ex
            return 0
    else:
        return 0

# Returns the card type    
def getCardID(numStr):
    valid = INVALID
    
    x1 = numStr[:1]
    x2 = numStr[:2]
    x3 = numStr[:3]
    x4 = numStr[:4]    

    if isNum(numStr):
        # For visa, prefix = 4, length = 13 or 16
        if x1 == '4' and (len(numStr) in [13, 16]):
            valid = VISA
        # For mastercard, prefix = 51...55, length = 16
        elif (x2 in ['51', '52', '53', '54', '55']) and len(numStr) == 16:
            valid = MASTERCARD
        # For american express, prefix = 34, 37; length = 15
        elif (x2 in ['34', '37']) and len(numStr) == 15:
            valid = AMERICAN_EXPRESS
        # For enroute, prefix = 2014, 2149; length = 15
        elif (x4 in ['2014', '2149']) and len(numStr) == 15:
            valid = EN_ROUTE
        # For diners club, prefix = 36, 38, 300...305; length = 14
        elif ((x3 in ['300', '301', '302', '303', '304', '305']) or \
              (x2 in ['36', '38'])) and len(numStr) == 14:
            valid = DINERS_CLUB
        # For discover, prefix = 60; length = 16
        elif x2 == '60' and len(numStr) == 16:
            valid = DISCOVER
        # Invalid
        else:
            valid = INVALID
        return valid

def isNum(s):
    try:
        i = int(s)
        return 1
    except ValueError, ve:
        print ve
        return 0

def getCardName(id):
    if id > -1 and id < len(cardNames):
        return cardNames[id]
    else:
        return ''
    

if __name__ == '__main__':
    card = ''
    if len(sys.argv) > 1:
        card = sys.argv[1]
    else:
        card = raw_input('Enter card number: ')
        
    if getCardID(card) > -1:
        print 'This card is supported.'
        print 'This is a ', getCardName(getCardID(card))
        if validCCNumber(card):
            ret = 'good'
        else:
            ret = 'bad'
        print 'The card number ', card, ' is ', ret
    else:
        print 'The card is invalid or unsupported'
