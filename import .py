#csv — для файлов csv работа с запятыми в БД 
#datetime - преобразования и форматирования даты и времени.
#decimal - точного округления десятичных дробей при арифметических операциях.
#email:разбора структуры email-сообщений, преобразования< связанных с обработкой писем.
#http: модуль интернет-ресурс по протоколу HTTP, отправлять и принимать запросы,  клиент или сервер на Python.
#json — это модуль для работы с популярным и востребованным форматом передачи данных JSON.
#math содержит стандартные функции для математических вычислений.
#os: этот модуль предназначен для взаимодействия с операционной системой.
#ssl - модуль, который позволяет работать с сертификатами ssl, используется для получения html страниц по протоколу https.
#string — этот модуль содержит множество функций для работы со строками. Поддерживает большинство функций, которые есть в других языках, 
# inter - графического интерфейса программ с помощью инструментария Tk GUI

#Подключение библиотек через
def Impo_rt():  
    import decimal
    result = decimal.Decimal('3.0') + decimal.Decimal('4.0')
    print(result)

# переопределение функции в библиотеке 
def func():
    from decimal import Decimal as Dcml
    result = Dcml('3.8') + Dcml('9.9')
    print(result)

# запрос текущего времени datetime.now()
# присвоить дату переиенной
#создаем кортеж



def date_time(name, date):
    from datetime import date as dt
    from datetime import datetime as dtm
    # метод представления произвольной строки в дату strptime(date, format)
    # format (%Y для 2018) (%y для 18) 
    date_1 = dtm.strptime(date,'%d.%m.%Y')
    # метод today() запрашивает сегодняшн дату
    b_d = dt.today() 
    r = b_d.year
    # метод replace() заменяет в объекте date() год на r  
    date = date_1.replace(year=r)
    # метод date() преобразует dtm в формат data    
    if date.date() < b_d:
        date = date_1.replace(year=r+1)
        next_2 = date.date() - b_d
        return f'{name} жди следующий год {next_2} дней' 
    else:
        funni = date.date() - b_d
        return f'{name} до веслеья остался {funni} день' 

H_B_D =  ('Лентик', '19.03.1987'), ('Аня', '18.04.1990')

for un_pac in H_B_D:
    name, date = un_pac 
    print (date_time(name,date))

# присваивание объектв




   


