

d = {'key1': 1, 'key2': 2}

ratio = 2

for key, value in d.items():
    d[key] -= ratio
    print(d[key])