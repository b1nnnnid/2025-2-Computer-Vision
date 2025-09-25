#-- 0923-0925

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
plt.plot(h_gray, 'b', marker='o', linewidth=1, linestyle='solid')   # linestyle='solid'

print(type(h_gray))
print(h_gray)   # 히스토그램 출력

# 히스토그램 계산 및 표시
h_gray2 = cv2.calcHist([gray2], [0], None, [256], [0, 256]) # 1바이트 gray의 0번 채널에서 히스토그램 구함
#plt.plot(h_gray2, 'm', linestyle='dashed', linewidth=3)
# x : 0, 1, 2, ..., 254, 255     >>>plot과 달리 bar()는 x값 필수
x = np.arange(256) # 0 ~ 255의 배열 생성 [ 0, 1, ..., 255 ] 
print(h_gray2.flatten())
plt.bar(x, h_gray2.flatten(), color='orange', width=2)

plt.show() # plot 창 출력 후 바로 다음으로 넘어가지 않고 잠시 중단...창을 닫으면 넘어감
# cv2.waitkey()...matplotlib의 show를 사용할 땐 굳이 불필요
cv2.destroyAllWindows()