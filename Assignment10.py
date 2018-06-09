print("Question 1")
#Question 1
class Animal:
    def animal_attribute(self):
        print("Animal attribute")
class Tiger(Animal):
    print("Tiger")
ob=Tiger()
ob.animal_attribute()
print("Question 2")
#Question 2
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())
print("Question 3")
#Question 3
class Cop:
    def __init__(self):
        self.nam=""
        self.a=0
        self.we=0
        self.d=""
    def add(self):
        self.nam=input("Enter the name: ")
        self.a=int(input("Enter the age: "))
        self.we=int(input("Enter work experience: "))
        self.d=input("Enter the designation: ")
    def display(self):
        print("Name: ",self.nam)
        print("Age: ",self.a)
        print("Work Experience: ",self.we)
        print("Designation: ",self.d)
    def update(self):
        s=input("Enter what do you want to update: ")
        if(s=="name"):
            nam = input("Enter the name: ")
            self.display()
        elif(s=="age"):
            a = int(input("Enter the age: "))
            self.display()
        elif(s=="work"):
            we = int(input("Enter work experience: "))
            self.display()
        elif(s=="designation"):
            d = input("Enter the designation: ")
            self.display()
class Mission(Cop):
    def __init__(self):
        super(Mission, self).__init__()
    def display_mission(self,mission):
        mission.display()
        print("Mission")
    def add_mission_details(self,mission):
        mission.add()
        mission.update()
        print("Fatal Mission")
ob=Cop()
mission=Mission()
mission.add_mission_details(ob)
mission.display_mission(ob)
print("Question 4")
#Question 4
class Shape:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        a=self.l*self.b
        print("Area is ",a)
class rectangle(Shape):
    print("Rectangle")
class square(Shape):
    print("Square")
r=rectangle(2,3)
r.area()
s=square(4,4)
s.area()
