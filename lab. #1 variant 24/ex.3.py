k = [int(s) for s in input("Введіть будь-які цілі числа через пробіл: ").split()]
sum1 = 0
n = 0
print("Найбільше число в списку, це -", max(k))
for i in k:
    if i % 2 !=0:
        sum1 += i
        n += 1
ser = sum1/n
print("Середнє арефметичне непарних елементів масиву: ", ser)
if min(k) >= 0:
    print("немає від'ємного елемента")
else:
    for d in k:
        if d < 0:
            print("Виведення від'ємних елементів:", d)