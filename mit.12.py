# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 20:04:47 2026

@author: shuu
"""

# 12. Searching and Sorting

# Monkey Sort（猴子排序） n!（n 的阶乘）
# 把数组随机打乱（shuffle）检查是否已经按从小到大排好如果没排好，就继续随机打乱直到碰巧排好为止

# Bubble Sort（冒泡排序 / 气泡排序）。 平均/最坏：O(n²)
# 核心思想：不断比较相邻两个元素，如果顺序错了就交换。

def bubble_sort(L):
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


testList = [1,3,5,7,2,6,25,18,13]
print(bubble_sort(testList))
print(testList)


# 选择排序（Selection Sort）的复杂度 O(n²)

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

# Merge Sort（归并排序）
# 分治法 divide and conquer 把一个大问题拆成很多小问题，解决小问题后再合并起来。
# 1）divide（拆分） log2​(n)
# 2）merge（合并）   O(n)
# Merge Sort 就是：一直对半拆到单个元素，再一步步合并成有序数组。

list1 = [1,5,12,18,19,20]
list2 = [2,3,4,17]

# compare1 = 1, 2
# result1 = []
# compare2 = 5, 2
# result2 = [1]
# compare3 = 5, 3
# result3 = [1,2]

# Merge Sort 里“合并两个有序子列表”的代码实现（merging sublists step）

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right): # 比较两个列表的开头元素
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

left = [1, 5, 12, 13, 33]
right = [2, 3, 10]

print(merge(left, right))




















