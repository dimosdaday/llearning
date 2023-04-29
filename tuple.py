"""Можества это не упорядоченые колллекции Set"""

movie = {4.3, 5.0, 4.1, 6, 3}
print(movie)    
# Преобразование списка в множество 
movies = ['Матрица', 'Сеть', 'Трон', 'Cеть']
unicorp = set(movies)
print(unicorp)

# метод replace заменяет пробелы set преобразовывает в уникальное множество   
not_unic = 'Съешь еще этих французких булок и выпей чаю'
unic = not_unic.replace(' ', '')
c = len(unic) - len(set(unic))
print(c)

# библиотека времени, и добавление в множество через метод add
"""import time
num_set = set()
for num in range(10**6):
    num_set.add(num)
start_time = time.time()
if 954999 in num_set:
    print(True)
print((time.time() - start_time))"""

# удаление из множества методом remove() и discard

maxi_toys = {'Самолет', 'Игрушка ', 'Кубики', 'Скалка', 'Фонарик'}
maxi_toys.remove('Скалка')
maxi_toys.discard('Самолет')
print(maxi_toys)

# Метод pop()  удаляет случайный член множество и возвращает его
toy = maxi_toys.pop()
print(f'куда пропали {toy}')
print(f'а кто остался {maxi_toys}')

#метод clear() для очистки множества
#maxi_toys.clear()
#print(maxi_toys)

# обнаружение пересечений в множествах & intersection
maxi_toys = {'Самолет', 'Игрушка', 'Кубики', 'Скалка', 'Фонарик'}
iva_toys = {'Лапочка', 'Дочка', 'Фонарик', 'Игрушка'}
toys = maxi_toys & iva_toys
#print(toys)
inter_toy = maxi_toys.intersection(iva_toys)
print(inter_toy)

# объединение множеств спомощью |, или метода union() 
uico = maxi_toys | iva_toys
toy_baby = maxi_toys.union(iva_toys)

print(toy_baby)

# вычитание множеств литералом '-' или методом diference
razn = maxi_toys - iva_toys
diff = maxi_toys.difference(iva_toys)
print(diff) 

# Симметрическая разность symmetric_dyfference
sim_diff = maxi_toys ^ iva_toys
sim_diff_2 = maxi_toys.symmetric_difference(iva_toys)
print(sim_diff_2)

col_1 = '100 25 50 60 50 30 15 30 40'
col_2 = '200 150 38 42 45 68 74 32 15'
new_cl1 = set(col_1.split())
new_cl2 = set(col_2.split())
print(len(new_cl2 & new_cl2)) 

# Функция сортировки множесва в список sorted

id_string = '32 40 50 60 30 50 18 20 38 15 16 77'
def serch (id_string):
    List_id = list(id_string.split())
    Set_id = set()
    for id in List_id:
      if id in Set_id:
         print(f'Найден дубликат id {id}') 
      Set_id.add(id)    
    print(sorted(Set_id))
   

serch(id_string)