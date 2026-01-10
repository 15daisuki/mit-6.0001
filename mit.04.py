# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 15:59:50 2026

@author: shuu
"""

# s = "6.00 is 6.0001 and 6.0002"
# new_str = ""
# new_str += s[-1]            # 2
# new_str += s[0]             # 6    
# new_str += s[4::30]         #  
# new_str += s[13:10:-1]      # 100
# print(new_str)

#-------------------------
# def is_even(i):
#     """
#     输入：i，一个正整数
#     返回：如果 i 是偶数，返回 True；否则返回 False
#     """
#     print("inside is_even")          # 每次调用这个函数时，都会打印这一行
#     return i % 2 == 0                # 判断 i 是否能被 2 整除（即是否为偶数）
# print(is_even(3))

# #---------------------------
# def f(x):
#     x = x + 1
#     print('in f(x): x =', x)
#     return x
# x = 6
# z = f(x)

# #---------------------------
# print("All numbers between 0 and 20: even or odd")
# for i in range(20):
#     if is_even(i):
#         print(i, "even")
#     else:
#         print(i, "odd")

# #---------------------------
# def func_a():
#     print('inside func_a')

# def func_b(y):
#     print('inside func_b')
#     return y

# def func_c(z):
#     print('inside func_c')
#     return z()

# print(func_a())   # func_a() 本身不返回值（隐式返回 None）
# print(5 + func_b(2))
# print(func_c(func_a)) # func_c 接收一个函数作为参数，并在内部调用它（z()）

#------------------------------------
# def f(y):
#     x = 1
#     x += 1
#     print(x)
# x = 5
# f(x)
# print(x)

# def g(y):
#     print(x)
#     print(x + 1)
# x = 5
# g(x)
# print(x)
    
# def h(y):
#     global x # 使用全局变量 x
#     x += 1

# x = 5
# h(x)
# print(x)    
    
def g(x):
    def h():              # h() 局部 h 只能在 g 内部被使用
        x = 'abc'
    x = x +1
    print('g: x=', x)
    h()                
    return x

x = 3
z = g(x)              
print(z)























