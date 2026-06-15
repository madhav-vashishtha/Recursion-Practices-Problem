def firstIndicesOfNumber(l1,x):
    if len(l1) == 0:
        return -1
    
    if l1[0] == x:
        return 0
    
    firstIndiceInLeftOver = firstIndicesOfNumber(l1[1:],x)

    if firstIndiceInLeftOver == -1:
        return -1
    else:
        return firstIndiceInLeftOver + 1
    
print(firstIndicesOfNumber([1, 2, 3, 2, 4, 2],2))

print(firstIndicesOfNumber([5, 6, 7, 8],10))

