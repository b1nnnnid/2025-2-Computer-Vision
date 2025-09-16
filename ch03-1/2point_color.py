import cv2
import sys
import numpy as np

img = cv2.imread('../data/lenna256.png')
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')
cv2.imshow('original image - color', img)

#1 컬러이미지 반전
img_reverse_color = cv2.subtract(255, img)
cv2.imshow("reverse_color", img_reverse_color)

#2 비선형 연산 : 감마연산
f = img / 255     # 감마 지수 계산을 위해 픽셀값을 0 ~ 1 사이 실수로 변환
img_gamma05 = np.uint8(255 * (f ** 0.5)) # 감마 연산 
cv2.putText(img_gamma05, "gamma=0.5", (20,30), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,0,255), 2)
img_gamma075 = np.uint8(255 * (f ** 0.75))
cv2.putText(img_gamma075, "gamma=0.75", (20,30), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,0,255), 2)
img_gamma10 = np.uint8(255 * (f ** 1.0))
cv2.putText(img_gamma10, "gamma=1.0", (20,30), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,0,255), 2)
img_gamma20 = np.uint8(255 * (f ** 2.0))
cv2.putText(img_gamma20, "gamma=2.0", (20,30), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,0,255), 2)
img_gamma30 = np.uint8(255 * (f ** 3.0))
cv2.putText(img_gamma30, "gamma=3.0", (20,30), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,0,255), 2)

pp = np.hstack((img_gamma05, img_gamma075, img_gamma10,img_gamma20,img_gamma30)) # hstack은 높이(세로)가 같아야 함
cv2.imshow('point processing - gamma', pp)

cv2.waitKey()
cv2.destroyAllWindows()