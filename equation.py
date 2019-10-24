
"""
Calculatin a second degree equation
10/2019
Author:
        Juliette Forest
"""

import math
def equation(a,b,c): #enter equation values
    delta = b**2-4*a*c #calculate the discriminant, here delta
    if delta < 0: #if delta is inferior to zero, no solution
        print("There is no solution")
    elif delta == 0: #if delta equal to zero, there is 1 solution
        x = (-b)/(2*a)
        print("The solution is: x = {}".format(x))
    else: #if delta is superior to 0, there are 2 solutions
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("There are two solutions: x = {} or x = {}".format(x1, x2))
