# -1002

import cv2
import numpy as np

gray = cv2.imread('../data/lenna256.png', cv2.IMREAD_GRAYSCALE)

# Embossing

femboss1 = np.array([[-1.0, 0.0, 0.0],  # 엠보싱 필터
                  [ 0.0, 0.0, 0.0],
                  [ 0.0, 0.0, 1.0]])
femboss2 = np.array([[-1.0, -1.0, 0.0], # 엠보싱 필터
                 [ -1.0, 0.0, 1.0],
                  [ 0.0, 1.0, 1.0]])

# 부호 반전 가능
femboss1a = np.array([[1.0, 0.0, 0.0],  # 엠보싱 필터
                  [ 0.0, 0.0, 0.0],
                  [ 0.0, 0.0, -1.0]])
femboss2a = np.array([[1.0, 1.0, 0.0], # 엠보싱 필터
                 [ 1.0, 0.0, -1.0],
                  [ 0.0, -1.0, -1.0]])

emboss0 = cv2.filter2D(gray, -1, femboss1) #엠보싱 연산이긴 하나 음수값을 전부 0으로 만들어 엠포싱 효과 x

gray16 = np.int16(gray)              # int8로 음수는 -128~127 
    # => -255~255 범위를 위해 16비트(-32768~32767)로 변환
    # int16은 -256~255까지 표현 가능
    # 예, 127 = 01111111 (8비트) => 00000000 01111111 (16비트)
    # 예, -1  = 11111111 (8비트) => 11111111 11111111 (16비트)
f1 = cv2.filter2D(gray16,-1,femboss1)
f2 = f1 + 128               # 엠보싱 효과를 위해 128 더함
f3 = np.clip(f2, 0, 255)    # clamping : 0보다 작으면 0, 255보다 크면 255
emboss1 = np.uint8(f3)      # 이미지로 표현하기 위해 다시 uint8로 변환

emboss2 = np.uint8( np.clip( cv2.filter2D(gray16,-1,femboss2) + 128, 0, 255 ) )  # 위 과정을 한 줄로 표현
emboss1a = np.uint8( np.clip( cv2.filter2D(gray16,-1,femboss1a) + 128, 0, 255 ) )
emboss2a = np.uint8( np.clip( cv2.filter2D(gray16,-1,femboss2a) + 128, 0, 255 ) )

emboss = np.hstack((gray, emboss0, emboss1, emboss2, emboss1a, emboss2a))
cv2.imshow('Emboss',emboss)

cv2.waitKey()
cv2.destroyAllWindows()