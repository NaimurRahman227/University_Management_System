koko = [23 ,22 ,44, 45, 57, 65, 77,90, 222]
new_koko = []

for i in koko :
    if i % 2 != 0 :
        new_koko.append(i**2)
    else :
        new_koko.append(i)
print(new_koko)

foko = [i**2 if i%2 == 0  else i + 1     for i in koko]

print(foko)