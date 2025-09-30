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
edge2 = cv2.filter2D(gray, -1, fedge2)

# 2) cv2.Laplacian() 함수 이용
laplacian = cv2.Laplacian(gray, -1)

grad = np.hstack((gray, edge2, laplacian))
cv2.imshow('Second derivatives', grad)

cv2.waitKey()
cv2.destroyAllWindows()