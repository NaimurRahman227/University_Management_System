naimur = 45
print(20 == 34)
print(30 == 30)

if naimur == 4 :
    print('go to school')

else :
    print('dont go to school')

hunda = input('enter a bunch of number to check : ')
clist = [int(x.strip()) for x in hunda.split(' ')]

for y in clist :

    if y > 0 :
        print(f' the number is positive : {y}')

    elif y < 0 :
        print(f'The number you entered is negative {y}')

    else :
        print(f'The number you entered is zero : {y}')

print(clist)
