class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary,age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print( "Name : ", self.name, ", Salary: ", self.salary,"age:",self.age)


"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000,7)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000,8)

emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)