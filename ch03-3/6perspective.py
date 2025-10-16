# -1016

import cv2
import numpy as np

img = cv2.imread('../data/perspective3.jpg')

# 입력 이미지에서 변환할 4개의 점 좌표(좌상, 좌하, 우상, 우하)...어파인은 3개
pts1 = np.float32([(75, 11),  (74, 357), (420, 95), (450, 317)] )  # 입력 이미지의 위치
# 변환 후 출력 이미지에서의 4개 점 좌표
pts2 = np.float32([(0, 0),  (0, 383), (511, 0), (511, 383)])    # 출력 이미지의 위치

# 입력 이미지에 점 표시(시각화)
cv2.circle(img, (75,11), 8, (0,0,255), -1)      # 빨간색 점
cv2.circle(img, (74,357), 8, (255,0,0), -1)    # 파란색 점
cv2.circle(img, (420,95), 8, (255,0,255), -1)  # 보라색 점
cv2.circle(img, (450,317), 8, (0,255,0), -1)   # 초록색 점

# 원근 변환 행렬 계산
perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
# 원근 변환 적용
dst = cv2.warpPerspective(img, perspect_mat, (img.shape[1], img.shape[0]), cv2.INTER_CUBIC)

img_perspective=np.vstack((img, dst))
cv2.imshow('Perspective', img_perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()
