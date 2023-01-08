# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fib(n):
    if n ==1 or n==-1:
        return 1
    elif n==0:
        return 0
    else:
        if n>0:
            return (Fib(n-1))+Fib(n-2)
        else:
            return (Fib(n+2))-Fib(n+1)

n = int(input("Input number: "))
lst = []

for i in range(-n,n+1):
    lst.append(Fib(i))

print(lst)
