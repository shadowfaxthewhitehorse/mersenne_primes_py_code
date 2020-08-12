# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:26:23 2020

@author: Anand Manikutty
"""

#
# IMPORTANT NOTE:
#
# please note that most of the code in this repository is private.
#
# miller_rabin() function courtesy Ayrx:
#
# https://gist.github.com/Ayrx/5884790#file-miller_rabin-py

import random

def prime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))
 
print(prime(103))

# As we mentioned above, Robinson worked in number theory and 
# he used the earliest computers to obtain results. He coded 
# the Lucas test for primality and tested whether 2^{n} - 1 was 
# prime for all primes n < 2304 on the SWAC computer. 
# He gave his results in "Mersenne and Fermat numbers" published 
# in the Proceedings of the American Mathematical Society in 
# 1954. These showed that these Mersenne numbers were all 
# composite except for the seventeen values: nn = 2, 3, 5, 
# 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 
# 2281, for which 2^{n} - 1 is a prime. At the time that 
# Robinson wrote this paper the last five of these primes 
# were larger than any that had previously been found.

def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

first_n = 2
last_n = 2400


last_mersenne = 4 - 1
count = 2

list_of_primes = []

for index in range(1, last_n):
    last_mersenne = 2*last_mersenne + 1
    count += 1
    
    if(miller_rabin(last_mersenne, 40)):
        print("The Mersenne number (" + str(count) + ") " + str(last_mersenne) + " is prime.")
        list_of_primes.append([count, last_mersenne])
    else:
#        print("The Mersenne number " + str(last_mersenne) + " is not prime.")
        print("The Mersenne number (" + str(count) + ") " + str(last_mersenne) + " is not prime.")


print(list_of_primes)
