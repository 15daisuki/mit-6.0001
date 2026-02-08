# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 08:18:01 2026

@author: shuu
"""

# 9. Python Classes and Inheritance Python 类（Classes）和继承（Inheritance）

class Student: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):      # 手动调用
            print("My name is", self.name, "and I am", self.age, "years old.")
            
    def __str__(self):         # __str__ 方法
        return f"The student name is {self.name} and {self.age} years old"

infor = Student("stan", 19)
infor.introduce()
print(infor)


# -------------------------------子类继承父类
class Animal:                   # 父类通常放的是所有子类都共有的东西
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")

class Dog(Animal):
    def bark(self):
        print(self.name, "is barking!")
        
class Cat(Animal):
    def meow(self):
        print(self.name, "is meowing!")

dog1 = Dog("lushi")
dog1.bark()
dog1.eat()
cat1 = Cat("open door")
cat1.eat()
cat1.meow()

# # --------------------getter and setter 
# class Animal(object):
#     def __init__(self, age):
#         self.age = age
#         self.name = None

#     # Getter 方法（获取属性）
#     def get_age(self):
#         return self.age

#     def get_name(self):
#         return self.name

#     # Setter 方法（设置属性）
#     def set_age(self, newage):
#         self.age = newage

#     def set_name(self, newname=""):
#         self.name = newname

#     # print(对象) 时会调用这个方法
#     def __str__(self):
#         return "animal:" + str(self.name) + ":" + str(self.age)


# # 创建对象
# a = Animal(5)

# # 输出默认状态
# print("初始对象:", a)

# # 使用 getter 获取属性
# print("年龄:", a.get_age())
# print("名字:", a.get_name())

# # 使用 setter 修改属性
# a.set_age(10)
# a.set_name("cat")

# print("修改后对象:", a)

# # 测试默认参数 newname=""
# a.set_name()
# print("名字清空后:", a)


#-------tag 用法
class Animal:
    def __init__(self, age):
        self.age = age


class Rabbit(Animal):
    tag = 1   # 类变量：所有Rabbit共享

    def __init__(self, age, parent1=None, parent2=None):
        super().__init__(age)

        self.parent1 = parent1
        self.parent2 = parent2

        # 给每只兔子分配唯一编号
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def __str__(self):
        return f"Rabbit ID={self.rid}, age={self.age}"
    
    def __add__(self, other):
        # self 是左边 r2
        # other 是右边 r5
        if isinstance(other, Rabbit):
            return Rabbit(self.age + other.age)
        return NotImplemented


# 创建几只兔子
r1 = Rabbit(2)
r2 = Rabbit(3)
r3 = Rabbit(1)
r5 = Rabbit(5)
r7 = r2+r5

print(r1)
print(r2)
print(r3)
print(r5)
print(r7)

# 查看当前 tag 已经增长到多少
print("Current Rabbit.tag =", Rabbit.tag)







