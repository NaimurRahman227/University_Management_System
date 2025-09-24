juju = [45, 67 ,23, 56 ,34 ,234, 23 ,67 , 90 ,56]
result = []

for i in juju :
    if i not in result :
        result.append(i)

print(len(result))
for i in range(20):
    for j in range(12):
        print(i, j)
