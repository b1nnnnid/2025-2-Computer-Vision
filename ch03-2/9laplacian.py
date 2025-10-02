# -1002

import cv2
import numpy as np

gray = cv2.imread('../data/lenna256.png', cv2.IMREAD_GRAYSCALE)
#gray = cv2.imread('../data/coins.png', cv2.IMREAD_GRAYSCALE)
#gray = cv2.imread('../data/check.png', cv2.IMREAD_GRAYSCALE)

# 2차 미분 
# 1) 필터 정의 후 filter2D() 함수 이용
fedge2 =np.array([[0.0, 1.0, 0.0],
                  [1.0, -4.0, 1.0],
                  [ 0.0, 1.0, 0.0]])
fedge2a =np.array([[0.0, -1.0, 0.0],
                  [-1.0, 4.0, -1.0],
                  [ 0.0, -1.0, 0.0]])
fedge2b =np.array([[1.0, 1.0, 1.0],
                  [1.0, -8.0, 1.0],
                  [ 1.0, 1.0, 1.0]])
fedge2c =np.array([[-1.0, -1.0, -1.0],
                  [-1.0, 8.0, -1.0],
                  [ -1.0, -1.0, -1.0]])

edge2 = cv2.filter2D(gray, -1, fedge2)
edge2a = cv2.filter2D(gray, -1, fedge2a)
edge2b = cv2.filter2D(gray, -1, fedge2b)
edge2c = cv2.filter2D(gray, -1, fedge2c)

# 2) cv2.Laplacian() 함수 이용
laplacian = cv2.Laplacian(gray, -1) #1바이트로 저장하되 음수 등 범위 초과 시 클램핑

laplacian2 = cv2.Laplacian(gray, cv2.CV_32F) #4바이트 배열에 저장
laplacian2 = cv2.convertScaleAbs(laplacian2)

grad = np.hstack((gray, edge2, edge2a, edge2b, edge2c,laplacian, laplacian2))
cv2.imshow('Second derivatives', grad)

cv2.waitKey()
cv2.destroyAllWindows()