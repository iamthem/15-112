def ct1(a):
    result = 0
    for i in range(0, a, 3):
        result += i
        if result >= 6:
            return i
    return result

def ct2(n):
    a = 0
    while n > a:
        a = n%10
        n //= 10
        b = 0
        for i in range(a):
            b += i
        print(b)
    return n


def rc1(m):
    if  ((not   isinstance(m, int))
        or  (m < 0)): return  False
    x   =   1
    while   (x  <   m//2):  x   += 10
    return  (x  +   m   ==  60)

def mysteryCode(n):
    n = abs(n)
    x = 0
    while(n!=0):
        if n%2 == 1:
            x = x*10 + n%10
        n //= 10
    return x


def isPerfectNum(n):
    divisors = []
    for i in range(1,n):
        if n // i == n / i:
            divisors.append(i)
    return sum(divisors) == n 

import copy
def f2(a):
    assert(sorted(a) == list(range(5,9)))
    b = copy.copy(a)
    for i in range(len(b)):
        b[len(b)-1-i] *= i
    return ((b[0] == 18) and (min(a) == b[2]) and (a[1] > a[3]))
