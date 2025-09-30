import cv2
import numpy as np

gray = cv2.imread('../data/morph_j.png', cv2.IMREAD_GRAYSCALE)

# 이진화 이미지로 배경과 객체 구분 : 오츠 알고리즘으로 자동 임계값 계산 및 이진화
t, b = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(t)

# 구조 요소
se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

k=1     # 반복 횟수

b_dilation1 = cv2.dilate(b, se, iterations=k)	# 팽창 1번
b_dilation2 = cv2.dilate(b, se, iterations=k+1)	# 팽창 2번
b_dilation3 = cv2.dilate(b, se, iterations=k+2)	# 팽창 3번
b_dilation = np.hstack((b, b_dilation1, b_dilation2, b_dilation3))

b_erosion1 = cv2.erode(b, se, iterations=k)	# 침식 1번
b_erosion2 = cv2.erode(b, se, iterations=k+1)	# 침식 2번
b_erosion3 = cv2.erode(b, se, iterations=k+2)	# 침식 3번
b_erosion = np.hstack((b, b_erosion1, b_erosion2, b_erosion3))

b_opening1 = cv2.dilate(cv2.erode(b, se, iterations=k), se, iterations=k)	# 열기 1번
b_opening2 = cv2.dilate(cv2.erode(b, se, iterations=k+1), se, iterations=k+1)	# 열기 2번
b_opening3 = cv2.dilate(cv2.erode(b, se, iterations=k+2), se, iterations=k+2)	# 열기 3번
b_opening = np.hstack((b, b_opening1, b_opening2, b_opening3))

b_closing1 = cv2.erode(cv2.dilate(b, se, iterations=k), se, iterations=k)	# 닫기 1번
b_closing2 = cv2.erode(cv2.dilate(b, se, iterations=k+1), se, iterations=k+1)	# 닫기 2번
b_closing3 = cv2.erode(cv2.dilate(b, se, iterations=k+2), se, iterations=k+2)	# 닫기 3번
b_closing = np.hstack((b, b_closing1, b_closing2, b_closing3))

morphology = np.vstack((b_dilation, b_erosion, b_opening, b_closing))
cv2.imshow('Different Structuring element', morphology)

cv2.waitKey()
cv2.destroyAllWindows()