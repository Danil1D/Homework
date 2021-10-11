k = [int(s) for s in input("Введіть будь-які цілі числа через пробіл: ").split()]
sum3 = 1
min1 = max(k)
for b in k:
    if min1 > b > 0:
        min1 = b
for i in k:
    if i % 2 != 0:
        sum3 *= i
if min1 > 0:
    print("Мінімальний додатній елемент: ", min1)
else: 
    print('немає додатнього елемента')
print("Добуток непарних елементів масиву: ",sum3)
if min(k) >= 0:
    print("немає від'ємного елемента")
else:
    for d in k:
        if d < 0:
            print("Виведення від'ємних елементів:", d)
