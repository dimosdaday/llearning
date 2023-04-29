#
package =  ('9:36:02', 15000), ('10:40:01', 1000), ('15:00:15', 5000)
from datetime import time as tm
from datetime import datetime as dtm 
from datetime import timedelta as tdelt




# возвращает тайм дату 
def d_tm(time):
    time_l = dtm.strptime(time,'%H:%M:%S')
    time = time_l.time() 
    return time  

# принимает пакет и выдает словарь
def un_package(package):
        # запрос сегодняшней даты
    data_read = dtm.now()
    # объявление словаря для провереных значений времени шагов
    storage_data = {}
    # создание вложеного словаря с провереными значениям
    data_bas = {data_read.strftime('%d-%m-%Y') : storage_data}
    # дата очистки словаря
    now_tm = '23:59:59'
    # дата для цикла
    tm_b = '0:00:00'
    #распаковака провека пакета и присвоение переменых
    for t_cod in package:
        if len(t_cod) != 2 or t_cod[0] is None or t_cod[1] is None:
            return False
        time, steps = t_cod 
        # Условие для очистки значений словаря по времени хранения
        if (dtm.now()).time() > d_tm(now_tm):
            storage_data.clear()
        #проверка пакета на нарушение хронологии    
        elif d_tm(time) < d_tm(tm_b) and storage_data != {}:
            return False 
        elif d_tm(time) > d_tm(tm_b):
            b_d = dict.fromkeys([time], steps)   
            storage_data.update(b_d)
        tm_b = time
    return data_bas
 
#print(un_package(package))
#словарь с ключачи {data : {9:36:02' : 15000}}  
storage_data = un_package(package)
   
# Распаковывает словарь Возвращает список [количество шагов, минут] 
def ttl_stps(dic_t):
    tot_taim = tdelt(minutes=0)
    stps = 0 
    # получение значений из словаря и передача из переменой 
    for dic_v in dic_t.values():
        # извлечение всех значений словаря
        for tm, stp in dic_v.items():
            # инкрементация переменой
            stps += stp 
            # преобразование строки  с временем в список (9, 5, 15)
            key_tdm = tm.split(':')
            # распаковка списка с временем в переменые
            h, m, s = key_tdm
            # передача переменых тайм дельта и смена типа даных на числа
            tot_taim = tdelt(hours=int(h), minutes=int(m), seconds=int(s)) 
            #короткий способ сложения времени часы надо сложить с часами  
            #tot_taim = d_tm(tm).hour + d_tm(tm).minute/60
    tim_cur = tot_taim.total_seconds()/60        
    
    return [stps, tim_cur, tm] 
   # return (tot_taim)
print(ttl_stps(storage_data))

# считает пройденое растояние
def dist(stps): 
    dist = (stps * 0.65) / 1000 
    return dist

# считает калории за сутки
def callorii(list):
    stps, time_curents, tm = list
    height =186 
    weight = 92
    hours = (time_curents)/60
    speed = dist(stps) / hours 
    cal = (weight * 0.035 + (speed**2 / height * 0.029 * weight))*(time_curents)
    return(cal)
      
def achiv(dist):
    if dist >= 6.5:
        return('Отличный результат! Цель достигнута')
    elif dist >= 3.9:
        return('Неплохо! День был продуктивным')
    elif dist >= 2:
        return('Завтра наверстаем')
    elif dist < 2:
        return('Лежать тоже полезно')

      

def show_message(list):
    stps, time_curents, tm = list
    distanc = dist(stps)
    calory = callorii(list)
    print(f'Время: {tm}.')
    print(f'Количество шагов за сегодня: {stps}.')
    print(f'Дистанция составила {distanc} км.')
    print(f'Вы сожгли {calory :.2f} ккал')
    print(f'{achiv(distanc)}')           

show_message(ttl_stps(storage_data))

print('Hellou WORLD')