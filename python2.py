num = int(input("Enter a number:"))
if (num > 0):
  print("Positive Number")
elif (num==0):
  print("Zero")
else:
  print("Negative Number")


factorial=1
if num < 0:
    print("Factorials don't exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
      factorial = factorial * i
    print("The factorial of ", num, " is ", factorial)

rev=0
while(num>0):
   dig=num%10
   rev=rev*10+dig
   num=num//10
print("Reverse of the number: ", rev)
print(num)

num2 = int(input("Enter the second number: "))
a=0
b=1
if num2<0:
   print("Number must be 0 or higher")
elif num2==0:
   print(a)
else:
   for i in range(2, num2):
      c=a+b
      a=b
      b=c
print(b)
