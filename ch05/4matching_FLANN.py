import cv2
import numpy as np
import time

img1 = cv2.imread('../data/mot_color70.jpg')[190:350, 440:560]  # 버스를 크롭한 이미지 : 검색 이미지로 사용
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('../data/mot_color83.jpg')  # 장면 이미지
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)
print('특징점 개수:', len(kp1), len(kp2))

# FLANN(Fast Library for Approximate Nearest Neighbors)는 특징점 주위의 이웃에 있는 특징기술자에 대해서만 거리를 계산
flann_matcher = cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_FLANNBASED)
flann_knn_matches = flann_matcher.knnMatch(des1, des2, 2)   # 가장 유사한 특징점 k(=2)개를 받음
print('전체 매칭 개수:', len(flann_knn_matches))
print(flann_knn_matches[0][0].queryIdx, ' -- ', flann_knn_matches[0][0].trainIdx, ' : ', flann_knn_matches[0][0].distance)  # DMatch 객체 정보 출력

# 매칭 전략을 만족하는 매칭쌍(good_match)을 찾음
T = 0.7
good_match = []
for nearest1, nearest2 in flann_knn_matches:
    if (nearest1.distance / nearest2.distance) < T:  # 최근접 이웃 거리 비율 전략
        good_match.append(nearest1)
print('good_match 개수:', len(good_match))

img_match = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1] + img2.shape[1], 3), dtype=np.uint8)
cv2.drawMatches(img1, kp1, img2, kp2, good_match, img_match, flags=cv2.DrawMatchesFlags_DEFAULT)  # good_match만 그림
cv2.imshow('Good Matches - FLANN', img_match)

cv2.waitKey()
cv2.destroyAllWindows()