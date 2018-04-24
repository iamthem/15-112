def f(x): 
    print('f', x)
    x += 1
    return x**2//10

def g(x):
    print('g', x)
    x = (7*x)%5
    return f(x+3)

import math 
def roc1(check1):
    a = check1 // 100
    b = check1 // 10 % 10
    c = check1 % 10
    d = b*b - math.log(16, 2) * a*c
    e = 2 * (d > 0) + 1 * (d == 0) + 0 * (d < 0)

    return bool(e % 2)

def fabricExcess(fabricInches):
    if fabricInches % 36 == 0:
        return 0
    else:
        return 36 - (fabricInches % 36)
