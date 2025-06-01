
dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}

dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

resDict = {}

for key in dict1:
    if key in dict2.keys():
        resDict[key] = dict1[key] , dict2[key]

print(resDict)