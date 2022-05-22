num = int(input("Input a integer number: "))
if num % 30 == 0:
    print("number multiply to 30")
elif num % 15 == 0:
    if num % 10 == 0:
        print("number multiply to 15, 10 and 5")
    else:
        print("number multiply to 15 and 5")
elif num % 10 == 0:
    print("number multiply to 10 and 5")
else:
    if num % 5 == 0:
        print("number multiply only to 5")
    else:
        print("number not multiply to 30, 15, 10 and 5")