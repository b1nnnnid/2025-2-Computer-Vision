import cv2
import sys
import numpy as np  # numpy 모듈 import, 모든 numpy 함수를 np로 사용할 수 있음

# 이미지 파일 읽기
img = cv2.imread('../data/soccer.jpg')	
if img is None : 
    sys.exit('파일을 찾을 수 없습니다.')

print(type(img))  # 이미지 타입 출력 (numpy.ndarray)
print(img.shape)  # 이미지 크기 및 채널 정보 출력

# 1 numpy의 슬라이싱(slicing) 예시
# 이미지의 왼쪽 위 절반을 보여줌: 전체 높이 맨 위부터 반절까지, 전체 너비 시작부터 반절까지지
cv2.imshow('Upper left half', img[0:img.shape[0]//2, 0:img.shape[1]//2, : ])
#cv2.imshow('Upper left half', img[:img.shape[0]//2, :img.shape[1]//2, : ]) 윗줄과 같은 표현... 양 끝값(0과 같은)은 생략 가능>> :만 있으면 끝에서 끝까지
cv2.imshow('Lower right half', img[img.shape[0]//2 : img.shape[0], img.shape[1]//2 : img.shape[1], :])
#cv2.imshow('Lower right half', img[img.shape[0]//2 : , img.shape[1]//2 : , :])



# 이미지의 중앙 절반을 보여줌: 전체 높이의 1/4 ~ 4/3, 전체 너비의 1/4 ~ 3/4
cv2.imshow('Central half', img[img.shape[0]//4:3*img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4, : ])

# 각 색상 채널만 분리해서 보여주기 (OpenCV는 BGR 순서로 색상값 저장)
cv2.imshow('Red channel', img[ :, :, 2])     # R...앞에 콜론 2개>>전체 이미지 크기
cv2.imshow('Green channel', img[ :, :, 1])  # G
cv2.imshow('Blue channel', img[ :, :, 0])    # B

# 2 OpenCV의 split 함수로 컬러 채널 분리
b, g, r = cv2.split(img)
cv2.imshow('Red in Color(1B)', r)  # 빨간색 채널만 그레이(1Byte)으로 보여줌

black = np.zeros((img.shape[0],img.shape[1]), np.uint8) # img와 같은 크기의 배열을 만들어 0으로 초기화 => 검은색 이미지 생성
img_R = cv2.merge((black, black, r)) # (black, black, Red) = (0, 0, Red)로 빨간색만 컬러로 합침
cv2.imshow('Red in Color', img_R)

cv2.waitKey()
cv2.destroyAllWindows()