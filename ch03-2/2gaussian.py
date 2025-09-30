# -0930

import cv2
import numpy as np

gray = cv2.imread('../data/lenna256.png', cv2.IMREAD_GRAYSCALE)

#1 Gaussian
gaussian1 = cv2.GaussianBlur(gray, (5, 5), 1.0)

gaussian = np.hstack((gray, gaussian1))
cv2.imshow('Smooth - gaussian1', gaussian)

#2 Gaussian - 다양한 크기의 필터...평균값 필터보다 선명하게 블러링
gaussian2 = np.hstack(( gray, cv2.GaussianBlur(gray, (5, 5), 1.0), cv2.GaussianBlur(gray, (7, 7), 1.0), cv2.GaussianBlur(gray, (11, 11), 1.0), cv2.GaussianBlur(gray, (15, 15), 1.0) )) 
cv2.imshow('Smooth - Gaussian2', gaussian2)

#3 Gaussian - 다양한 sigma는 보통 0, 값이 클수록 블러링 효과 커짐
gaussian3 = np.hstack(( gray, cv2.GaussianBlur(gray,(5,5),1.0), cv2.GaussianBlur(gray,(5,5),3.0), cv2.GaussianBlur(gray,(5,5),7.0), cv2.GaussianBlur(gray,(5,5),11.0))) 
cv2.imshow('Smooth - Gaussian3', gaussian3)

cv2.waitKey()
cv2.destroyAllWindows()