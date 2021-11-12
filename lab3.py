import csv
import io

#запис у файл
print("FirstGroup.txt")
f1 = "FirstGroup.txt"
fd = open(f1, "w")
fd.write("St - 5\n")
fd.write("St - 8\n")
fd.write("St - 10\n")
fd.write("St - 9\n")
fd.close()
import os


#дозапис у файл 1
fd = open(f1, "a")

or12 = int(input('Ви хочете додати студента в список? (1 - Так, 2 - Ні)\n '))
if or12 == 1:
    a = input("Введіть ім'я студента:")
    b = input("Введіть його середню оцінку:")
    fd.write(a+" - "+b)   
else:
    fd.close()

#читання файлу
fd = open(f1, "r")
reader = csv.reader(fd, delimiter = "\t")
for str in reader:
    print(str)
fd.close()

#запис у файл
print("SecondGroup.txt")
f2 = "SecondGroup.txt"
fd = open(f2, "w")
fd.write("St1 - 6\n")
fd.write("St2 - 4\n")
fd.write("St3 - 11\n")
fd.write("St4 - 12\n")
fd.close()

#дозапис у файл 2
fd = open(f2, "a")

or1 = int(input('Ви хочете додати студента в список? (1 - Так, 2 - Ні)\n '))
if or1 == 1:
    a = input("Введіть ім'я студента:")
    b = input("Введіть його середню оцінку:")
    fd.write(a+" - "+b)    
else:
    fd.close()

#читання файлу
fd = open(f2, "r")
reader = csv.reader(fd, delimiter="\t") 
for str in reader: 
 print(str) 
fd.close()

#Пошук слова
a = int(input("Оберіть файл ('FirstGroup.txt' - 1, 'SecondGroup.txt' - 2)\n"))
k = True

while k:
    if a == 1:
        fs = open(f1).read()
        f = open(f1)
    if a == 2:
        fs = open(f2).read()
        f = open(f2)
    if a!=1 and a!=2:
        print("Файла з відповідністю такій цифрі немає.") 
        break

    w = input("Введіть ім'я студента, щоб побачити його середній бал:\n")

    if w in fs:
        for i in f.readlines():
            if i.find(w) > -1:
                print(i.strip())
                k = False
                break
    else:
        print("Такого студента немає у списку")