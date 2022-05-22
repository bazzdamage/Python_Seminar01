# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет,
# является ли этот день выходным.
day_of_week = int(input("Please enter number of day "))
if day_of_week not in range(1, 8):
    print(f"Day {day_of_week} doesn't exist, enter number between 1 and 7")
elif day_of_week in range(1, 6):
    print(f"Day {day_of_week} is workday, get up and go to work!")
else:
    print(f"Day {day_of_week} is weekend, you can sleep a little longer")
