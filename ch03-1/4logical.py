import cv2
import sys
import numpy as np

src = cv2.imread('../data/lenna256.png')

if src is None:
    sys.exit('파일을 찾을 수 없습니다.')

mask = cv2.imread('../data/opencv_logo256_mask.png', cv2.IMREAD_GRAYSCALE)
mask_inv = cv2.imread('../data/opencv_logo256_mask_inv.png', cv2.IMREAD_GRAYSCALE)

mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) # mask를 3채널로 변환
mask_inv = cv2.cvtColor(mask_inv, cv2.COLOR_GRAY2BGR) # mask_inv를 3채널로 변환
pp0 = np.hstack((mask,mask_inv))
#연산 가능한 로고 이미지 마스크...흑백사진처럼 보임
cv2.imshow('point processing - logical mask', pp0)

#1 AND...모두 1일 때만 1
src_and = cv2.bitwise_and(src, mask) # mask의 흰색(1)에 해당하는 roi는 그대로, 검정색(0)은 검정색으로
src_and_inv = cv2.bitwise_and(src, mask_inv) # mask의 흰색(1)에 해당하는 roi는 그대로, 검정색(0)은 검정색으로

pp1 = np.hstack((src_and,src_and_inv))
cv2.imshow('point processing - logical AND/OR', pp1)

#2 OR...하나라도 1이면 1
src_or = cv2.bitwise_or(src, mask) # mask의 검정색(0)에 해당하는 roi는 그대로, 흰색(1)은 흰색으로
src_or_inv = cv2.bitwise_or(src, mask_inv) # mask의 검정색(0)에 해당하는 roi는 그대로, 흰색(1)은 흰색으로

pp2 = np.hstack((src_or, src_or_inv))
cv2.imshow('point processing - logical OR', pp2)

#3 NOT...0은 1로, 1은 0으로(반전 이미지)
src_not = cv2.bitwise_not(src) 
cv2.imshow('point processing - logical NOT', src_not)

cv2.waitKey()
cv2.destroyAllWindows()