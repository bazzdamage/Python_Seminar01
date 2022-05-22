numbers = []
for i in range(5):
    numbers.append(int(input(f"input number {i + 1} ")))

print(len(numbers))
max = numbers[0]
for j in numbers[1:]:
    if j > max:
        max = j

print(f"numbers:\n{numbers}")
print(f"max = {max}")