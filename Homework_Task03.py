# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
print("enter the coordinates of Point (x and y)")
x = int(input("x = "))
y = int(input("y = "))
if x == 0:
    if y == 0:
        print(f"Point [x:{x};y:{y}] lies in center of axes")
    elif y < 0:
        print(f"Point [x:{x};y:{y}] lies on axis y between III and IV quarters")
    elif y > 0:
        print(f"Point [x:{x};y:{y}] lies on axis y between II and I quarters")
if y == 0:
    if x < 0:
        print(f"Point [x:{x};y:{y}] lies on axis x between II and III quarters")
    elif x > 0:
        print(f"Point [x:{x};y:{y}] lies on axis x between I and IV quarters")
if x > 0:
    if y > 0:
        print(f"Point [x:{x};y:{y}] lies in I quarter")
    else:
        print(f"Point [x:{x};y:{y}] lies in IV quarter")
if x < 0:
    if y > 0:
        print(f"Point [x:{x};y:{y}] lies in II quarter")
    else:
        print(f"Point [x:{x};y:{y}] lies in III quarter")
