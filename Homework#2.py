# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print ('Введите вещественное число:');
a = input()
s = a.split(".")
x1 = int(s[0])
x2 = int(s[1])
print (x1)
print (x2)
sum1 = 0
sum2 = 0

while (x1 !=0):
    sum1 = sum1 + x1%10
    x1 = x1//10
while (x2 !=0):
    sum1 = sum1 + x2%10
    x2 = x2//10

sum = sum1 + sum2
print(sum)

# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

print ('Введите целое число N:');
n = int (input())
list = []
i = 1
import math

if n<=0:
    print ('введено неверное число')
elif n>0:
    while (i<=n):
        list.append(math.factorial(i))
        i+=1

print (list)

# 16. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

print ('Введите целое число N:');
n = int (input())
list = []
i = 1
if n<=0:
    print ('введено неверное число')
elif n>0:
    while (i<=n):
        list.append((1+1/i)**i)
        i+=1
        
new_list = [round(i,2) for i in list]
print (new_list)
print (sum(new_list))

# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите 
#      произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
#      в одной строке одно число.

print ('Введите целое число N:');
n = int (input())
my_list = []
i = 0
if n<=0:
    print ('введено неверное число')
elif n>0:
    while (i<=n*2):
        my_list.append(-n+i)
        i+=1
print(my_list)


with open ('numbers.txt', 'w') as data:
    data.write ('0\n')
    data.write ('1\n')
    data.write ('2\n')
new_list = []
path = 'numbers.txt'
data = open (path, 'r')
for line in data:
    print(int(line))
    new_list.append(my_list[int(line)])
    print(new_list)

    print(sum(new_list))

# файл txt к заданию 17мпочему-то на гит не добавляется. Там на разных строках указаны позиции 0,1,2