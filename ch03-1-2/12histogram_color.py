import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/soccer.jpg')
#img = cv2.imread('../data/lenna256.png')
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv2.imshow('Color image', img)

# BGR 각 채널의 히스토그램 계산 및 표시
h_r = cv2.calcHist([img], [2], None, [256], [0, 256]) # 2번 채널인 R 채널에서 히스토그램 구함
plt.plot(h_r, color='r', linewidth=1)             # linestyle='solid'

h_g = cv2.calcHist([img], [1], None, [256], [0, 256]) # 1번 채널인 G 채널에서 히스토그램 구함
plt.plot(h_g, color='g', linestyle='dotted', linewidth=2)

h_b = cv2.calcHist([img], [0], None, [256], [0, 256]) # 0번 채널인 B 채널에서 히스토그램 구함
plt.plot(h_b, color='b', marker='.', linewidth=3)   # marker='o'

plt.show() # plot 창 출력

cv2.destroyAllWindows()