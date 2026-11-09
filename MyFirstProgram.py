numbers = [20, 2, 7, 6, 20, 13, 6, 2]
repeats = []
for i in numbers:
    if numbers.count(i) > 1 and i not in repeats:
        repeats.append(i)
print("Duplicates:")
for num in repeats:
    print(num)
