import cv2
import numpy as np

gray = cv2.imread('../data/lenna256.png', cv2.IMREAD_GRAYSCALE)
#gray = cv2.imread('../data/coins.png', cv2.IMREAD_GRAYSCALE)
#gray = cv2.imread('../data/check.png', cv2.IMREAD_GRAYSCALE)

blur = cv2.blur(gray, (3, 3))  # 에지 검출의 전처리과정 : 스무딩, 잡음 제거

# 1차 미분 : Sobel
# 1) 필터 정의 후 filter2D() 함수 이용
sobel_filter_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])  # 수직 에지 필터
sobel_filter_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  # 수평 에지 필터
sobel_grad_x = cv2.filter2D(blur, -1, sobel_filter_x)  # 수직 에지 필터 적용
sobel_grad_y = cv2.filter2D(blur, -1, sobel_filter_y)  # 수평 에지 필터 적용

# 2) cv2.Sobel() 함수 이용
#sobel_grad_x = cv2.Sobel(blur, cv2.CV_32F, 1, 0, ksize=3)  # 소벨 연산자 적용 # 수직 에지
#sobel_grad_y = cv2.Sobel(blur, cv2.CV_32F, 0, 1, ksize=3)  # 수평 에지

sobel_x = cv2.convertScaleAbs(sobel_grad_x)  # 절대값을 취해 양수 영상으로 변환, 수직 에지
sobel_y = cv2.convertScaleAbs(sobel_grad_y)  # 절대값을 취해 양수 영상으로 변환, 수평 에지

sobel_edge = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)  # 에지 강도 계산, 수평 + 수직

sobel = np.hstack((gray, sobel_x, sobel_y, sobel_edge))
cv2.imshow('Sobel',sobel)

cv2.waitKey()
cv2.destroyAllWindows()