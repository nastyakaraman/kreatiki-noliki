# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:07:43 2022

@author: User
"""

import random
import sys

#cоздаем словарь с комбинациями для игры компьютера - занятыми и свободными
comb={'all': [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                     (1, 4, 7), (2, 5, 8), (3, 6, 9),
                     (1, 5, 9), (7, 5, 3)],
      'available': [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                     (1, 4, 7), (2, 5, 8), (3, 6, 9),
                     (1, 5, 9), (7, 5, 3)],
      'python_priority': [(4, 5, 6),(2, 5, 8),
                       (1, 5, 9), (7, 5, 3)],
      'busy':[]}
#cоздаем словарь для игрового поля - сюда будем добавлять свободные и занятые ячейки
igrovoe_pole={'all': [1,2,3,4,5,6,7,8,9], #все существующие ячейки на игровом поле
              'available': [1,2,3,4,5,6,7,8,9], #доступные ячейки на игровом поле
              'busy': [], #занятые ячейки на игровом поле
              'py_igrok':[], #занятые ячейки Питона на игровом поле
              'human_igrok':[], #занятые ячейки игрока на игровом поле
              'pole': [1,2,3,4,5,6,7,8,9]} #как выглядит игрвоое поле

#cоздаем функцию для вывода игрового поля на экран
def print_igrpole(list_):
    str1=' '
    str2=' '
    str3=' '
    for i in range(len(list_)):
        if i<3:
            str1=str1+str(list_[i])+ '  '
        elif i>=3 and i<6:
            str2=str2+str(list_[i])+ '  '
        else:
            str3=str3+str(list_[i])+ '  '
    itog='\n' + ' _______'+ '\n'+'\n' +str1+'\n'+str2+'\n'+str3 + '\n'+ ' _______'+ '\n'
    return print(itog)
    
    
#определяем с помощью рандомайзера, что достанется игроку - крестики или нолики
print('Приветствую, игрок. Сейчас мы выберем, достанутся тебе крестики или нолики')
n=int(input('Введи любое целое число: '))
#выбираем рандомное число от 0 до числа с консоли
r=random.randint(0,n)
#если оно четное, присваиваем крестики, если нечетное - нолики
if r%2==0:
    igrok='x'
    igrok_python='о'
else:
    igrok = 'о'
    igrok_python='x'
print('Тебе достались', igrok)

print('Ознакомьcя с игровым полем:')
print_igrpole(igrovoe_pole['pole'])
print('Оно имеет размерность 3х3. Для того чтобы сделать ход, необходимо выбрать нужную "ячейку"')

#спрашиваем игрока, готов ли он продолжать игру. если нет, выключаем скрипт
usl1=input('Готов играть? Напиши да или нет:\n')
if usl1=='нет':
    sys.exit()
    
#переменная, которую мы будем проверять, чтобы продождать игру
grand_usl=1


#функция, которая закончит игру, когда игровое поле заполнится
def game_finish(list_):           
    if len(list_)==9:
        return 0
        print('Игра окончена')
        sys.exit()
    else:
        return 1

#функция, проверяет, появилась ли на поле выигрышная комбинация и определяет победителя
def winner_check(pole_,comb_):
    n=[]
    if len(pole_['busy'])>4:
        for tpl in comb_['all']:
            if tpl[0] in pole_['py_igrok'] and tpl[1] in pole_['py_igrok'] and tpl[2] in pole_['py_igrok']:
                n.append(int(0))
            elif tpl[0] in pole_['human_igrok'] and tpl[1] in pole_['human_igrok'] and tpl[2] in pole_['human_igrok']:
                n.append(int(1))
            else:
                n.append(int(100))
    if int(0) in n:
        return 0 #если победитель-питон
    elif int(1) in n:
        return 1 #если победитель-игрок
    else:
        return 100 #если победителя пока нет

#функция, с помощью которой питон попробует переиграть человека
def win_human (pole_,comb_):
    n_hu=[] #здесь будет определяться ячейка, чтобы не дать человеку выйграть
    n_py=[] #здесь будет определяться ячейка, чтобы не пропустить свой выйгрыш
    num=0

    #сначала проверим свои шансы на выйгрыш
    if len(pole_['py_igrok'])>1:
        for tpl in comb_['all']:
            if tpl[0] in pole_['py_igrok'] and tpl[1] in pole_['py_igrok']:
                n_py.append(tpl[2])
            elif tpl[1] in pole_['py_igrok'] and tpl[2] in pole_['py_igrok']:
                n_py.append(tpl[0])
            elif tpl[0] in pole_['py_igrok'] and tpl[2] in pole_['py_igrok']:
                n_py.append(tpl[1])
            else:
                n_py.append(int(0))
    
    for i in range(len(n_py)):
        if n_py[i] and n_py[i] in pole_['available']:
            num=n_py[i]
            
    if num:
        return (num)
    else:
        #теперь посмотрим, может ли человек выйграть в следующем ходе
        if len(pole_['human_igrok'])>1:
            for tpl in comb_['all']:
                if tpl[0] in pole_['human_igrok'] and tpl[1] in pole_['human_igrok']:
                    n_hu.append(tpl[2])
                elif tpl[1] in pole_['human_igrok'] and tpl[2] in pole_['human_igrok']:
                    n_hu.append(tpl[0])
                elif tpl[0] in pole_['human_igrok'] and tpl[2] in pole_['human_igrok']:
                    n_hu.append(tpl[1])
                else:
                    n_hu.append(int(0))
        for i in range(len(n_hu)):
            if n_hu[i] and n_hu[i] in pole_['available']:
                num=n_hu[i]
        if num:
            return (num)
        else:
            return (0)
    
    
#функция, которая преобразоывает словарь игровых ячеек при осуществлении хода
#на входе - словарь игровых ячеек и номер новой ячейки, чей ход, переменные крестики-нолики игроков
def igrovoe_pole_change (dic,num,hod_,ig,igp):
    if hod_:
        dic['human_igrok'].append(igrovoe_pole['all'][num-1])
        if ig=='x':
            dic['pole'][num-1]='x'
        else:
            dic['pole'][num-1]='о'
    else:
        dic['py_igrok'].append(igrovoe_pole['all'][num-1])
        if igp=='x':
            dic['pole'][num-1]='x'
        else:
            dic['pole'][num-1]='о'
    dic['busy'].append(igrovoe_pole['all'][num-1])
    dic['available'].remove(igrovoe_pole['all'][num-1])
    return print_igrpole(dic['pole'])
    
    
#функция для редактирования словаря комбинаций
#на вход - два списка с кортежами комбинаций и список занятых ячеек, которые мы проверяем
def comb_reorg(available, busy, igrok_num):
    for i in range(len(available)):
        for num in igrok_num:
            if num in available[i]:
                if available[i] not in busy:
                    busy.append(available[i])
            
    for element in busy:
        if element in available:
            available.remove(element)

#переменная, которую мы будем проверять, чтобы понять, кто ходит 1-игрок, 0-питон
if igrok=='x':
    hod=1
else:
    hod=0
    
#первый ход     
if hod:
    grand_usl=game_finish(igrovoe_pole['busy'])
    print('\nТвой ход первый')
    print_igrpole(igrovoe_pole['pole'])
    nomer=int(input('Введи номер ячейки для осуществления хода (без ковычек и прочего): '))
    igrovoe_pole_change (igrovoe_pole,nomer,hod, igrok, igrok_python)
    comb_reorg(comb['python_priority'], comb['busy'], igrovoe_pole['human_igrok'])
    hod=0
else:
    grand_usl=game_finish(igrovoe_pole['busy'])
    print('Ходит Питон')
    nomer=int(5) #начать игру с центра поля - выигрышная комбинация
    igrovoe_pole_change (igrovoe_pole,nomer,hod, igrok, igrok_python)
    hod=1
    

#цикл для проведения дальнейшей игры 
while grand_usl:
    
    #проверяем, не заполнилось ли поле
    #grand_usl=game_finish(igrovoe_pole['busy'])
    
    #проверяем, есть ли на игровом поле победитель
    if winner_check(igrovoe_pole,comb)==1:
        print ('Ты выиграл')
        break
    elif winner_check(igrovoe_pole,comb)==0:
        print ('Выиграл Питон')
        break
    elif not game_finish(igrovoe_pole['busy']):
        print ('Ничья')
        grand_usl=game_finish(igrovoe_pole['busy'])
        break
    else:
        print('Следующий ход')
    
    if hod:
        print('Ты ходишь')
        nomer=int(input('Введи номер свободной ячейки для осуществления хода (без ковычек и прочего): '))
        if nomer not in igrovoe_pole['available']:
            print('Будь внимательнее - эта ячейка уже занята')
            nomer=int(input('Введи номер свободной ячейки для осуществления хода (без ковычек и прочего): '))
        igrovoe_pole_change (igrovoe_pole,nomer,hod, igrok, igrok_python)
        comb_reorg(comb['available'], comb['busy'], igrovoe_pole['human_igrok'])
        hod=0
        
    else:
        print('Ходит Питон')
        
        #если первый ход был у игрока и он не поставил крестик в центр поля
        if len(igrovoe_pole['busy'])==1 and 5 in igrovoe_pole['available']:
            nomer=int(5)
            
        #если было два хода и первым питон поставил пятерку
        elif len(igrovoe_pole['busy'])==2 and 5 in igrovoe_pole['py_igrok']:
            comb_reorg(comb['python_priority'], comb['busy'], igrovoe_pole['human_igrok'])
            r=random.randint(0,len(comb['python_priority'])-1)
            python_comb=comb['python_priority'][r]
            for element in python_comb:
                if element in igrovoe_pole['available']:
                    nomer=int(element)
        
        else:
            if win_human (igrovoe_pole,comb):
                nomer=win_human (igrovoe_pole,comb)
            elif len(igrovoe_pole['available'])==1:
                nomer=igrovoe_pole['available'][0]
            else:
                if len(comb['available'])>0:
                    r=random.randint(0,len(comb['available'])-1)
                    python_comb=comb['available'][r]
                    for element in python_comb:
                        if element in igrovoe_pole['available']:
                            nomer=int(element)
                else:
                    #когда не осталось выйгрышных комбинаций
                    nomer=igrovoe_pole['available'][0]
                    
        
        igrovoe_pole_change (igrovoe_pole,nomer,hod, igrok, igrok_python)
        hod=1      
