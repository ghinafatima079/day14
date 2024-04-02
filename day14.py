# Write a Python class called Rectangle with attributes length and width, and methods to calculate its area and perimeter.
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def cal_area(self):
        area=self.length*self.width
        return area
    def cal_peri(self):
        peri=2*(self.length+self.width)
        return peri
l=float(input("Enter length of rectangle:"))
w=float(input("Enter width of rectangle:"))
rect=Rectangle(l,w)
print(f"The area of the rectangle is {rect.cal_area()}")
print(f"The perimeter of the rectangle is {rect.cal_peri()}")

# Create a Python class called Student with attributes name, age, and grades
# and methods to add grades, calculate average grade, and display student information.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.grades=[]
    def add_grades(self,grade):
        self.grades.append(grade)
    def avg_grades(self):
        total=sum(self.grades)
        print(f"The average grade is {total/len(self.grades)}")
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
st=Student("ABC",20)
st.add_grades(7)
st.add_grades(8)
st.add_grades(10)
st.display_info()
st.avg_grades()

# Employee and Manager class
class Employee:
    def __init__(self,name,salary,bonus_percentage):
        self.name=name
        self.salary=salary
        self.bonus_percentage=bonus_percentage
    def calculate_bonus(self):
        return self.salary*(self.bonus_percentage/100)
class Manager(Employee):
    def __init__(self,name,salary,bonus_percentage,department):
        super().__init__(name,salary,bonus_percentage)
        self.dept=department
    def calculate_bonus(self):
        base_bonus=super().calculate_bonus()
        return base_bonus*0.1
    
emp1 = Employee("ABC", 1000, 5)
print("Employee 1 Bonus:", emp1.calculate_bonus())
mngr1 = Manager("XYZ", 7000, 7, "Marketing")
print("Manager 1 Bonus:", mngr1.calculate_bonus())
mngr2 = Manager("PQR", 5000, 6, "HR")
print("Manager 2 Bonus:", mngr2.calculate_bonus()) 
    