ar = [[1, 2, 3], [1, 2, 4], [1, 1, 1], [6, 6, 6]]
maximum = sum(ar[0])
number = 0
for i in range(1, len(ar)):
    if sum(ar[i]) > maximum:
        maximum = sum(ar[i])
        number = i
print("Row number:")
print(number)
