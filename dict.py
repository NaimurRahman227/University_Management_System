my_dict = {'name' : 'naimur' , 'roll' : 2002147 , 'dept' : 'ECE'}

print(my_dict)
print(my_dict.values())

for i in my_dict.values():
    print(i)

for k,v in my_dict.items():
    print(f" {k} : {v}")

u = [1 , 2 , 3 , 4 , 5]
l = ['mango', 'jack' , 'rocklemon' , 'apple', 'pineapple']

h = dict(zip(u,l))
print(h)
print(dict(h))
print(dict(zip(u,l)))

print(h[1])

#dictionary comprehension
even_odd = list(range(0,21))

dictview = {i : 'even' if i%2 == 0 else 'odd' for i in even_odd}

print(dictview)