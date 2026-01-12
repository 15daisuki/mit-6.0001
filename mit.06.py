# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 13:01:16 2026

@author: shuu
"""

#------------------------阶乘的两种方式 Recursion 递归 
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)         # 4 * (3 * (2 * 1))

print(fact(4))   # 输出：24

def factorial_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod
print(factorial_iter(5))

def mult(a,b):          # a*b
    if b == 1:
        return a
    else:
        return a + mult(a,b-1)
print(mult(3,6))

def sum_1(n):                # 0+1+...+n=n * (n + 1) // 2
    return n * (n + 1) // 2
print(sum_1(4))

def sum_2(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print(sum_2(8))

#------------------------------------------ 汉诺塔
move_count = 0

def printMove(from_tower, to_tower):
    global move_count
    move_count += 1
    # print(f"move {move_count:3d}: {from_tower} → {to_tower}")

def hanoi(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        hanoi(n-1, fr, spare, to)
        printMove(fr, to)
        hanoi(n-1, spare, to, fr)

# 执行
move_count = 0
hanoi(4, 'A', 'C', 'B')           # 先用 n=3 测试
print(f"\n总移动次数：{move_count}")

#-------------------------------------斐波那契
def fib(x):
    """ assumes x is an int >= 0
        returns the x-th Fibonacci number """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

# fib(4) = fib(3) + fib(2)  fib(3)=fib(2) + fib(1) fib(2) = fib(1) + fib(0)

def fib_efficient(n, d):
    """
    使用记忆化（字典）计算第 n 个斐波那契数
    参数 d 是字典，用于保存已经计算过的结果
    """
    if n in d:             # 如果已经算过，直接返回保存的结果
        return d[n]
    
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans         # 计算完后把结果存进字典
        return ans


# 使用方式
d = {1: 1, 2: 2}           # 初始已知值（这里采用 fib(1)=1, fib(2)=2 的定义）
print(fib_efficient(20, d)) # 输出

# -------------------------------------------



