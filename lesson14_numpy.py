#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

expenses = [0, 312, 4232, 0, 1958, 3062, 1454]
purchases = [0, 1, 5, 0, 3, 5, 4]
cashback = [0, 3, 138, 0, 4, 14, 12]

transactions = np.array([expenses, purchases, cashback])

print(transactions)
print(type(transactions))


# In[5]:


expenses = [0, 312, 4232, 0, 1958, 3062, 1454]
purchases = [0, 1, 5, 0, 3, 5, 4]
cashback = [0, 3, 138, 0, 4, 14, 12]

transactions = np.array([expenses, purchases, cashback])
transactions.ravel()


# In[12]:


# Создайте два списка, которые будут содержать натуральные числа от 1 до 100. Назовите их list_1 и list_2.
# Преобразуйте их в NumPy-массивы, умножьте друг на друга и запишите в переменную result
# Чему равно result[17]?

list_1 = list(range(1,101))
list_2 = list(range(1,101))
array1 = np.array(list_1)
array2 = np.array(list_2)
a3 = array1*array2
a3[17]


# In[15]:


# Создайте единичную диагональную NumPy матрицу шириной 5, превратите ее в одномерный NumPy массив 
# (вспоминаем метод ravel()) и запишите его в переменную list_1.
# Создайте NumPy массив из чисел от 25 (включительно) до 12.5 (не включительно) с шагом -0.5 и запишите его в переменную list_2.
# Перемножьте поэлементно list_1 на list_2 и запишите в result.
# Чему равно result[9]?

list_1 = (np.eye(5)).ravel()
list_2 = np.arange(25,12.5,-0.5)
result = list_2*list_1
result[9]


# In[19]:


# Вам дана обычная матрица в Python: matrix_1 = [[1,2],[3,9]]. Превратите ее в NumPy-матрицу и запишите в переменную matrix_2
# Умножьте matrix_2 на транспонированную matrix_2 и запишите результат в переменную result.
# Найдите сумму всех элементов result.
matrix_1 = [[1,2],[3,9]]
matrix_2 = np.array(matrix_1)
result = matrix_2 * matrix_2.transpose()
np.sum(result)

