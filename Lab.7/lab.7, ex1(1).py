#Variant №1
# Y(x)=x*sin(5*x), x=[-2...5]

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-2, 5)
y = x * np.sin(5*x)

fig, ax = plt.subplots()
plt.plot(x,y)
plt.show()

fig.savefig(input('Дайте назву графіку: \n'))
print("Ваш графік збереженний біля файла .py")
