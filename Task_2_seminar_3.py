# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input("Input the length: "))
lst = []

for j in range(n):
    lst.append(int(input('Input elements of the list: ')))
print(f'{lst} => ', end=' ')


mult = 1
i = 0

while i < len(lst)/2:
    mult = lst[i] * lst[((len(lst)-1)-i)]
    i += 1
    print(mult, end=" ")
