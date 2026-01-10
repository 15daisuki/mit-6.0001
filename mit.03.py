# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 12:44:20 2026

@author: shuu
"""

# s = "hello"
# # s[0] = 'y' no
# s= 'y'+s[1:len(s)]  # 从第二个字符开始取到字符串最后”，写成 s[1:]
# print(s)

# an_letters = "aefhilmnorsAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word:")
# times = int(input("Enthusiasm level (1-10):"))

# i = 0
# while i <len(word):
#     char = word[i]
#     if char in an_letters:
#         print("Give me an " + char + "!" + char)
#     else:
#         print("Give me a " + char + "!" + char)
#     i += 1
# print("waht does that spell?")
# for i in range(times):
#     print(word, "!!!")

# ------------------------重复input
# an_letters = "aefhilmnorsAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word:")
# times = int(input("Enthusiasm level (1-10):"))

# for char in word:
#     if char in an_letters:
#         print("Give me an " + char + "!" + char)
#     else:
#         print("Give me a " + char + "!" + char)
# print("waht does that spell?")
# for i in range(times):
#     print(word, "!!!")

# ------------------------ 猜立方根
# cube = 128

# for guess in range(abs(cube) + 1):
#     if guess**3 == abs(cube):
#         break

# if guess**3 == abs(cube):
#     if cube < 0:
#         guess = -guess
#     print(f"Cube root of {cube} is {guess}")
# else:
#     print(f"{cube} is not a perfect cube")
    
# ---------------------二分法 近似立方根 abs(g**3 - 27) < 0.001
cube = 27
epsilon = 0.001 # 精度
num_guesses = 0 # 次数

low = 0
high = float(cube)
guess = (high + low) / 2.0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube: # 猜小了
        low = guess
    else:               # 猜大了
        high = guess
    
    guess = (high + low) / 2.0
    num_guesses += 1

print(f'num_guesses= ={num_guesses}')
print(f'{guess} is close to the cube root of {cube}')












