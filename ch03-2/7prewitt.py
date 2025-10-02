# -1002

import cv2
import numpy as np

#gray = cv2.imread('../data/lenna256.png', cv2.IMREAD_GRAYSCALE)
#gray = cv2.imread('../data/coins.png', cv2.IMREAD_GRAYSCALE)
gray = cv2.imread('../data/check.png', cv2.IMREAD_GRAYSCALE)

blur = cv2.blur(gray, (3, 3))  # 에지 검출의 전처리과정 : 스무딩, 잡음 제거

# 1차 미분 : Prewitt(에지 검출 필터)
prewitt_filter_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])   # 수직 에지 필터...x가 수직임 주의!!
prewitt_filter_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])   # 수평 에지 필터

prewitt_grad_x = cv2.filter2D(blur, -1, prewitt_filter_x) # 수직 에지 필터 적용
prewitt_grad_y = cv2.filter2D(blur, -1, prewitt_filter_y) # 수평 에지 필터 적용

prewitt_x = cv2.convertScaleAbs(prewitt_grad_x)   # 절대값을 취해 양수 영상으로 변환, 수직 에지
prewitt_y = cv2.convertScaleAbs(prewitt_grad_y)   # 절대값을 취해 양수 영상으로 변환, 수평 에지

prewitt_edge = cv2.addWeighted(prewitt_x,0.5, prewitt_y,0.5,0)  # 에지 강도 계산, 수평 + 수직

prewitt = np.hstack((gray, prewitt_x, prewitt_y, prewitt_edge))
cv2.imshow('Prewitt', prewitt)

cv2.waitKey()
cv2.destroyAllWindows()