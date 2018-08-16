# How many bricks would it take to make a reasonable size planet

# :)

import math

# ten thousand kilometers, a good bit bigger than earth, smaller than the gas giants 
# and 10 just makes things round
RADIUS = 10000 

# Bricks per meter
# lets use half bricks - they're more close to square, then we can double them
HALFBRICKSPERMETER = 10

# Area of a planet
# of course, times by two since we used half bricks
area_of_a_planet = 2*int(math.pi*((RADIUS*HALFBRICKSPERMETER)**2))
print("{:,}".format(area_of_a_planet))
