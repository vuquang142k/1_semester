#Программа сделана Ву Минь Куанг ИУ7-14Б
#Переписать все отрицательные элементы матрицы X(x,y) в массиве D без пропусков.Упорядочить их в массиве D по убыванию
#Если в матрице нет ни одного отрицательного элемента, то напечагать соответствующий текст
#Напечагать исходную матрицу в виде матрицы и сфор. массив D

 
x=int(input('Введите количество строк: '))
y=int(input('Введите количество столбцов: '))
s=[]
n=[]
print('Введите каждую строку матрицы:')
for i in range(x):
    a=[i for i in input().split()]
    s.append(a)
for i in range(x):
    for j in range(y):
        if float(s[i][j])<0:
            n.append(s[i][j])
print('Матрица X:')
for i in range(x):
    for j in range(y):
        print('{:^5}'.format(s[i][j]),end='')
    print()
print()
if len(n)==0:
    print('В матрице нет ни отрицательного элемента')
else:
    print('Массив D: ',' '.join(n))
    n.sort(reverse=False)
    print('Массив D: ', ' '.join(n))




