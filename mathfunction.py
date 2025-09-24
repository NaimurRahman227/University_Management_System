import math
g = 2.6
print(math.ceil(g))

print(math.floor(g))

print(round(g))

num = float(input('Enter a number : '))

if num >= 0 :
    rounded_num = int(num + .5)

else :
    rounded_num = int(num - .5)

print('rounded_number : ' , rounded_num)

