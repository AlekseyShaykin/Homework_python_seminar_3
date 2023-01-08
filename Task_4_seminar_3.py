# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

m = int(input('Iput number: '))


def Quantity_of_dev(m):  # кол-во необходимых делений на 2
    i = 0
    while m > 1:
        m = int(m/2)
        i += 1
    return (i)


i = Quantity_of_dev(m)

lst = []
for k in range(i-1):
    m0 = int(m/2)/(2**(i-(k+2)))-int((m/2/2)/(2**(i-(k+2))))*2
    lst.append(int(m0))


# j=1                                         # j = i - n (n - порядковый номер элемента двоичного числа)
# m0 = int(m/2)/(2**j)-int((m/2/2)/(2**j))*2   #универсальная формула
# print(f'm0 = {int(m0)}')


m1 = int(m/(2**i))  # первый элемент
lst2 = [m1]

m3 = m-int(m/2)*2  # последний элемент
lst3 = [m3]

lst4 = lst2+lst+lst3

text = str(lst4)

print(f'{m} ---> ', end='')
for char in text:
    if char.isdigit():
        print(char, end='')
