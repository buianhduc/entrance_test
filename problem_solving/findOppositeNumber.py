def findOppositeNumber(n,i):
    if i > n:
        return -1 #there is no opposite number
    mid = n/2
    if i > mid:
        return i-mid
    elif i < mid:
        return i+mid
    else:
        return 0

print(findOppositeNumber(12,9))