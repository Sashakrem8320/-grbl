import cv2

# Load image, grayscale, Gaussian blur, adaptive threshold
cap = cv2.VideoCapture(0)

# "Прогреваем" камеру, чтобы снимок не был тёмным

cap.read()

# Делаем снимок
ret, frame = cap.read()

# Записываем в файл
cv2.imwrite('cam.png', frame)

# Отключаем камеру

image = cv2.imread('cam.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9,9), 0)
thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,15,30)

# Dilate to combine adjacent text contours
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
dilate = cv2.dilate(thresh, kernel, iterations=7)

# Find contours, highlight text areas, and extract ROIs
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

ROI_number = 0
for c in cnts:
    area = cv2.contourArea(c)
    if area > 10000:
        x,y,w,h = cv2.boundingRect(c)
        print(x,y)
        #if x>900 and y>400 and y<700:
        cropped_img = image[y:y + h, x:x + w]
        cv2.rectangle(image, (x, y), (x + w, y + h), (36, 205, 12), 3)
        # ROI = image[y:y+h, x:x+w]
        # cv2.imwrite('ROI_{}.png'.format(ROI_number), ROI)
        # ROI_number += 1
        img_name = "ui" + ".jpg"
        cv2.imwrite(img_name, cropped_img)
#cv2.imshow('thresh', thresh)
#cv2.imshow('dilate', dilate)
cv2.imshow('image', image)
cv2.waitKey()