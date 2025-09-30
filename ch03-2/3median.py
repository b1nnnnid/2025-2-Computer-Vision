# -0930

import cv2
import numpy as np

#gray = cv2.imread('../data/lenna256.png', cv2.IMREAD_GRAYSCALE)
gray = cv2.imread('../data/morph.jpg', cv2.IMREAD_GRAYSCALE)
#median 필터는 소금후추 노이즈 제거에 효과적...morph 이미지로 확인

median1 = cv2.medianBlur(gray, 5)

#1 평균/가우시안 필터와 비교
median = np.hstack((gray, median1, cv2.blur(gray, (5, 5)), cv2.GaussianBlur(gray, (5, 5), 1.0)))
cv2.imshow('Average - blur', median)

#2 다양한 크기의 필터
median1 = np.hstack((gray, cv2.medianBlur(gray, 3), cv2.medianBlur(gray, 7), cv2.medianBlur(gray, 11)))
cv2.imshow('Smooth - Median1', median1)



cv2.waitKey()
cv2.destroyAllWindows()