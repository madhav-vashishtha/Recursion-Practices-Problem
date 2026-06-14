def SumOfArray(l1):
    if len(l1) == 0:
        return 0
    
    SumOfLeftOverArray = SumOfArray(l1[1:])

    ans = l1[0] + SumOfLeftOverArray

    return ans

print(SumOfArray([1, 2, 3, 4, 5]))

print(SumOfArray([10, -2, 3, 5]))


