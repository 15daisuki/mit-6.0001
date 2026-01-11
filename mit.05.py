# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 13:11:23 2026

@author: shuu
"""

# def quotient_and_remainder(x, y):
#     q = x // y          # 整除（地板除），得到商
#     r = x % y           # 取余，得到余数
#     return (q, r)       # 返回一个包含(商, 余数)的元组
# (quot, rem) = quotient_and_remainder(7,2 )
# print(quot,rem)

# L = [5,7,2,8,44,2,7,5,0]
# L.append(2)  # 在列表末尾添加单个元素
# print(L)
# L.pop(9) # 移除并返回指定位置的元素
# print(L)
# L.remove(7) # 移除列表中第一个匹配的值
# print(L)
# del L[0:4]
# print(L)

# s = "I,3 dsd,kind"
# list(s)
# d = s.split(',')         # split() 把字符串按分隔符拆分成列表 
# L = ['a','b','c']
# k = "~".join(L)          # "-".join() 把可迭代对象（通常列表）用分隔符连接成字符串
# print(L)
# print(d)
# print(k)

# num = [2,5,7,1,3,2,5,7,9]
# num.sort()                 # lst.sort()
# print(num)

# num = [2,5,7,1,3,2,5,7,9]
# new_num = sorted(num)        # sorted()：产生新列表，原列表不变
# print(new_num)
# print(num)
# desc = sorted(num, reverse=True) # 降序
# print(desc)

num = [2,5,7,1,3,2,5,7,9]
num.reverse()              # 反转列表
print(num)

warm = ['red', 'yellow', 'orange']      # 创建一个列表对象
hot = warm                              # hot 指向同一个列表对象（别名）
                                        # 把 warm 现在指向的那个对象，也给 hot 这个名字贴上
                                        # → 现在同一个列表对象同时被两个名字（warm 和 hot）引用
                                        # 这就是“别名（alias）”的真正含义

hot.append('pink')                      # 通过 hot 修改列表内容
                                        # → 同一个列表被加了 'pink'

print(hot)     # ['red', 'yellow', 'orange', 'pink']
print(warm)    # ['red', 'yellow', 'orange', 'pink']  ← 也变了！
"""hot = warm 并没有复制列表，只是让两个变量名指向同一个内存中的列表对象。
修改列表内容时，所有指向它的变量名都会“看到”相同的变化。"""

# Cloning a list 安全地获取列表的独立拷贝
color = ['blue', 'green', 'grey']
a = color[:]                  # 切片操作 [:] 创建了一个新的、独立的列表
color.append('black')
print(a)
print(color)




