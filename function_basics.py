#function is 2 types
# 1. User defined Function
# 2. Built-in Function

nunnu = ' this is my name string'

print(nunnu[6])
print(nunnu[-1])
print(nunnu[len(nunnu)-1])

#string is immutable // immutable means cant be changed after assigned

#string methods

nanu = nunnu.title()
print(nanu)
upnanu = nunnu.upper()
downnunu = nunnu.lower()

print(upnanu)
print(downnunu)

nambu = 'this skdfjid tHshkF dkDKHJWS'
x = nambu.replace('skdfjid' , 'dxgdjvbc')
print(x)
print(nambu.swapcase())

print(nambu.count('S'))


name = input('enter your name')
age = input('enter your age :')

passage = 'i am {} , i am {} years old'.format(name, age)
print(passage)

pass2 = f'i am {name} and i am {age} years old'
print(pass2)