# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 09:38:13 2026

@author: shuu
"""

# 10. Understanding Program Efficiency, Part 1
# 研究程序（算法）的效率
# 1）我们怎么预测算法需要多少时间？
# 2）算法设计的选择如何影响效率？

# HOW TO EVALUATE EFFICIENCY OF PROGRAMS 如何评估效率
# 1）measure with a timer（用计时器测）
import time

def c_to_f(c):
    return c*9/5 + 32

t0 = time.perf_counter()      # time.perf_counter() 给的是一个“系统计时器的当前值”
c_to_f(100000)
t1 = time.perf_counter() - t0
print(t1)


# 2）count the operations（数操作次数）

def c_to_f(c):
    return c*9.0/5 + 32

def mysum(x):
    total = 0
    for i in range(x+1):
        total += i
    return total

ex1 = mysum(4)
print(ex1)

#----还取决于数据的位置
def search_for_elmt(L, e):
    for i in L:
        if i == e:
            return True
    return False
L = [5, 2, 7, 9]
e1 = 5
e2 = 9
ex2 = search_for_elmt(L,e1) # O(1)
print(ex2)
ex3 = search_for_elmt(L,e2) # O(n) 
print(ex3)



# 3）abstract notion of order of growth（抽象的增长阶）----最适合
# 时间复杂度 Big-O 表示法 比较算法效率并预测大数据性能。

# Best Case / Average Case / Worst Case算法最多会慢到什么程度 常用这个最坏打算
# Big-O 简化口诀 
# 1去掉常数
# 2去掉系数
# 3只保留增长最快的项（最高阶）

# n **2 + 2n + 2         Big-O = O(n ** 2)

# 1）constant（常数） → O(1)
# 2）linear（线性） → O(n)
# 3）quadratic（二次） → O(n²)
# 4）logarithmic（对数） → O(log n)
# 5）n log n → O(n log n)
# 6）exponential（指数） → O(2^n) 或 O(3^n)
# O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n)

# ANALYZING PROGRAMS AND THEIR COMPLEXITY = 分析程序及其复杂度

# Law of Addition（加法法则）

n = 2

for i in range(n):  # Big-O = O(n)
    print('a')

for j in range(n*n):  # Big-O = O(n*n)
    print('b')

# Big-O 的乘法法则（Law of Multiplication），专门用于分析 嵌套循环 nested loops
# 当代码结构是“循环里面还有循环”时，用乘法。

for i in range(n):
    for j in range(n):
        print('a')

# 在无序列表（unsorted list）里做线性查找（linear search）

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

L = [3, 7, 1, 9]
e = 1
ex4 = linear_search(L, e)
print(ex4)

# 在有序列表（sorted list）中做线性查找（linear search）

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

L = [1, 3, 5, 7, 9]
e = 7
ex5 = linear_search(L, e)
print(ex5)

# 无序列表：必须查完整个列表才能确定没有 → O(n)

# 有序列表：遇到比 e 大的就能提前停止 → 平均更快

# 但最坏情况仍然要查 n 个元素 → O(n)

# -----Linear Complexity（线性复杂度）

s = "527"


def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val

ex6 = addDigits(s)
print(ex6)

def fact_iter(n):       # 1 + 3n + 1 = 3n + 2 = O(n)
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


# Quadratic Complexity（二次复杂度）= O(n²)

# 判断 L1 是否是 L2 的子集
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

L1 = [1,2,55]
L2 = [9,8,7,6,5,4,3,2,1]
ex7 = isSubset(L1, L2)
print(ex7)















