import pandas as pd
import matplotlib.pyplot as plt

test =  open('test.txt', 'r', encoding= "utf-8").read().lower()

char_list = list(test)

df = pd.DataFrame({'chars': char_list})
df = df[df.chars != ' ']
df['num'] = 10
df = df.groupby('chars').sum().sort_values('num', ascending=False) / len(df)

plt.bar(df.index, df.num, width=0.5, color='g')
plt.show()
plt.savefig(input('Дайте назву гістограммі: \n'))
print("Ваша гістограмма збережена біля файла .py")