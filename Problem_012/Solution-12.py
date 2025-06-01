
list1 = [3, 5, 7, 4, 8, 8]

list2 = [4, 9, 8, 7, 1, 1, 13]

commonList = []

for value in list1:
    if (value in list2) and (value not in commonList) :
        commonList.append(value)

summationResult = sum(commonList)
print(summationResult)

