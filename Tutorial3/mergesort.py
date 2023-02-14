import math as mt

def combine(L1,L2):
    L = []
    while len(L1) != 0 and len(L2) != 0:
        if L1[0] >= L2[0]:
            L.append(L2[0])
            del L2[0]
        else:
            L.append(L1[0])
            del L1[0]
    else:
        if L1 == []:
            L.extend(L2)
        else:
            L.extend(L1)
    return L

def mergesort(L: list):
    n = len(L)
    if n == 2:
        if L[0] >= L[1]:
            return [L[1],L[0]]
        else:
            return L
    elif n == 1:
        return L
    B1 = mergesort(L[:mt.ceil(n/2)])
    B2 = mergesort(L[mt.ceil(n/2):])
    return combine(B1,B2)



# print(mergesort([0,9,8,3,5,6,4,3,2,1]))