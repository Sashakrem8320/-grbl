import cv2

# Загрузка изображения
image = cv2.imread('cam.png')

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
