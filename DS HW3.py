import numpy as np

arr = np.random.randint(-100, 101, 200)

print("Початковий масив:")
print(arr)

positive_mask = arr > 0
positive_numbers = arr[positive_mask]

print("\nДодатні числа:")
print(positive_numbers)

arr[arr < 0] = 0

print("\nМасив після заміни від’ємних чисел на 0:")
print(arr)

average = np.mean(arr)

print("\nСереднє значення масиву:", average)