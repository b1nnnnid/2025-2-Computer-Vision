# -1106

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

# 전수조사 방법(Brute-Force 매칭, BF 매칭)
bf_matcher = cv2.BFMatcher()

# 1) 최근접 특징점
bf_matches = bf_matcher.match(des1, des2)   # 가장 유사한 특징점 1개를 받음
print('전체 매칭 개수:', len(bf_matches))
print(bf_matches[0].queryIdx, ' -- ', bf_matches[0].trainIdx, ' : ', bf_matches[0].distance)  # DMatch 객체 정보 출력

# 매칭 전략을 만족하는 매칭쌍(good_match)을 찾음
T = 200
good_match = []
for nearest in bf_matches :
    if nearest.distance < T :  # 고정 임계값, 최근접 이웃 거리 비율 전략
        good_match.append(nearest)
print('good_match 개수:', len(good_match))

img_match = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1] + img2.shape[1], 3), dtype=np.uint8)
cv2.drawMatches(img1, kp1, img2, kp2, good_match, img_match, flags=cv2.DrawMatchesFlags_DEFAULT)  # good_match만 그림
# cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS, cv2.DrawMatchesFlags_DEFAULT, cv2.DrawMatchesFlags_DRAW_OVER_OUTIMG, cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS, cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS
cv2.imshow('Good Matches', img_match)

# 2) k개의 유사한 특징점
bf_knn_matches = bf_matcher.knnMatch(des1, des2, 2)     # 가장 유사한 특징점 k(=2)개를 받음
print('전체 매칭 개수:', len(bf_knn_matches))
print(bf_knn_matches[0][0].queryIdx, ' -- ', bf_knn_matches[0][0].trainIdx, ' : ', bf_knn_matches[0][0].distance)  # DMatch 객체 정보 출력

# 최근접 2개의 이웃 거리 비율이 임계값보다 작으면 매칭으로 간주
T2 = 0.7
good_match2 = []     # 매칭 전략을 만족하는 매칭쌍(good_match)을 찾음
for nearest1, nearest2 in bf_knn_matches :
    if (nearest1.distance / nearest2.distance) < T2 :  # 최근접 이웃 거리 비율 전략
        good_match2.append(nearest1)
print('good_match 개수:', len(good_match2))

img_match2 = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1] + img2.shape[1], 3), dtype=np.uint8)
cv2.drawMatches(img1, kp1, img2, kp2, good_match2, img_match2, flags=cv2.DrawMatchesFlags_DEFAULT)  # good_match만 그림
# cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS, cv2.DrawMatchesFlags_DEFAULT, cv2.DrawMatchesFlags_DRAW_OVER_OUTIMG, cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS, cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS
cv2.imshow('Good Matches - kNN', img_match2)

cv2.waitKey()
cv2.destroyAllWindows()