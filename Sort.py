import numpy as np
import random
def bubble(ln):   #Параметр длины списка
    print('Bubble sort:--------------------------------------------------------------------')
    global A            #Выбор А созданной в глобальной программе
    global ch
    bub_count=0
    tg=True
    i=0           #Переменная для подсчета кол-ва итераций
    bub_push=0
    if ch == 1:          #Ascending
        while tg:
            tg=False          
            for j in range(ln-i-1):   # i тут для оптимизации кол-ва итераций
                bub_count+=1        #Подсчет кол-ва сравнений
                if A[j] > A[j+1]:
                    A[j],A[j+1]=A[j+1],A[j]
                    bub_push+=1     #Подсчет кол-ва перестановок
                    tg=True
            i+=1
        print(f' Number of checks for Bubble:{bub_count}')
        print(f' Number of pushes for Bubble:{bub_push}')
        return A
    elif ch == 2:        #Descending
        while tg:
            tg=False
            for j in range(ln-i-1):    # i тут для оптимизации кол-ва итераций
                bub_count+=1        #Подсчет кол-ва сравнений
                if A[j] < A[j+1]:
                    A[j],A[j+1]=A[j+1],A[j]
                    bub_push+=1     #Подсчет кол-ва перестановок
                    tg=True
            i+=1
        print(f' Number of checks for Bubble:{bub_count}')
        print(f' Number of pushes for Bubble:{bub_push}')
        return A
def selection(ln):
    global A
    global ch
    sel_count=0
    sel_replace=0
    print('Selection sort:-----------------------------------------------------------------')
    if ch==1:               #Ascending
        for i in range(ln-1):
            mn=i      #Выбор самого первого элемента как минимальный, для сравнения с последующими
            for j in range(i+1,n):
                sel_count+=1    #Подсчет кол-ва сравнений
                if A[j] < A[mn]:
                    mn=j
                    sel_replace+=1   #Подсчет подстановок в минимум
            A[i],A[mn]=A[mn],A[i]
    elif ch==2:             #Descending
        for i in range(ln-1):
            mn=i      #Выбор самого первого элемента как минимальный, для сравнения с последующими
            for j in range(i+1,n):
                sel_count+=1    #Подсчет кол-ва сравнений
                if A[j] > A[mn]:
                    mn=j
                    sel_replace+=1   #Подсчет подстановок в минимум
            A[i],A[mn]=A[mn],A[i]
    print(f' Number of checks for Selection:{sel_count}')
    print(f'Number of replacements for Selection:{sel_replace}')
    return A
def linsertion(ln=100000):   #Параметр по умолчанию
    global A
    global ch
    lin_push=0
    lin_replace=0
    print('Linear Insertion sort:----------------------------------------------------------')
    if ch==1:               #Ascending
        for i in range(1,ln):
            j=i-1
            key=A[i]
            while j>=0 and A[j]>key:
                lin_push+=1
                A[j+1]=A[j]
                j-=1
            lin_replace+=1
            A[j+1]=key
    elif ch==2:             #Descending
        for i in range(1,ln):
            j=i-1
            key=A[i]
            while j>=0 and A[j]<key:
                lin_push+=1
                A[j+1]=A[j]
                j-=1
            lin_replace+=1
            A[j+1]=key
    print(f'Number of pushes for Linear Insertion sort:{lin_push}')
    print(f'Number of replacements for Linear Insertion sort:{lin_replace}')
    return A
def binsertion(ln): 
    global A
    global ch
    bin_replace=0
    bin_count=0
    print('Binary Insertion sort:----------------------------------------------------------')
    if ch==1:           #Ascending
        for i in range(1,ln):
            x=A[i]
            l=0
            r=i-1
            bin_count+=1       
            while l<=r:
                m=(l+r)//2
                bin_count+=1
                if x<A[m]:
                    r=m-1
                else:
                    l=m+1
            for j in range(i-1, l-1,-1):
                bin_replace+=1
                A[j+1]=A[j]
            bin_replace+=1
            A[l]=x
    if ch==2:           #Descending
        for i in range(1,ln):
            x=A[i]
            l=0
            r=i-1
            bin_count+=1
            while l<=r:
                m=(l+r)//2
                bin_count+=1
                if x>A[m]:
                    r=m-1
                else:
                    l=m+1
            for j in range(i-1, l-1,-1):
                bin_replace+=1
                A[j+1]=A[j]
            bin_replace+=1
            A[l]=x
    print(f'Number of checks for Binary Insertion sort:{bin_count}')
    print(f'Number of replacements for Binary Insertion sort:{bin_replace}')
    return A
var=int(input('Random array: press 1 | User array: press 2\nPrint:'))
if var==1:
    A=np.zeros(100000,dtype=int)
    for i in range(100000):
        A[i]=random.randint(0,100000)
elif var==2:
    A=np.zeros(30,dtype=int)
    for i in range(30):
        A[i]=int(input(f'A[{i}]='))
n=len(A)
print(A)
csort=int(input('Choose your fighter:\n Bubble: press 1 | Selection: press 2 | Linear Insertion: press 3\n Binary Insertion: press 4\nPrint:'))
ch=int(input('Ascending: press 1 | Descending: press 2\nPrint:'))
if csort==1:
    bub_sort = bubble(n)          #Вызов функции с параметром длины(Обязательный параметр)
    print(bub_sort)     
elif csort==2:
    sel_sort = selection(ln=n)    #Вызов функции с поименованным параметром
    print(sel_sort)
elif csort==3:
    lins_sort = linsertion()      #Вызов функции с параметром по умолчанию
    print(lins_sort)
elif csort==4:
    bins_sort = binsertion(n)
    print(bins_sort)




    
