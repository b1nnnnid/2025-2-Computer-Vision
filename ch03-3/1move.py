# -1016

import cv2
import numpy as np

def contain(p, shape) :       # 좌표(y,x)가 범위내 인지 검사
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

img = cv2.imread('../data/flower.jpg')

# 1) 직접 반복문을 이용하여 구현
dst = np.zeros(img.shape, img.dtype)  # 입력 이미지(img)와 같은 크기의 출력 이미지(0 : 검정)
pt = (100, 50)   # 입력 이미지를 pt만큼 이동
for i in range(dst.shape[0]) :  # 출력 이미지의 각 픽셀 (i, j)에 대해 – 역방향 사상
    for j in range(dst.shape[1]) :
        y, x = np.subtract((i, j), pt)  # 1) 입력 픽셀 위치 (y, x) 계산 : (i,j)에서 –pt 만큼 이동한 위치 결정
        if contain((y, x), img.shape):  # (y,x)가 img.shape에 포함되면
            dst[i, j] = img[y, x]       # 2) 출력 이미지 (i,j)의 픽셀값 결정 : 입력이미지 (y,x) 픽셀값 저장

# 2) affine 변환 행렬로 계산
# warpAffine() 내부에서는 이 𝑀의 역행렬 𝑀^(−1)을 사용해서 역변환 매핑을 자동으로 처리하므로 전변환 행렬을 주어야 함...역변환 x
M = np.float32([
    [1, 0, pt[1]],
    [0, 1, pt[0]]
])
dst2 = cv2.warpAffine(img, M, (img.shape[1], img.shape[0])) # affine 변환 행렬 계산

move = np.hstack((img, dst, dst2))
cv2.imshow('Move', move)

cv2.waitKey()
cv2.destroyAllWindows()