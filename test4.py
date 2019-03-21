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

"""
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
"""
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age')    # 删除属性 'age'


emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)