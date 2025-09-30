# -0930

import cv2
import numpy as np

gray = cv2.imread('../data/lenna256.png', cv2.IMREAD_GRAYSCALE)

# 1 평균 블러(스무딩) 필터 적용
# 1-1 filter2D() 함수로 스무딩 필터 적용
faverage = np.array([[1.0/9.0, 1.0/9.0, 1.0/9.0],       # numpy 배열로 3*3 스무딩 필터 생성
                     [1.0/9.0, 1.0/9.0, 1.0/9.0],
                     [1.0/9.0, 1.0/9.0, 1.0/9.0]])
average1 = cv2.filter2D(gray, -1, faverage)         # 필터 적용(convolution 계산)

# 1-2 cv2.blur() 함수로 스무딩 필터 적용
average2 = cv2.blur(gray, (3, 3)) # cv2.blur() 함수로 스무딩 필터 적용

average = np.hstack(( gray, average1, average2 ))
cv2.imshow('Average - blur', average)

#2 다양한 크기의 스무딩 필터... 크기가 클수록 블러 효과 강해짐
smooth = np.hstack(( gray, cv2.blur(gray,(3,3),0.0), cv2.blur(gray,(7,7),0.0), cv2.blur(gray,(11,11),0.0), cv2.blur(gray,(15,15),0.0) ))
cv2.imshow('Smooth', smooth)

cv2.waitKey()
cv2.destroyAllWindows()