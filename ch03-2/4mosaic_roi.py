# -0930

import cv2

img = cv2.imread('../data/bts.jpg')

x, y, w, h = cv2.selectROI(img) 	# 관심 영역(roi)을 선택
print("Selected ROI:", x, y, w, h)

roi = img[y:y+h, x:x+w]	# 선택한 영역만 잘라냄

# 선택한 영역만(roi) 스무딩을 이용한 모자익
ksize = 15  # 홀수만 가능...양측 균형 위해

#roi = cv2.GaussianBlur(roi, (ksize, ksize), 0.0) # 가우시안 블러링...평균 블러보다 선명

#roi = cv2.blur(roi, (ksize, ksize), 0.0) # 평균 블러링

roi = cv2.medianBlur(roi, ksize)   # 미디언(중간값) 필터...물감 그림처럼 뭉개짐

img[y:y+h, x:x+w] = roi  # 원본 이미지에 적용

cv2.imshow('Mosaic', img)

cv2.waitKey(0)
cv2.destroyAllWindows()