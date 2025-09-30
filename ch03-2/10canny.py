import cv2
import numpy as np

gray = cv2.imread('../data/lenna256.png', cv2.IMREAD_GRAYSCALE)

# Canny : 다양한 임계값 적용
# 같은 Tlow, 다른 Thigh
# 다른 Tlow, 같은 Thigh
canny1 = cv2.Canny(gray, 50, 200)  # Tlow=50, Thigh=200으로 설정
canny2 = cv2.Canny(gray, 100, 200)  # Tlow=100, Thigh=200으로 설정

canny = np.hstack((gray, canny1, canny2))
cv2.imshow('Canny', canny)

cv2.waitKey()
cv2.destroyAllWindows()