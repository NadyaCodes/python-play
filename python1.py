employee_name = "John"
# print(employee_name)
# employee_name = "Sam"
# print(type(employee_name))
# print(employee_name)
# employee_name = 3
# print(type(employee_name))
# print(employee_name)

# employee_name = True
# print(type(employee_name))
# print(employee_name)

employee_name = 3.14
print(type(employee_name))
print(employee_name)

#this is a comment
#Arithmetic Operators: + - * /
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Relational Operators: < > == !=
print(a>b)
print(a<b)
print(a==b)
print(a!=b)

#Logical Operators & |
a=True
b=False
print(a&b)
a=True
b=True
print(a&b)

print(a|b)

s1 = '''This is a 
multiline string'''

print(s1)
print(s1[-2])
print(s1[3:10])

print(len(s1))
print(s1.lower())
print(s1.upper())
print(s1.replace("i", "a"))
print(s1)
print(s1.count("i"))
print(s1.find("i"))
print(s1.split("i"))


#Tuple -  like an immutable array
tup1=(1, "a", True)
print(tup1)
tup2=(1, "a", True,2,"b",3+5)
print(tup2)
print(tup2[1:4])
print(tup1+tup2)
print(tup1*3+tup2)
tup3=(3,7)
tup4=(3,8,1,34,7)
print(min(tup3))
print(max(tup4))

#List - like an array
l1=[1, "word", 3.14, True, 3+5]
print(l1)
print(l1[2:5])
l1[4]="newL14"
print(l1)
l1.append("Hi!")
print(l1)
l1.pop()
print(l1)
l1.reverse()
print(l1)
l1.insert(1, "new1")
print(l1)
l2=["mango", "banana", "guava", "apple"]
l2.sort()
print(l2)

#Dictionary - like an object
fruit={"Apple":10, "Orange":20, "Banana":40, "Peach":100}
print(fruit)
print(fruit.keys())
print(fruit.values())
fruit["Orange"]=10
print(fruit["Orange"])
fruit["Mango"]="mango"
print(fruit)
addedFruit={"New Fruit":1000}
fruit.update(addedFruit)
print(fruit)
fruit.pop("Orange")
print(fruit)

#Set - unordered, unindexed group....no duplicates allowed
set1={1, "a", True}
print(set1)
set1.add("New")
print(set1)
set1.update([2, 3, 4])
print(set1)
set1.remove(3)
print(set1)
set2={6, 7, 8, 9}
print(set1.union(set2))
set3={1, 3, 5, 7, 9}
set4={5, 6, 7, 8, 9}
print(set3.intersection(set4))

#if
a=10
b=20
if a>b:
  print("a is greater than b")
else:
  print("b is greater than a")

c=30
if (a>b & a>c):
  print("a is the greatest")
elif (b>a & b>c):
  print("b is the greatest")
else:
  print("c is the greatest")


iftup1=(1,2,3,4,5)

if 3 in iftup1:
  print("Yeah, there's a three")
else:
  print("nope")

iflist=[1,2,3,4,5]
if iflist[1]==2:
  iflist[1]=iflist[1]+100
print(iflist)

#Loop
i = 1
while i<=10:
  print(i)
  i=i+1

fruitList=["apple", "orange", "banana"]

for i in fruitList:
  print(i)

colorList=["blue", "purple", "red"]

for i in fruitList:
  for n in colorList:
    print(n, i)

