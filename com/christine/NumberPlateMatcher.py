# checks if input is a valid kenyan plate using the format  LLL NNNL
# where L denotes a letter and N denotes a number
import re

class NumberPlateMatcher:

    numberPlate = raw_input('Enter a String')
    str = 'KBX 234K'
    match = re.search(r'^[A-Z]{3} [0-9]{3}[A-Z]{1}$', numberPlate)
    if match:
        print 'found Plate:', match.group()
    else:
        print 'did not find valid plate'
