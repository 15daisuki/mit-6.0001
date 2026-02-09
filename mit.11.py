# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 15:04:54 2026

@author: shuu
"""

# 11. Understanding Program Efficiency, Part 2
# 估算资源数量

# Bisection Search（二分查找 / 折半查找） 前提：列表必须是 有序的 sorted list。
# 二分查找的递归实现（Implementation 1）
# divide-and-conquer（分治算法）
# 时间复杂度：O(n log n) 每次缩小一半

def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2       # O(log n)
        if L[half] > e:
            return bisect_search1(L[:half], e) # 每次 copy 是 O(n)
        else:
            return bisect_search1(L[half:], e)
L = [1,3,5,7,9,11]
e = 9
exqmple1 = bisect_search1(L, e)
print(exqmple1)

# 二分查找的更好实现方式（Alternative O(log n)
# 不要复制列表，而是用两个变量：
# low：当前搜索范围的左边界
# high：当前搜索范围的右边界

def bisect_search2(L, e):

    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e

        mid = (low + high) // 2

        if L[mid] == e:
            return True

        elif L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)

        else:
            return bisect_search_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)


# 测试
L = [1, 3, 5, 7, 9, 11]
e = 9

example1 = bisect_search2(L, e)
print(example1)

# Logarithmic Complexity（对数复杂度）O(log n)
# 整数转成字符串

def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result

ex3 = intToStr(123)
print(ex3)
print(type(ex3))

# 递归 递归写的阶乘

def fact_recur(n):      # O（n）
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n-1)

# 幂集（Power Set）
# 一个集合的 幂集 = 这个集合的 所有子集（包含空集和全集）。
# 集合 {1,2,3}
# 幂集为 {},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}

# 例：分两种 集合 {1,2,3,4}
# (1) 不包含 4 的子集
# {},{1},{2},{1,2},{3},{1,3},{2,3},{1,2,3} 8种
# (2) 包含 4 的子集
# {4},{1,4},{2,4},{1,2,4},{3,4},{1,3,4},{2,3,4},{1,2,3,4} 8种
# 一共8 + 8 =16

# 如果集合有 n 个元素，那么幂集大小是：2**n


# 生成子集（幂集）的递归算法是指数复杂度 O(2^n)。
def genSubsets(L):
    if len(L) == 0:
        return [[]]

    smaller = genSubsets(L[:-1])       # [1, 2, 3]
    extra = L[-1:]                     # [4]
    new = []

    for small in smaller:
        new.append(small + extra)

    return smaller + new

L = [1,2,3]
print(genSubsets(L))












