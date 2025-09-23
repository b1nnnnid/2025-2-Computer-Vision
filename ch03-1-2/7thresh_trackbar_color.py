#-- 0923
import cv2
import sys
import numpy as np

def onChange(value):               # 트랙바 콜백 함수, value는 트랙바의 현재 위치(값)
    global img, bar_name, title   # 전역 변수 참조

    b_th = cv2.getTrackbarPos("Blue", title)    # Trackbar의 현재 위치 값 얻기 -> 임계값으로 사용
    g_th = cv2.getTrackbarPos("Green", title)
    r_th = cv2.getTrackbarPos("Red", title)
    
    ret, img_b = cv2.threshold(img[:,:,0], b_th, 255, cv2.THRESH_BINARY)   # 임계값으로 이진화...세로 전체, 가로 전체, 블루 채널
    ret, img_g = cv2.threshold(img[:,:,1], g_th, 255, cv2.THRESH_BINARY)
    ret, img_r = cv2.threshold(img[:,:,2], r_th, 255, cv2.THRESH_BINARY)
    
    
    img_thresh = cv2.merge((img_b, img_g, img_r))
    cv2.imshow(title, img_thresh) # 이진화된 이미지 표시

img = cv2.imread('../data/lenna512.png', cv2.IMREAD_COLOR) # BGR 컬러 영상을 컬러로 저장
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

title = 'Trackbar Event'    # 이미지 창 이름 : 트랙바가 추가될 창
cv2.imshow(title, img)     # 트랙바 생성 전에 이미지 창 생성

bar_name = "Blue"      # 트랙바 이름
cv2.createTrackbar("Blue", title, img[0][0][0], 255, onChange)   # 트랙바 생성 및 콜백 함수 등록
cv2.createTrackbar("Green", title, img[0][0][1], 255, onChange)
cv2.createTrackbar("Red", title, img[0][0][2], 255, onChange)

cv2.waitKey(0)
cv2.destroyAllWindows()
