# 2. Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
import itertools
print("statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\n")
count_true = 0
count_false = 0


def statement_equality(predicats):
    x = int(predicats[0])
    y = int(predicats[1])
    z = int(predicats[2])
    left_part = not(x or y or z)
    right_part = not x and not y and not z
    print (f"left part = {left_part}\nright part = {right_part}\n")
    if left_part == right_part:
        print(f"statement with x = {x}, y = {y}, z = {z} are equal\n")
        global count_true
        count_true += 1
    else:
        print(f"statement with x = {x}, y = {y}, z = {z} are NOT equal\n")
        global count_false
        count_false += 1


for i in itertools.product('01', repeat=3):
    statement_equality(i)


print(f"statement was equal {count_true} times\nand not equal {count_false} times ")