# Кортеж это не изменяемый список 

# Объявления кортежа tuple()
package_1 = ('2:00:15', 1500)
print(type(package_1))
# Распаковка кортежа для присвоение переменой
time, steps = package_1
print(time) 

# Упаковка данных в кортеж
package_2 = 'сила', 'пребудет', 'с тобой', 'да'
package_3 = 1500,
print(type(package_3))
print(type(package_2))



not_tuple = (5**5, 4**4, 2**2, 3**3, 5**1)

strd_tup = tuple(sorted(not_tuple))


days = 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница' 
steps= 1000, 3000, 4000, 2000, 500

result =[]
for i in range(len(days)):
    tuple = days[i], steps[i]
    result.append(tuple)
print(result)