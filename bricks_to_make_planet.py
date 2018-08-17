# How many bricks would it take to make a reasonable size planet

# :)

import math

# ten thousand kilometers, a good bit bigger than earth, smaller than the gas giants 
# and 10 just makes things round
RADIUS = 10000 

# Bricks per meter
# lets use half bricks - they're more close to square, then we can double them
HALFBRICKSPERKILOMETER = 10 * 1000

# Whole bricks to make a planet
# of course, divide by two since we used half bricks
area_of_a_planet = int(math.pi*((RADIUS * HALFBRICKSPERKILOMETER)**2))/2
print(area_of_a_planet)
