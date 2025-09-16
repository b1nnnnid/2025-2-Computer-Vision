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

#1 AND
src_and = cv2.bitwise_and(src, mask) # mask의 흰색(1)에 해당하는 roi는 그대로, 검정색(0)은 검정색으로
src_and_inv = cv2.bitwise_and(src, mask_inv) # mask의 흰색(1)에 해당하는 roi는 그대로, 검정색(0)은 검정색으로

pp1 = np.hstack((src_and,src_and_inv))
#cv2.imshow('point processing - logical AND/OR', pp1)

#2 OR
src_or = cv2.bitwise_or(src, mask) # mask의 검정색(0)에 해당하는 roi는 그대로, 흰색(1)은 흰색으로
src_or_inv = cv2.bitwise_or(src, mask_inv) # mask의 검정색(0)에 해당하는 roi는 그대로, 흰색(1)은 흰색으로

pp2 = np.hstack((src_or, src_or_inv))
#cv2.imshow('point processing - logical OR', pp2)

#3 NOT
src_not = cv2.bitwise_not(src) 
#cv2.imshow('point processing - logical NOT', src_not)

cv2.waitKey()
cv2.destroyAllWindows()