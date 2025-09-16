import cv2
import sys
import numpy as np

img1 = cv2.imread('../data/opencv_logo256.png')
if img1 is None:
    sys.exit('파일을 찾을 수 없습니다.')

img2 = cv2.imread('../data/lenna256.png')
if img2 is None:
    sys.exit('파일을 찾을 수 없습니다.')

#1 크기가 같은 두개의 이미지의 사칙 연산
img_plus3 = cv2.add(img1, img2)         # y = x1 + x2
img_minus3 = cv2.subtract(img1, img2)   # y = x1 - x2
img_multi3 = cv2.multiply(img1, img2)   # y = x1 * x2
img_div3 = cv2.divide(img1, img2)       # y = x1 / x2

pp1 = np.hstack((img_plus3, img_minus3, img_multi3, img_div3)) # hstack은 높이(세로)가 같아야 함
cv2.imshow('point processing - two images', pp1)

#2 이미지 블렌딩(Image Blending)
img_addW1 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0) # img1 * 0.5 + img2 * 0.5
img_addW2 = cv2.addWeighted(img1, 0.2, img2, 0.8, 0) # img1 * 0.2 + img2 * 0.8
img_addW3 = cv2.addWeighted(img1, 0.8, img2, 0.2, 0) # img1 * 0.8 + img2 * 0.2

pp2 = np.hstack((img_addW1, img_addW2, img_addW3)) # hstack은 높이(세로)가 같아야 함
cv2.imshow('addWeighted', pp2)

#3 조화로운 결합(SeamlessClone)
img_clone = cv2.seamlessClone(img1, img2, np.full(img2.shape[:2],255,np.uint8), (128,128), cv2.NORMAL_CLONE)
img_clone2 = cv2.seamlessClone(img1, img2, np.full(img2.shape[:2],255,np.uint8), (128,128), cv2.MIXED_CLONE)

pp3 = np.hstack((img_clone, img_clone2)) # hstack은 높이(세로)가 같아야 함
cv2.imshow('seamlessClone', pp3)

cv2.waitKey()
cv2.destroyAllWindows()