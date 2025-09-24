gulu = [34, 78 ,98, 76845, 989856, 8784, 90, 876]

result = 0

i = 0
n = len(gulu)
while i < n :
    result = result + gulu[i]
    i += 1

print(result)
i = 0
while i < n :
    if gulu[i] % 2 == 0 :
        gulu[i] = 0
    i += 1

print(gulu)


fuku = [23, 45 ,667, 23, 12, 12, 45, 667, 89 ,00]
resultt  = 0
for k in range(len(fuku) - 1) :
    if fuku[k] != fuku[k+1] :
        resultt = resultt +1

print(resultt)

print(len(set(fuku)))


#Attributes of set data type in python
#unordered cant find elements by index
#immutable // no update
#no duplicates