import tkinter
import random
import pygame #для мелодии и анимации
import time #для анимации
#доп задание
#===============================================================
#звук
pygame.mixer.init()
pygame.mixer.music.load('melody.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
#===============================================================
def keygen(hex):
    if len(hex) != 5:
        print('Нужно ровно 5 знаков')
    for i in hex:
        if i not in '0123456789ABCDEFabcdef':
            print('Используйте только символы 16-ричной системы')
    dec = str(int(hex, 16))       
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    n1, n2, n3 = dec[0], dec[1], dec[2]
    n4, n5 = dec[-2], dec[-1] 
    n = 35 #длина (s - 1) так как начинается с нуля для номера расположения символа
    b = ''
    for d in [n1, n2, n3]:          
        pos = random.randint(0, 4)  
        for i in range(5):          
            if i == pos:
                b = b + d
            else:
                b = b + s[random.randint(0, n)]
        b = b + '-'                 
    return b[:-1] + ' ' + n4 + n5
#======================================================================================
#Окно
window = tkinter.Tk()
#название окна
window.title('Генератор ключа')
window.geometry('1024x768')
#это установит картинку на задний фон по ее размерам
background = tkinter.PhotoImage(file='pic3.png')
tkinter.Label(window, image=background).place(x=0, y=0)
#надпись что ввести вспомогалтельная
tkinter.Label(window, text='Введите hex-число с длиной 5 знаков:', font=('Verdana', 15)).place(x=40, y=620)
#поле для ввода
hexnum_get = tkinter.Entry(window, width=10, font=('Verdana', 15))
hexnum_get.place(x=40, y=655)
#создает надпись ключ, куде выведется готовый ключ
tkinter.Label(window, text='Ключ:', font=('Verdana', 15)).place(x=40, y=700)
key_enter = tkinter.Entry(window, width=30, font=('Verdana', 15))
key_enter.place(x=120, y=700)



star = tkinter.Label(window, text='*', font=('Verdana', 25), fg='red')
star.place(x=950, y=700)

def zvezd():
    for i in range(100):
        if i % 2 == 0:
            star['fg'] = 'red'
        else:
            star['fg'] = 'yellow'
        window.update()
        time.sleep(0.2)
#===================================================================================================
#функционал кнопки
def button1():
    key_enter.delete(0, 'end') #очищает сроку вывода ключа, чтобы не накапливались сгенерированные ключи
    key_enter.insert(0, keygen(hexnum_get.get()))
    zvezd()
#создает кнопку для геенрации
tkinter.Button(window, text='Сгенерировать', font=('Verdana', 15), command=button1).place(x=40, y=740)

window.mainloop()




