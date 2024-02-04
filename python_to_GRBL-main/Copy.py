import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# "Прогреваем" камеру, чтобы снимок не был тёмным

cap.read()

# Делаем снимок
ret, frame = cap.read()

# Записываем в файл
cv2.imwrite('cam.png', frame)

# Отключаем камеру
cap.release()

from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"cam.png")

# Setting the points for cropped image
left = 0
top = 0
right = 208
bottom = 235

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
im1.save('cam.png', quality=95)




my_photo = cv2.imread('cam.png')
#my_photo = cv2.imread('bricks\\White1.jpg')
img_grey = cv2.cvtColor(my_photo,cv2.COLOR_BGR2GRAY)

rows = img_grey.shape[0]
circles = cv2.HoughCircles(img_grey, cv2.HOUGH_GRADIENT, 1, rows / 8,
                          param1=40, param2=32,
                          minRadius=30, maxRadius=70)

res = np.zeros(my_photo.shape)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        print(center)
        # circle center
        cv2.circle(my_photo, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv2.circle(my_photo, center, radius, (255, 0, 255), 3)

cv2.imshow('origin', my_photo) #

cv2.waitKey()
cv2.destroyAllWindows()