import cv2
import sys
import numpy as np

gray = cv2.imread('../data/lenna256.png', cv2.IMREAD_GRAYSCALE)
if gray is None :
    sys.exit('파일을 찾을 수 없습니다.')

#1 사칙연산...이미지는 2차원 배열(행렬)로 표현되어 직접 연산 가능능
img_plus = gray + 50       # y = x + 50
img_minus = gray - 50      # y = x - 50
img_multi = gray * 2       # y = 2 * x
img_div = gray / 2         # y = x / 2
img_reverse = 255 - gray   # y = 255 - x ... 이미지 반전(사진학적 역변환)


# hstack은 수평 방향(horizontal) 으로 배열을 이어 붙이는 함수... 생성한 5개의 이미지를 붙여 한 번에 보여줌
# hstack은 배열(이미지)의 높이(세로)가 같아야 함
pp1 = np.hstack((gray, img_plus, img_minus, img_multi, img_div, img_reverse)) 
cv2.imshow('point processing', pp1)
#단순 연산으로는 오류 이미지 출력...clamping 필요(음수값, 255 초과값 자르기)

#2 opencv 함수
img_plus2 = cv2.add(gray, 50)         # y = x + 50
img_minus2 = cv2.subtract(gray, 50)   # y = x - 50
img_multi2 = cv2.multiply(gray, 2)    # y = 2 * x
img_div2 = cv2.divide(gray, 2)        # y = x / 2
img_reverse2 = cv2.subtract(255,gray)    # y = 255 - x

pp2 = np.hstack((gray, img_plus2, img_minus2, img_multi2, img_div2, img_reverse2)) # hstack은 높이(세로)가 같아야 함
cv2.imshow('point processing - opencv', pp2)
#clamping 처리(포화연산)된 사진 출력

cv2.waitKey()
cv2.destroyAllWindows()