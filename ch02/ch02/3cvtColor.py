import cv2
import sys

img_path = '../data/soccer.jpg'

# 이미지 파일 읽기
img=cv2.imread(img_path)
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

# 이미지 보여주기
cv2.imshow('Original Image', img)

# 1 그레이 이미지로 변환
#grayImg = cv2.imread(img_path,  cv2.IMREAD_GRAYSCALE)  # 1) 직접 그레이로 읽는 방법
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 2) 컬러 이미지를 그레이로 변환
cv2.imshow('GrayImage', grayImg) # 그레이 이미지 보여주기
 
# 2 컬러 모델 변환
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # BGR 이미지를 HSV 값으로 변환
ycrcbImg = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb) # BGR 이미지를 YCrCb 값으로 변환
rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR 이미지를 RGB로 변환

#print(img[0, 0]) # 원본 이미지의 첫 번째 픽셀(BGR 값) 출력
#print(rgbImg[0, 0]) # RGB로 변환된 이미지의 첫 번째 픽셀(RGB 값) 출력

#cv2.imshow('HSVImage', hsvImg)  # HSV 값을 가진 이미지를 BGR 창으로 보여주기
#cv2.imshow('YCrCbImage', ycrcbImg) # YCrCb 값을 가진 이미지를 BGR 창으로 보여주기
#cv2.imshow('RGBImage', rgbImg) # RGB 값을 가진 이미지를 BGR 창으로 보여주기

cv2.waitKey()
cv2.destroyAllWindows()