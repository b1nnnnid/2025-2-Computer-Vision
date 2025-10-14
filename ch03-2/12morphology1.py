# -1014

import cv2
import numpy as np

gray = cv2.imread('../data/morph_j.png', cv2.IMREAD_GRAYSCALE)

# 이진화 이미지로 배경과 객체 구분 : 오츠 알고리즘으로 자동 임계값 계산 및 이진화
t, b = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(t)

# 구조 요소(Structuring Element)
# 1) 직접 정의
se1 = np.uint8([[0,0,1,0,0],			# 타원형 구조 요소
            [0,1,1,1,0],
            [1,1,1,1,1],
            [0,1,1,1,0],
            [0,0,1,0,0]])

# 2) OpenCV 함수 이용
# 다양한 구조 요소 적용: shape 인자 바꿔보기
se2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
#se3 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
#se4 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))

k=1     # 반복 횟수

b_dilation = cv2.dilate(b, se2, iterations=k)	# 팽창: 객체 팽창, 배경 축소, 검정 잡음 제거

b_erosion = cv2.erode(b, se2, iterations=k)	# 침식: 객체 축소, 배경 팽창, 흰 잡음 제거


# 직접 중첩해도 ok, morphologyEX함수에 shape 바꿔줘도 ok
b_opening = cv2.dilate(cv2.erode(b, se2, iterations=k), se2, iterations=k)	# 열기: 침식>>팽창
# b_opening = cv2.morphologyEx(b, cv2.MORPH_OPEN, se2)

b_closing = cv2.erode(cv2.dilate(b, se2, iterations=k), se2, iterations=k)	# 닫기: 팽창>>침식
# b_closing = cv2.morphologyEx(b, cv2.MORPH_CLOSE, se2)

morphology = np.vstack((b, b_dilation,b_erosion,b_opening,b_closing))
cv2.imshow('Morphology',morphology)

cv2.waitKey()
cv2.destroyAllWindows()