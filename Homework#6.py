# 44. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

print ('Введите значение x1:');
x1 = int (input())
print ('Введите значение y1:');
y1 = int (input())
print ('Введите значение x2:');
x2 = int (input())
print ('Введите значение y2:');
y2 = int (input())

a = (x1, y1)
b = (x2, y2)

import cmath 
def length(op, a, b):
    print ('длина отрезка AB равна:', op(a,b))

length(lambda a, b: cmath.sqrt((x2-x1)**2 + (y2-y1)**2), a, b)


#45. Найти сумму чисел списка стоящих на нечетной позиции. 

numbers = list(map(int, input().split()))
print (numbers)
new_nums = list(j for i, j in enumerate(numbers) if i&1) #здесь пробовал через filtr() но не придумал как, не получилось.
print(new_nums)
def calc (list):
    sum = 0
    for i in list:
        sum+=i
    print(sum)

calc(new_nums)

#46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

numbers = list(map(int, input().split()))
print (numbers)
new_nums = [numbers[i]*numbers[-i-1] for i in range(len(numbers)//2 + len(numbers)%2)]

print(new_nums)

#47.Сформировать список из N членов последовательности. Для N=5: 1,-3,9,-27,81 
#(каждый член больше предыдущего в три раза, знак чередуется)

print ('Введите количество членов последовательности N:');
n = int(input())
li = list((-3)**i for i in range(n))
print(li)