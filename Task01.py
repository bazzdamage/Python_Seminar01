a = int(input("Please enter number a: "))
b = int(input("Please enter number b: "))
if a < b and a*a == b:
    print(f"{a}^2 = {b}")
elif b < a and b*b == a:
    print(f"{b}^2 = {a}")
else:
    print(f"numbers {a} and {b} are not square of each other")