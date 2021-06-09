
d = {'key1': 1, 'key2': 2, 'aab': 3, 'student4': 3}

print(sorted(list(d.keys())))

max_value = max(d.values())

print(max_value)
print(list(d.keys())[list(d.values()).index(max_value)])

print(sorted([student for student, score in d.items() if score == max_value]))

x = '1'
y = 'hej'

print(x, ' | ', y)