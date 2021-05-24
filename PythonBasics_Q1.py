data = list(range(2000,3201))


n = []

for i in data:
    if ((i%7 == 0) and (i%5 != 0)):
        n.append(i)

print(n)