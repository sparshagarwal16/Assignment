print("Question 1")
#Question 1
import math
class circle:
    def __init__(self,radius):
        self.r=radius
    def getArea(self):
        a=math.pi*self.r**2
        print("Area of the circle is ",a," square units")
    def getCircumference(self):
        c=2*math.pi*self.r
        print("Circumference of the circumference is ",c," units")
r=int(input("Enter the radius: "))
d=circle(r)
d.getArea()
d.getCircumference()
print("Question 2")
#Question 2
class Student:
    def __init__(self,name,roll):
        self.nam=name
        self.rn=roll
    def Display(self):
        print("Name of the student is ",self.nam)
        print("Roll No. of the student is ",self.rn)
nam=input("Enter the name of the student: ")
rn=int(input("Enter the Roll No. of the student: "))
D=Student(nam,rn)
D.Display()
print("Question 3")
#Question 3
class Temperature:
    def __init__(self,cel,fah):
        self.c=cel
        self.f=fah
    def convertFahrenheit(self):
        w=(self.c+32)*1.8
        print("Temperature in Fahrenheit is ",w)
    def convertCelcius(self):
        s=(self.f-32)*0.55
        print("Temperature in Celsius is ",s)
c=int(input("Enter temperature in celcius: "))
f=int(input("Enter temperature in fahrenheit: "))
obj=Temperature(c,f)
obj.convertCelcius()
obj.convertFahrenheit()
print("Question 4")
#Question 4
class MovieDetails:
    def __init__(self,moviename,artistname,year,ratings):
        self.mn=moviename
        self.an=artistname
        self.yor=year
        self.r=ratings
    def Display(self):
        print("Name of the movie is ",self.mn)
        print("Name of the artist is ",self.an)
        print("Year of release ",self.r)
        print("Ratings ",self.r)
    def update(self):
        s=input("Enter what do you want to update: ")
        if(s=="movie name"):
            self.mn=input("Enter the name of the movie: ")
            self.Display()
        elif(s=="artist name"):
            self.an=input("Enter the name of the artist: ")
            self.Display()
        elif(s=="year"):
            self.yor=input("Enter the year of release: ")
            self.Display()
        elif(s=="ratings"):
            self.r=input("Enter the ratings: ")
            self.Display()
        else:
            self.Display()
mn=input("Enter the name of the movie: ")
an=input("Name of the artist: ")
yor=input("Enter the year of release: ")
r = input("Enter the ratings: ")
s=MovieDetails(mn,an,yor,r)
s.Display()
s.update()
print("Question 5")
#Question 5
class Expenditure:
    def __init__(self,exp,sav):
        self.e=exp
        self.s=sav
        self.sa=0
    def displayes(self):
        print("Expenditure: ",self.e)
        print("Savings: ",self.s)
    def salary(self):
        self.sa=self.e+self.s
    def display(self):
        print("Salary: ",self.sa)
e=int(input("Enter expenditure: "))
s=int(input("Enter savings: "))
object=Expenditure(e,s)
object.displayes()
object.salary()
object.display()





