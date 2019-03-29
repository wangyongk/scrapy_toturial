a = [x for x in range(10)]
print(a)
a.append(10)
print(a)
b = [11, 12, 13]
a.append(b)
print(a)
a.extend(b)
print(a)
a.insert(1, 'a')
print(a)
print(a)
for i in range(1, 5):
    i = i + 1
    print(i)
