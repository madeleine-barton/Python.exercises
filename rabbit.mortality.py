# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:13:03 2018

@author: bar823
"""

# 9. Mortal Fibonacci Rabbits
# Purpose: Include a mortality function in rabbit mating model
# Signature: int + int + int -> int


def mortal_rabs(n, m, k):

    """ Include a mortality function in the fibonnacci rabbits

    >>>mortal_rabs(3,1,1)
    return(2)

    >>>mortal_rabs(1,1,1)
    return(0)

    >>>mortal_rabs(3,0,1)
    return(2)

    """
    if(n < 2 | k < 1):          # only this spacing was accepted
        pop_size = 0
    else:
        rabs = [1, 1]
        babies = [1, 0]
        adults = [0, 1]
        deaths = [0, 0]
        for i in range(2, n):
            babies.append((adults[i-1]-deaths[i-1])*k)
            adults.append(rabs[i-1])
            if (i >= m and m != 0):
                deaths.append(babies[i-m])
            else:
                deaths.append(0)
            rabs.append(babies[i] + adults[i] - deaths[i])
            pop_size = rabs[i]
    return(pop_size)


n = 94
m = 0
k = 1

mortal_rabs(n, m, k)
print(mortal_rabs(n, m, k))
