from random import choices

def often_words(name):
    dict_often_word = {}
    for i in list(name):
        count = 0
        while i in list(name):
            if i in list(name):
                count += 1
                name.remove(i)
                dict_often_word[i] = count
    dict_often_word = list(dict_often_word.items())
    dict_often_word.sort(key=lambda x: x[1])
    return dict_often_word

print('1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);')
def choice_name(name, n=100):
    return choices(name, k=n)
names = choice_name(['Kate', 'Adam', 'Nataly', 'Lisa', 'John', 'Kate', 'Olga', 'Maria', 'Artem', 'Julia', 'Olga', 'Lisa', 'Maria',
                       'Alex', 'Peter', 'Julia', 'Andrew', 'Kate', 'Sam', 'Garry'])
print(names)

print('2. Напишите функцию вывода самого частого имени из списка на выходе функции F;')
dict = names*1
dict=often_words(dict)
dict.sort(key=lambda x: x[1], reverse=True)
print(dict[0][0])

print('3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.')
dict = names*1
char = []
for i in list(dict):
    for a in i[0]:
        char+=i[0]
char=often_words(char)
print(char[0][0])

print('Другой способ вывода редкой буквы')
dict.sort(key=lambda x: x[1])
print(dict[0][0][0])
