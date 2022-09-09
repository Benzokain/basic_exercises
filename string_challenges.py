from collections import Counter
from itertools import count
# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(Counter(word.lower())['а'])


# Вывести количество гласных букв в слове
word = 'Архангельск'
letters = 'аеёоуыэюя'
count = 0
for letter in word:
    if letter in letters: count+=1
else:
    print(f'Количество класных букв {count}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
lenght = 0
for word in sentence.split():
    lenght+= len(word)
else:
    print(f'Средняя длина слова в предложении {lenght//len(sentence.split())}')

