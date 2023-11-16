class Phone:
  def set_color(self,color):
    self.color=color
  def set_cost(self,cost):
    self.cost=cost
  def show_color(self):
      print("This phone is",self.color)
      return self.color
  def show_cost(self):
    print("This phone costs $", self.cost)
    return self.cost
  def make_call(self):
    print("Making phone call")
  def play_game(self):
    print("Playing game")

p1=Phone()
p1.make_call()
p1.play_game()
p1.set_color("red")
p1.show_color()



class Employee:
  def __init__(self,name,age,salary,gender):
    self.name=name
    self.age=age
    self.salary=salary
    self.gender=gender
  
  def employee_details(self):
    print("Name of employee is: ",self.name)
    print("Age of employee is: ",self.age)
    print("Salary of employee is: ",self.salary)
    print("Gender of employee is: ",self.gender)


e1=Employee("Mark", 20, 50000, "male")
e1.employee_details()


class Vehicle:
  def __init__(self,mileage,cost):
    self.mileage=mileage
    self.cost=cost
  def show_details(self):
    print("I am a vehicle")
    print("The mileage is ",self.mileage)
    print("The cost is",self.cost)

class Car(Vehicle):
  def __init__(self,mileage,cost,tyres,hp):
    super().__init__(mileage, cost)
    self.tyres=tyres
    self.hp=hp
  def show_car(self):
    print("I am a car")
    print("Number of tyres are", self.tyres)
    print("Value of horse power is", self.hp)

v1=Vehicle(300,1000)
v1.show_details()

c1=Car(200,1200, 4, 300)
c1.show_details()
c1.show_car()

#Single Inheritance
#Multiple Inheritance - two parents, inherit both parent's properties - class Child(Parent1,Parent2)
#Multi-level Inheritance - Parent, Child, Grandchild - class Child(Parent)...class Grandchild(Child)
#Hybrid Inheritance