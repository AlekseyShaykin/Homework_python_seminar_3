# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.(если получаются длинные числа после запятой,
# это нормально и особенность данного языка программирования. ваш ответ может не совпадать
# с примером(может получитя 0,20))

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst1 = [1.1, 1.2, 3.1, 5.8, 10.01]
print(f'исходный список из вещественных элементов: {lst1}')

# Убираем целые числа из всех элементов списка lst1
lst2 = []
for i in range(len(lst1)):
    lst1[i] = lst1[i] - int(lst1[i])
    lst2.append(lst1[i])


def Max_method(list5):
    i =0
    max = list5[0]
    while i < (len(list5)-1):
        if list5[i+1] > max:
            max = list5[i+1]
        i+=1
    # print(max)
    return max

def Min_method(list5):
    i = 0
    min = list5[0]
    while i < (len(list5)-1):
        if list5[i+1] < min:
            min = list5[i+1]
        i+=1
    # print(min)
    return min

max1 = Max_method(lst2)
min1 = Min_method(lst2)

deviation = round((max1 - min1), 3)
print(f'Разница между максимальным  и минимальным значением дробной части элементов составляет {deviation}')



print()
print('2-й способ: ')
print()
# 2 способ поиска максимального и минимального элемента в списке

max_number = max(lst2)
print(f"Максимальное число в списке: {max_number}")

min_number = min(lst2)
print(f"Минимальное число в списке: {min_number}")

deviation1 = round((max_number - min_number), 3)
print(f'Разница между максимальным  и минимальным значением дробной части элементов составляет {deviation1}')