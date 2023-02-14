from mergesort import mergesort
import math as mt

def crossinv(L1,L2):
    inv = 0
    L1 = mergesort(L1)
    L2 = mergesort(L2)
    while L1 != [] and L2 != []:
        if L1[0] > L2[0]:
            inv += len(L1)
            del L2[0]
        elif L1[0] < L2[0]:
            del L1[0]
        else:
            print("Please enter a list with distinct elements")
            raise Exception
    return inv


def countinversions(L):
    n = len(L)
    if n == 2:
        if L[0] > L[1]:
            return 1
        else:
            return 0
    elif n == 1 :
        return 0

    B1 = L[:mt.ceil(n/2)]
    B2 = L[mt.ceil(n/2):]
    inv1 = countinversions(B1)
    inv2 = countinversions(B2)
    crossinvs = crossinv(B1,B2)
    return inv1 + inv2 + crossinvs


print(countinversions([1,2,4,3,0,-1]))