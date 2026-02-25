def mergeTwoLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    
    if list1[0] < list2[0]:
        return [list1[0]] + mergeTwoLists(list1[1:], list2)
    else:
        return [list2[0]] + mergeTwoLists(list1, list2[1:])

list1 = [1,2,4]
list2 = [1,3,4]
print(mergeTwoLists(list1, list2))

list1 = []
list2 = []
print(mergeTwoLists(list1, list2))

list1 = []
list2 = [0]
print(mergeTwoLists(list1, list2))
