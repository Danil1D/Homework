import csv
import random

k = ["Мурка ", "Нявка ", "Сніжка "]
s = ["з'їла ", "вкрала ", "любить "]
v = ["ковбаску","сир","сухарик"]

i = 1
while i == 1:
    print (random.choice(k)+random.choice(s)+random.choice(v))
    i = float(input("Продовжити? 1 - Так, 2 - Ні  " ))   