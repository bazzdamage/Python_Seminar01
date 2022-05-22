# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
quarter = int(input("enter the quarter of coordinates "))
if quarter not in range(1, 5):
    print(f"quarter (as the name implies) must be 1,2,3 or 4")
else:
    if quarter == 1:
        print(f"points with x > 0 to infinity and y > 0 to infinity belongs I quarter")
    elif quarter == 2:
        print(f"points with x < 0 to -infinity and y > 0 to infinity belongs II quarter")
    elif quarter == 3:
        print(f"points with x < 0 to -infinity and y < 0 to -infinity belongs III quarter")
    else:
        print(f"points with x > 0 to infinity and y < 0 to -infinity belongs IV quarter")
