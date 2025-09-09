import cv2     # opencv 모듈 import, 모든 opencv 함수를 cv2로 사용할 수 있음
import sys

img_path = 'soccer.jpg'  # 이미지 파일명

# 이미지 파일 읽기
img = cv2.imread(img_path) # 이미지 파일을 읽어 '이미지 데이터'를 img 배열 변수에 저장(default는 컬러(3Byte)로 표시(저장))
# img = cv2.imread(img_path, cv2.IMREAD_COLOR)
grayImg = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE) # 그레이스케일로 저장(1픽셀을 1Byte로 저장)

# 이미지가 정상적으로 읽혔는지 확인
if img is None : # 이미지 읽기에 실패하면 종료
    sys.exit('파일을 찾을 수 없습니다.')

#print(type(img))  # img 타입 출력 (numpy.ndarray)
#print(img.shape)  # img 크기 및 채널 정보 출력

#print(type(grayImg))   # grayImg 타입 출력 (numpy.ndarray)
#print(grayImg.shape)   # grayImg 크기 및 채널 정보 출력

#print(img[0,0])    # img[0,0] 픽셀의 컬러값(B,G,R) 출력

#print(grayImg[0,0])    # grayImg[0,0] 픽셀의 그레이값 출력

#print(img[0,0,0], img[0,0,1], img[0,0,2]) # img[0,0] 픽셀의 B, G, R 값 출력

# 이미지 읽기에 성공하면
cv2.imshow('Image Display', img)    # 이미지 사이즈에 맞는 창을 생성하여 이미지를 창에 출력
cv2.imshow('Gray Image Display', grayImg)

cv2.waitKey() # 키 입력 대기(창을 바로 종료하지 않기 위해)
cv2.destroyAllWindows() # 모든 창을 닫고 종료