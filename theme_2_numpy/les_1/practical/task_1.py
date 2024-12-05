import numpy as np

v = np.arange(1, 11)
print("Оригинальный вектор:", v)

added_v = v + 5       
subtracted_v = v - 7
multiplied_v = v * 2 
squared_v = v ** 4  

print("Вектор после сложения :", added_v)
print("Вектор после вычитания :", subtracted_v)
print("Вектор после умножения :", multiplied_v)
print("Вектор после возведения в квадрат :", squared_v)
