import cv2
import sys
import numpy as np

src1=cv2.imread('../data/lenna512.png')
src2=cv2.imread('../data/opencv_logo256.png')

if src1 is None or src2 is None:
    sys.exit('파일을 찾을 수 없습니다.')

mask = cv2.imread('../data/opencv_logo256_mask.png', cv2.IMREAD_GRAYSCALE) # 로고 마스크(흰색: 배경, 검정: 로고)
mask_inv = cv2.imread('../data/opencv_logo256_mask_inv.png', cv2.IMREAD_GRAYSCALE) # 로고 반전(배경) 마스크(흰색: 로고, 검정: 배경)

sy, sx = 0,0
rows, cols, channels = src2.shape # 로고 이미지 크기
roi = src1[sy:sy+rows, sx:sx+cols]	# 배경 이미지에서 로고 이미지가 들어간 영역 슬라이싱

# bitwise 함수의 첫번째와 두번째 배열이 같은 경우, 해당 배열에 mask를 적용하겠다는 의미
# roi AND roi = roi, 즉 roi에 mask를 적용하겠다는 의미
src1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv) # 마스크의 흰색 영역만 배경 유지, 나머지는 검정
src2_fg = cv2.bitwise_and(src2, src2, mask = mask) # 마스크의 흰색 영역만 로고 유지, 나머지는 검정

dst = cv2.bitwise_or(src1_bg, src2_fg) # 두 이미지 OR 결합

src1[sy:sy+rows, sx:sx+cols] = dst # 합성 결과 dst를 배경 이미지 src1에 삽입

pp = np.hstack((src1_bg, src2_fg, dst))
#cv2.imshow('point processing - logical', pp)
#cv2.imshow('combine', src1)

cv2.waitKey()
cv2.destroyAllWindows()