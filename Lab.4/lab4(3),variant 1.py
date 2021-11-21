import re
a = 0
document_text = open('Стивен Кинг.txt', 'r', encoding= "utf-8").read().lower()  # Используйте тест на русском или украинском языке
match_pattern = re.findall(r'\b[а-я]{3,30}\b', document_text)

for words in match_pattern:
    b = int(f' {match_pattern.count(words)}')
    k = ( f'{words}')
    if b > a:
        a = b
        d = k
print("Найдовша послідовність слів: ",a)
print("Із слова: ", [d])