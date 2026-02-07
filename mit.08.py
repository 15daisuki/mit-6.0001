# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 10:27:51 2026

@author: shuu
"""

# 8. Object Oriented Programming 面对对象编程

class Car:
    def __init__(self, brand, speed):  # 这里 self 就是 my_car
        self.brand = brand             # my_car.brand = "Toyota"
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} 加速了，现在速度 {self.speed}")

my_car = Car("Toyota", 50)
my_car.accelerate()

# ---CREATING AND USING YOUR OWN TYPES WITH CLASSES 用类创建并使用你自己的数据类型

# Creating the class（创建类）
# 这个类型应该有什么属性和方法？
# class Car:
#     def __init__(self, brand):
#         self.brand = brand


# Using the class（使用类）
# “我现在要造一辆车出来用”
# mycar = Car("Toyota")

# how defind class

# class Coordinate(object):  # or class Coordinate:
    # 定义一个叫 Coordinate 的类，它继承自 Python 最基础的 object 类。

# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def distance(self, other):  # self = c, other = zero
#         x_diff_sq = (self.x - other.x) ** 2 # (3-0)**2 = 9
#         y_diff_sq = (self.y - other.y) ** 2 # (4-0)**2 = 16
#         return (x_diff_sq + y_diff_sq) ** 0.5 # (9 + 16)**0.5 = 5


# # 创建两个点
# c = Coordinate(3, 4)
# zero = Coordinate(0, 0)

# # 输出坐标
# print("c:", c.x, c.y)
# print("zero:", zero.x, zero.y)

# # 计算距离
# print("distance:", c.distance(zero)) # = print(Coordinate.distance(c,zero))

# --------str
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return f"<{self.x},{self.y}>"


c = Coordinate(3, 4)
print(c)
print(Coordinate)         # 说明 Coordinate 本身是一个 类对象
print(type(Coordinate))   # Coordinate 这个类，本身也是一个对象 类型是 type

print(isinstance(c, Coordinate)) # isinstance 用来判断对象是不是某个类的实例

# -------特殊运算符（Special Operators）/ 魔术方法（dunder methods）

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x},{self.y}>"

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

c1 = Coordinate(3, 4)
c2 = Coordinate(1, 2)

print(c1)          # 调用 __str__
print(c1 + c2)     # 调用 __add__
print(c1 - c2)     # 调用 __sub__
print(c1 == c2)    # 调用 __eq__
print(c2 < c1)     # 调用 __lt__

# ------例子 定义一个表示风速矢量的类
class Velocity:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    # 重载 + 运算符
    def __add__(self, other):
        return Velocity(self.u + other.u, self.v + other.v, self.w + other.w)

    # 重载 * 运算符（实现标量乘法）
    def __mul__(self, scalar):
        return Velocity(self.u * scalar, self.v * scalar, self.w * scalar)

    def __repr__(self):
        return f"Velocity(u={self.u}, v={self.v}, w={self.w})"

# 使用
v1 = Velocity(1.0, 0.0, 0.0)
v2 = Velocity(0.5, 2.0, -1.0)
v3 = v1 + v2  # 自动触发 __add__
print(v3)     # 自动触发 __repr__










