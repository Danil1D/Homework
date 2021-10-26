#1)
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
list1 = [int(s) for s in input("Введіть будь-які цілі числа через пробіл: ").split()] 
bubble_sort(list1)  
print(list1)

#2)
h = int(input("Введіть ваше значення для пошуку числа: "))
def poshuk1(list1, h):
    for i in list1:
        if list1.index(i):
                return list1[h]
print("Ваше число: ", poshuk1(list1,h))
#3)
k = int(input("Введіть ваше число для пошуку значення: " ))
def poshuk2(list1, k):
    for i in list1:
        if i == k:
                return list1.index(i)
print("Ваше значення елементу: ", poshuk2(list1,k))
        
#4) 
add = list1
def min(list1, add):
    bubble_sort(list1)
    return add[:5]
print("Перші 5 найменших чисел: ", min(list1,add))

#5)
add = list1
def max(list1, add):
    bubble_sort(list1)
    list1.reverse()
    return add[:5]
print("Останні 5 найбільших чисел: " ,max(list1,add))

#6)
def ser(a):
    return (sum(list1)/len(list1))
print("Середнє арифметичне списку чисел: " ,ser(list1))

#7)
def povernenna(list1):
    b = []
    for i in list1:
        if i not in  b:
            b.append(i)
    return b
print(povernenna(list1))