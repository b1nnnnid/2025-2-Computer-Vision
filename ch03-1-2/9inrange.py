import cv2

# 1. 손 이미지에서 피부색 영역 추출
src1 = cv2.imread('../data/hand.jpg')  # 손 이미지 읽기
hsv1 = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)  # BGR 이미지를 HSV로 변환
lowerb1 = (0, 30, 0)    # 피부색 HSV 하한값
upperb1 = (20, 180, 255)  # 피부색 HSV 상한값
dst1 = cv2.inRange(hsv1, lowerb1, upperb1)  # 피부색 범위에 해당하는 마스크 생성
cv2.imshow('hands', dst1)  # 마스크 이미지 표시

# 1-1. 마스크로 피부색 영역만 컬러로 추출
#dst_skin = cv2.bitwise_and(src1, src1, mask=dst1)
#cv2.imshow('hands - skin', dst_skin)

# 2. 꽃 이미지에서 특정 색상 영역 추출
src2 = cv2.imread('../data/flower.jpg')  # 꽃 이미지 읽기
hsv2 = cv2.cvtColor(src2,cv2.COLOR_BGR2HSV)  # BGR 이미지를 HSV로 변환
lowerb2 = (150, 100, 100)  # 꽃색 HSV 하한값
upperb2 = (180, 255, 255)  # 꽃색 HSV 상한값
dst2 = cv2.inRange(hsv2, lowerb2, upperb2)  # 꽃색 범위에 해당하는 마스크 생성
cv2.imshow('flower', dst2)  # 마스크 이미지 표시

# 2-1. 마스크로 꽃색 영역만 컬러로 추출
#dst_flower = cv2.bitwise_and(src2, src2, mask=dst2)
#cv2.imshow('flower - color', dst_flower)

cv2.waitKey()
cv2.destroyAllWindows()