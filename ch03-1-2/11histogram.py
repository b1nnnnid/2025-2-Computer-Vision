#-- 0923

import cv2
import numpy as np
import matplotlib.pyplot as plt # matplotlib 설치
#matplotlib : 파이썬에서 데이타를 차트나 플롯(Plot)으로 그려주는 라이브러리 패키지로서 가장 많이 사용되는 데이타 시각화(Data Visualization) 패키지

# 이미지 밝기/채도 분포 그래프 그리기
gray = cv2.imread("../data/CT-brain-image.jpg", cv2.IMREAD_GRAYSCALE)
gray2 = cv2.subtract(255,gray)  # 반전 이미지

img_gray=np.hstack((gray, gray2))
cv2.imshow('Gray image',img_gray)

# 히스토그램 계산 및 표시
h_gray = cv2.calcHist([gray], [0], None, [256], [0, 256]) # 1바이트 gray의 0번 채널에서 히스토그램 구함
plt.plot(h_gray, 'b', linewidth=3)   # linestyle='solid'

print(type(h_gray))
print(h_gray)   # 히스토그램 출력

# 히스토그램 계산 및 표시
h_gray2 = cv2.calcHist([gray2], [0], None, [256], [0, 256]) # 1바이트 gray의 0번 채널에서 히스토그램 구함
plt.plot(h_gray2, 'm', linestyle='dashed', linewidth=3)

plt.show() # plot 창 출력
plt.waitkey()
cv2.destroyAllWindows()