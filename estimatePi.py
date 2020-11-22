import sys
import random

## Area of a square = x**2
## Area of a circle = pi*(r**2)
## Circle Equation: (x - h)**2 + (y-k)**2 = r**2

## Arbitrarily define x = 16 and therefore r = 8.
x = 16
r = x/2

inCircle = 0
total = 0

trials = int(sys.argv[1])

for n in range(trials):
    xRandom = random.uniform(r * -1, r)
    yRandom = random.uniform(r * -1, r)
    if ((xRandom**2 + yRandom**2)**(1/2)) <= r:
        inCircle += 1
    total += 1

piEstimate = ((inCircle/total)/(r**2))*(x**2)

print("Pi estimate: " + str(piEstimate))
