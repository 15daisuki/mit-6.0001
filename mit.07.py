# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 20:20:25 2026

@author: shuu
"""

# 1) Unit Testing（单元测试）
# 2) Regression Testing（回归测试）
# 3) Integration Testing（集成测试）

# --------黑盒测试------不看代码，只管输入输出
def sqrt(x, eps):
    """Assumes x, eps floats, x >= 0, eps > 0"""

# 边界值（boundary）

# 正常值（normal）
# 特殊值（perfect square）
# 小数范围（0~1）
# 复杂值（无理数）
# 极端值（非常大/非常小）

# -----------玻璃盒测试------看代码内部逻辑，专门针对 if/else、循环、分支写测试
def shipping_cost(weight):
    cost = 0
    
    if weight <= 0:
        return 0
    
    if weight < 5:
        cost = 10
    else:
        cost = 20

    for i in range(int(weight)):
        cost += 1

    return cost

print(shipping_cost(7))


#-------异常（Exception）----------
# try 里放“可能会出错的代码”，    except 里放“出错后的补救措施”，
# try:
#     a = int(input("Tell me one number:"))
#     b = int(input("Tell me another number:"))
#     print(a/b)

# except:
#     print("Bug in user input.")


# 直接抛出异常（raise exception）
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b cannot be 0") # raise <exceptionName>(arguments)
    return a / b
try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("发生错误:", e)









