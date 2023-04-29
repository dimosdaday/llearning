class Contact:
    def __init__(self, name, phone, adress, birthday):
        self.name = name
        self.phone = phone
        self.adress = adress
        self.birthday = birthday
        print(f'Создаем новый контакт {name}')

    def show_contac (self):
        print(f'контакт {self.name}, тел. {self.phone}, адр. {self.adress}, день др. {self.birthday}')   

Mike = Contact('Mike', '+7 987 886 15 45', 
               'Россия, Москва, Большая Пироговская, дом 35б, кв. 6',
                 '15.05.1891')

#print(f'Имя конатакта в берлине', Mike.name)
#print(Mike.adress)

Vlad = Contact ('Vlad', '666', 'transilvaniya', '2.3.068')


Vlad.adress = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
#print(Vlad.adress)

#Vlad.show_contac()
import math

class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = 4*math.pi*radius*radius
        self.average_temp_celcius = temp_celsius
        self.average_temp_fahrenheit = temp_celsius*9/5+32
        
    def show_info(self):
        print(f'Планета {self.name}, имеет площадь {self.surface_area} кв.км.') 
        print(f'Средняя температура планеты: {self.average_temp_fahrenheit} по фарингейту')

#Jupiter = Planet('Юпитер', 6991, -108) 

#Jupiter.show_info() 

class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f'{self.name}, ({self.phone})')

class Friend(User):
    def __init__(self, name, phone, adress):
        super().__init__(name, phone)
        self.adress = adress

    def show(self):
        print(f'Имя:{self.name} // тел.{self.phone} // adress:{self.adress}')

#fatcher = User("Отец", "854 66 15")
#son = Friend("Сын", "78552", "Дубровка 15")


#fatcher.show()
#son.show()

from math import radians, sin, cos, acos

class Point:
    def _init_(self, latitude, longtitude):
        self.latitude = radians(latitude)
        self.longtitude = radians(longtitude)

    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(self.longtitude - other.longtitude)
        return 6371*acos(cos_d) 


class City(Point):
    def _init_(self, latitude, longtitude, name, population):
        super()._init_(latitude, longtitude)
        self.name = name
        self.population = population   

        def show_city(self):
            print(f'город {self.name}, население {self.population} чел.') 


class Moutin(Point):
    def _init_(self, latitude, longtitude, name, hieght):
        super()._init_(latitude, longtitude)
        self.name = name
        self.hieght = hieght

    def show_mountin(self):
        print(f'название горы {self.name}, высота горы {self.hieght} м')

        
#ewerest = Moutin(27, 86,'Эверест','8 км')


#ewerest.show_mountin()

# Создали род. класс

class Human:
    def __init__(self, name ):
        self.name = name

    def show(self):
        return self.name

    def answer_question(self):
        print('Хороший вопрос! Следующий вопрос')

# Класс потомок в него добавили метод ask_question()
class Student(Human):
    def __init__(self, name):
        super().__init__(name)
        
# принимает имя и запрос возвращает сообщение и запрос к другому класс, someone.name возвращает имя класса
    def ask_question(self, someone, question):
        print(f'Товарищ {someone.name}, ответь пожалуйста {question}')
        someone.answer_question(question)




    


class Mentor(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self,question):
        if question in 'мне грустненько, что делать':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:    
            return super().answer_question()    

mariy = Mentor('Марина')  
        
vaska = Student('vaska')    
vaska.ask_question( mariy, 'мне грустненько, что делать')


class Cod_reviewer(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if question in 'мне грустненько, что делать':
            print ('Отдохни и возвращайся с вопросами по теории.')
        elif question in 'как устроиться работать питонистом?':
            print('сейчас раскажу')    
        else:
            return super().answer_question()           

georg = Cod_reviewer('Гога')             
vaska.ask_question( georg, 'мне грустненько, что делать')
vaska.ask_question( georg, 'как устроиться работать питонистом?')



print(mariy.name)
#print(georg.show())