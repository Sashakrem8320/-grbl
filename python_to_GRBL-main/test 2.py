import time

maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран
#!/usr/bin/env python
import datetime
import serial
import mouse

# Open grbl serial port
s = serial.Serial('COM10', 115200) # put your serial port here
print('Connected to: ' + s.name)
print('Serial port open: ' + str(s.is_open))

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import screen_brightness_control as sbc
import pyttsx3

text = 'какой-нибудь текст'
tts = pyttsx3.init()
rate = tts.getProperty('rate') #Скорость произношения
tts.setProperty('rate', rate-40)

volume = tts.getProperty('volume') #Громкость голоса
tts.setProperty('volume', volume+0.9)

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru')

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)

tts.say(text)
tts.runAndWait()

















def checkr():
    global was_hod
    reset()
    send_gcode("G1  X91 Y120.0901")
    time.sleep(8)
    hot = 0
    while hot ==0:
        import cv2
        import numpy as np

        cap = cv2.VideoCapture(0)

        # "Прогреваем" камеру, чтобы снимок не был тёмным

        cap.read()

        # Делаем снимок
        ret, frame = cap.read()

        # Записываем в файл
        cv2.imwrite('cam.png', frame)

        cap.release()

        # Загрузка изображения
        image = cv2.imread('cam.png')
        cv2.imshow('origin', image)  #

        cv2.waitKey()

        cv2.destroyAllWindows()

        # Координаты точек для обрезки (левый верхний угол и правый нижний угол)
        x1, y1, x2, y2 = 0, 0, 211, 243

        # Обрезка изображения
        cropped_image = image[y1:y2, x1:x2]

        # Сохранение обрезанного изображения
        cv2.imwrite('1.jpg', cropped_image)

        x1, y1, x2, y2 = 131, 61, 371, 232
        # Обрезка изображения
        cropped_image = image[y1:y2, x1:x2]

        # Сохранение обрезанного изображения
        cv2.imwrite('2.jpg', cropped_image)

        x1, y1, x2, y2 = 286, 43, 475, 223
        # Обрезка изображения
        cropped_image = image[y1:y2, x1:x2]

        # Сохранение обрезанного изображения
        cv2.imwrite('3.jpg', cropped_image)

        # Координаты точек для обрезки (левый верхний угол и правый нижний угол)
        x1, y1, x2, y2 = 0, 206, 207, 419
        # Обрезка изображения
        cropped_image = image[y1:y2, x1:x2]

        # Сохранение обрезанного изображения
        cv2.imwrite('4.jpg', cropped_image)

        x1, y1, x2, y2 = 147, 216, 335, 429
        # Обрезка изображения
        cropped_image = image[y1:y2, x1:x2]

        # Сохранение обрезанного изображения
        cv2.imwrite('5.jpg', cropped_image)

        x1, y1, x2, y2 = 315, 217, 477, 426
        # Обрезка изображения
        cropped_image = image[y1:y2, x1:x2]
        cv2
        # Сохранение обрезанного изображения
        cv2.imwrite('6.jpg', cropped_image)

        x1, y1, x2, y2 = 0, 391, 161, 631
        # Обрезка изображения
        cropped_image = image[y1:y2, x1:x2]

        # Сохранение обрезанного изображения
        cv2.imwrite('7.jpg', cropped_image)

        x1, y1, x2, y2 = 163, 409, 359, 633
        # Обрезка изображения
        cropped_image = image[y1:y2, x1:x2]

        # Сохранение обрезанного изображения
        cv2.imwrite('8.jpg', cropped_image)

        x1, y1, x2, y2 = 308, 395, 475, 637
        # Обрезка изображения
        cropped_image = image[y1:y2, x1:x2]

        # Сохранение обрезанного изображения
        cv2.imwrite('9.jpg', cropped_image)

        # Загрузка изображения

        for f in range(9):

            my_photo = cv2.imread(str(f + 1) + '.jpg')
        # my_photo = cv2.imread('cam.png')
        # my_photo = cv2.imread('bricks\\White1.jpg')
            img_grey = cv2.cvtColor(my_photo, cv2.COLOR_BGR2GRAY)

            rows = img_grey.shape[0]
            circles = cv2.HoughCircles(img_grey, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                       param1=40, param2=32,
                                       minRadius=30, maxRadius=70)


            res = np.zeros(my_photo.shape)

            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    center = (i[0], i[1])
                    centerr = i[0]

                    # circle center
                    cv2.circle(my_photo, center, 1, (0, 100, 100), 3)
                    # circle outline
                    radius = i[2]
                    cv2.circle(my_photo, center, radius, (255, 0, 255), 3)
                    if len(str(centerr))>0:
                        if f+1 not in was_hod:
                            hot = int(f+1)
                            was_hod.append(f + 1)
                            print(123456789)
                            continue

            #cv2.imshow('origin', my_photo)  #

            #cv2.waitKey()

            #cv2.destroyAllWindows()
    print(hot, "хот")
    return hot




def reset():
    send_gcode('$X')
    send_gcode('M3S90')
    send_gcode('$H')
    send_gcode('F2000')
    send_gcode('G92X0Y0')
    print("Готов к работе")
# Serial write and readline0
def send_gcode(gcode):
    s.write(str.encode(gcode+"\n"))
    print(s.readline().strip().decode('utf-8'))
    print('Sending: ' + str(str.encode(gcode)))


# Wake up grbl


def start_robot():
    tts.say("Настройка")
    tts.runAndWait()
    reset()
    with open('Поле22_0019.gcode', 'r') as f:
        start = f.read()
    start = start.split("\n")
    for i in range(len(start)):
        send_gcode(start[i])


    #send_gcode('G1 X100 Y100 F10000') # Go to X:100, Y:100, Z:0.0 at 5000 mm/min
    #send_gcode('G1 X0 Y0')

    # Close serial port


def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


# Сделать ход в ячейку
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


# Искусственный интеллект: поиск линии с нужным количеством X и O на победных линиях
def check_line(sum_O, sum_X):
    step = ""
    for line in victories:
        o = 0
        x = 0

        for j in range(0, 3):
            if maps[line[j]] == "O":
                o = o + 1
            if maps[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]




    return step


# Искусственный интеллект: выбор хода
def AI():
    step = ""

    # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
    step = check_line(2, 0)

    # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
    if step == "":
        step = check_line(0, 2)

        # 3) если 1 фигура своя и 0 чужих - ставим
    if step == "":
        step = check_line(1, 0)

        # 4) центр пуст, то занимаем центр
    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5

            # 5) если центр занят, то занимаем первую ячейку
    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1
    if step == 1:
        with open('кр1.gcode', 'r') as f:
            start = f.read()
        start = start.split("\n")
        for i in range(len(start)):
            send_gcode(start[i])
    elif step == 2:
        with open('кр2.gcode', 'r') as f:
            start = f.read()
        start = start.split("\n")
        for i in range(len(start)):
            send_gcode(start[i])
    elif step == 3:
        with open('кр3.gcode', 'r') as f:
            start = f.read()
        start = start.split("\n")
        for i in range(len(start)):
            send_gcode(start[i])
    elif step == 4:
        with open('кр4.gcode', 'r') as f:
            start = f.read()
        start = start.split("\n")
        for i in range(len(start)):
            send_gcode(start[i])
    elif step == 5:
        with open('кр5.gcode', 'r') as f:
            start = f.read()
        start = start.split("\n")
        for i in range(len(start)):
            send_gcode(start[i])
    elif step == 6:
        with open('кр6.gcode', 'r') as f:
            start = f.read()
        start = start.split("\n")
        for i in range(len(start)):
            send_gcode(start[i])
    elif step == 7:
        with open('кр7.gcode', 'r') as f:
            start = f.read()
        start = start.split("\n")
        for i in range(len(start)):
            send_gcode(start[i])
    elif step == 8:
        with open('кр8.gcode', 'r') as f:
            start = f.read()
        start = start.split("\n")
        for i in range(len(start)):
            send_gcode(start[i])
    elif step == 9:
        with open('кр9.gcode', 'r') as f:
            start = f.read()
        start = start.split("\n")
        for i in range(len(start)):
            send_gcode(start[i])

    print(step, "step")
    was_hod.append(step)
    return step

was_hod = []
# Основная программа
game_over = False
human = True
start_robot()
tts.say("Нарисуйте кружок")
tts.runAndWait()
time.sleep(10)

while game_over == False:

    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if human == True:
        symbol = "X"
        step = checkr()
    else:
        print("Компьютер делает ход: ")
        tts.say("Я хожу")
        tts.runAndWait()
        symbol = "O"
        step = AI()
        time.sleep(15)
        tts.say("Нарисуйте кружок")
        tts.runAndWait()


    # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
    if step != "":
        step_maps(step, symbol)  # делаем ход в указанную ячейку
        win = get_result()  # определим победителя
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        print("Ничья!")
        game_over = True
        win = "дружба"

    human = not (human)

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
tts.say("Победил"+ str(win))
tts.runAndWait()
print("Победил", win)