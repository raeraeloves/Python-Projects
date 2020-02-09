# import libraries
import math
sqrt = math.sqrt

# create variable class
class coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# instantiate coords object
while True:
    try:
        coord1 = coords(
            int(input('Enter the first x-value: ')),
            int(input('Enter the corresponding first y-value: '))
            )
        coord2 = coords(
            int(input('Enter the second x-value: ')),
            int(input('Enter the corresponding second y-value: '))
            )
        print()
    except ValueError: # verify numeric response
        print('Numbers only, please!')
        continue
    else:
        print('Coordinates are ({}, {}) and ({}, {}).\n'.format(coord1.x, coord1.y, coord2.x, coord2.y))
        break

# calculate distance
d = sqrt((coord2.x - coord1.x) ** 2) + ((coord2.y - coord1.y) ** 2)
print('The distance between points ({}, {}) and ({}, {}) is: {:.0f}.'.format(coord1.x, coord1.y, coord2.x, coord2.y, d))

# calculate slope        
while True:
    try: 
        m = (coord2.x - coord1.x) / (coord2.y - coord1.y)
        print('The slope from ({}, {}) to ({}, {}) is: {:.3f}.'.format(coord1.x, coord1.y, coord2.x, coord2.y, m))
        break
    except ZeroDivisionError:
        print('Denominator is zero. Slope is undefined.')
        break

        


