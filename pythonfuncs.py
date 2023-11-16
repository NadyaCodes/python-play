def hello():
  print("Hello")

hello()

def add10(x):
  return x+10

print(add10(9))

#Lamda functions (anonymous functions)

g = lambda x: x*x*x
print(g(5))

li=[5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
filter_list=list(filter(lambda x: (x%2 != 0), li))
print(filter_list)

map_list=list(map(lambda x: x*2, li))
print(map_list)


from functools import reduce
sum = reduce((lambda x, y: x+y), li)
print(sum)