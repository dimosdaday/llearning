#Словарь  коллекция элементов; каждый элемент словаря состоит из пар слов
# Объявление словаря {} или dict()
movie = {
    'хакеры' : 4.5,
    'пятая власть' : 5,
    'трон' : 3.5
}
#print(movie)
#создание через список
movies = [('Слон', 'Моська'), ('Змея','Лев'), ('Змея', '312')]
id_ict= dict(movies)
#print(id_ict)

movas = dict(Гитара = 5, кино = 'домино', Лава = 16)
print(movas)
 
# объявление словаря через метод  dict.fromkeys()
movas_2 = dict.fromkeys(['Слон', 'Моська', 'Змея','Лев'], 5.5)
print(movas_2)

# Упаковка последовательностей и кортежей в zip
mit = ['Слон', 'Моська', 'Змея','Лев']
bit = [15 , 20 , 30, 1  ]
kovan = zip(mit,bit)
print(dict(kovan))

#создание словаря через цикл dict comprehensions
robert = { pip : 'животные' for pip in mit}

# обращение к значению словаря по ключу
#print(robert['Слон'])

# Вложенный словарь
mov_1 = {
    'Матрица': {'rey' : 5.5, 'review' : 'фильм крут'},
    'Трон': {'rey' : 4.5, 'review' : 'так себе'}
}
neo = mov_1['Матрица']
print(neo['rey'], neo['review'])

# проверка ключа в словаре через ветвление
if 'Врата' in mov_1: 
    print('фильм найден')
else:
    print('фильма нет')

# Метод get() обращение к словарю по ключу в аргументе
print(mov_1.get('Трон'))

#Для добавления элемента в словарь нужно новому ключу словаря присвоить значение.
mov_1 ['Кино'] =  {'Перемен' : 4.2}

# замена значений в словаре
movie['хакеры'] = 5.0

# объединение словарей методом update
id_ict.update(movas)

# удаление записей из словаря оператором del
del id_ict['Лава']

#удаляет элемент возвращает значение метод pop() 
id_pop = id_ict.pop('кино', 'ключ утерян')
print(id_pop)

# метод keys возвращает все ключи словаря
keys = id_ict.keys()
print(keys)

# метод values возвращает все значения словаря
val = id_ict.values()
print(val)

# перебор ключей словаря в цикле
for id_1 in id_ict:
    print(id_1)

#перебор значений словаря в цикле
for val in id_ict.values():
    print(f'значения {val}')

# запрос из словаря пары ключ:значение метод items()
print(movie.items())

# распаковка словаря методом items через цикл
for movie_1, reyting_1 in movie.items():
    print(f'фильм {movie_1} получил оценку {reyting_1}')

# очистка словаря методом clear
id_ict.clear()

# Метод copy() создаст независимую копию исходного словаря:
copy_movie = movie.copy()
print(id(movie))
print(id(copy_movie))







recom = {
    'Хенкок' : {'rey' : 3.0, 'review' : 'так себе'},
    'Матрица': {'rey' : 5.5, 'review' : 'фильм крут'},
    'Трон': {'rey' : 4.5, 'review' : 'так себе'}
}
low_reyting = {}
favorit_mov = {}
for mov_3, reyting_2 in recom.items():
    if reyting_2 ['rey'] < 4:
        low_reyting [mov_3] = reyting_2 
        print(f'фильм {mov_3} не интересен {reyting_2["review"]} фильм удален из рекомендаций.')
    elif reyting_2 ['rey'] > 4:
        favorit_mov[mov_3] = reyting_2

for mov_4 in low_reyting:
    if mov_4 in recom:
        del recom[mov_4]

print(recom)
