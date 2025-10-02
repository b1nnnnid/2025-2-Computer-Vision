# -0930~1002

import cv2
import numpy as np

gray = cv2.imread('../data/lenna256.png', cv2.IMREAD_GRAYSCALE)

# Sharpening... 블러링과 반대, 경계를 더 뚜렷하게, 픽셀값이 음수를 가질 수 있음
fsharpen1 = np.array([[0.0, -1.0, 0.0],     # 샤프닝 필터(중앙값 5)
                  [-1.0, 5.0, -1.0],
                  [ 0.0, -1.0, 0.0]])
sharpen1 = cv2.filter2D(gray, -1, fsharpen1)    # 샤프닝 필터 적용
cv2.putText(sharpen1, 'sharpen 5', (10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,100,100), 2)

#sharpen1 과 동일한 이미지 출력
sharpen1a = cv2.filter2D(gray, cv2.CV_32F, fsharpen1)
sharpen1a = np.clip(sharpen1a, 0, 255) #직접 클램핑 처리 가능(최대 최솟값 범위 내로 자르기)
sharpen1a = np.uint8(sharpen1a)


fsharpen2 = np.array([[-1.0, -1.0, -1.0],   # 샤프닝 필터(중앙값 9)
                  [-1.0, 9.0, -1.0],
                  [-1.0, -1.0, -1.0]])
sharpen2 = cv2.filter2D(gray, -1, fsharpen2)    # 샤프닝 필터 적용
cv2.putText(sharpen2, 'sharpen 9', (10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,100,100), 2)

sharpen = np.hstack((gray, sharpen1, sharpen2))
cv2.imshow('Sharpening', sharpen)

cv2.waitKey()
cv2.destroyAllWindows()