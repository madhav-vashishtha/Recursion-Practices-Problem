def binary_search(arr, low, high, target):

    if low > high:
        return -1
    
    mid = (low+high)//2

    if arr[mid] == target:
        return mid
    
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    
    else:
        return binary_search(arr, mid + 1, high, target)
    
nums = [-1, 0, 3, 5, 9, 12]
target = 9

result = binary_search(nums, target, 0, len(nums) - 1)

print(result)

