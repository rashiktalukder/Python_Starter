
data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
result = []

for value in data_list:
    if type(value) == int:
        result.append(value)

print(result)