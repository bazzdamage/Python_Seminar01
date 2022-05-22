# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
import math

print("enter coordinates of point A: ")
a_x = int(input("x of A = "))
a_y = int(input("y of A = "))
print("enter coordinates of point B: ")
b_x = int(input("x of B = "))
b_y = int(input("y of B = "))
distance = round(math.sqrt(math.pow(b_x - a_x, 2) + math.pow(b_y - a_y, 2)), 3)
print(f"distance between point A[{a_x};{a_y}] and B[{b_x};{b_y}] = {distance}")
