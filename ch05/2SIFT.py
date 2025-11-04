import cv2
import sys
import numpy as np

img = cv2.imread('../data/mot_color70.jpg') 
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

sift = cv2.SIFT_create()  # SIFT 특징 생성자
kp, des = sift.detectAndCompute(img, None)  # SIFT 특징점 검출과 특징 디스크립터 계산을 한 번에 수행
# 2mask : 특징점을 검출할 영역 지정 마스크
print(len(kp), des.shape)
print(des[0])   # 128차원의 벡터 : 16블록*8방향

dst = cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)   # 특징점을 그림
dst_rich = cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# flags : cv.DRAW_MATCHES_FLAGS_DEFAULT, cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG, cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS

img_sift = np.hstack((dst, dst_rich))
cv2.imshow('sift', img_sift)

cv2.waitKey()
cv2.destroyAllWindows()