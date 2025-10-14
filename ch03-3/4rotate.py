import cv2
import numpy as np

#img = cv2.imread('../data/lenna256.png')
img = cv2.imread('../data/rose_small.png')

(h, w) = img.shape[:2]      # 이미지의 크기
(cX, cY) = (w // 2, h // 2) # 이미지의 중심

# 1) 45도 회전 변환 행렬 계산
M45 = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)   # 이미지의 중심을 중심으로 이미지를 회전합시키는 행렬

rotated_45 = cv2.warpAffine(img, M45, (w, h))  # 회전 행렬을 이미지에 적용하여 이미지 회전시킴
cv2.imshow('Rotation - 45', rotated_45)

# 2-1) 90도 회전 변환 행렬 계산
M90 = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)   # 이미지의 중심을 중심으로 이미지를 회전합시키는 행렬

# 2-2) 3개의 좌표쌍으로 affine 행렬 계산
#src_points = np.float32([[0,0], [0,h-1], [w-1,0]])      # 입력 이미지의 위치
#dst_points = np.float32([[0,w-1], [h-1,w-1], [0,0]])    # 출력 이미지의 위치
#M90 = cv2.getAffineTransform(src_points, dst_points) # 3개의 좌표점 쌍으로 변환시키는 Affine 변환 행렬 계산

rotated_90 = cv2.warpAffine(img, M90, (w, h)) # affine 변환 행렬을 이미지에 적용하여 이미지 회전시킴, (h,w)
cv2.imshow('Rotation - 90', rotated_90)

cv2.waitKey()
cv2.destroyAllWindows()