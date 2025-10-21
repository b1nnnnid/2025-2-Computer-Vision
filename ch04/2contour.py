# - 1021

import cv2
import sys

img = cv2.imread('../data/soccer.jpg')	 
img = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)
#img = cv2.imread('../data/shapes2.png')
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

img2 = img.copy()   # 결과 비교를 위한 이미지 복사본

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1) Canny 에지 검출과 findContours
canny = cv2.Canny(gray, 100, 200)    # 에지 이미지
cv2.imshow('Canny', canny)

#contours, hierarchy = cv2.findContours(canny, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)  # 내외 모든 윤곽선
contours, hierarchy = cv2.findContours(canny, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE) # 외곽 윤곽선만   # shapes2 비교

# 2) Otsu 이진화와 findContours
t, bin_gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)    # 이진 이미지
cv2.imshow('Otsu binarization', bin_gray)

#contours, hierarchy = cv2.findContours(bin_gray, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)  # 내외 모든 윤곽선

#print(contours)        # 윤곽선 좌표 정보 출력
#print(contour.shape)   # 윤곽선 좌표 개수(길이)
#print(hierarchy)        # 윤곽선 계층 구조 정보 출력

cv2.drawContours(img, contours, -1, (255, 255, 0), 2)  # 모든 contour(길이 100 이하 포함)
cv2.imshow('Contours - all', img)

lcontours=[]        # 긴 contour만 저장할 배열
for i in range(len(contours)) :     # 모든 contour에 대해
    #print(i, contours[i].shape)        # 각 contour의 좌표 개수(길이) 출력
    if contours[i].shape[0] > 100 :	    # 각 contour의 길이가 100보다 크면
        lcontours.append(contours[i])   # 길이가 100보다 큰 contour만 lcontours에 저장

cv2.drawContours(img2, lcontours, -1, (255, 0, 255), 2)   # 길이 100보다 큰 contour만 그리기
#cv2.imshow('Contours - long',img2)

cv2.waitKey()
cv2.destroyAllWindows()