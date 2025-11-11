import cv2
import sys
import numpy as np


# 이미지 경로 설정
img = cv2.imread('../data/3.png') 
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

# 이미지 크기 조정
height, width = img.shape[:2]
max_width = 1200
max_height = 800
scale_w = max_width / width
scale_h = max_height / height
scale = min(scale_w, scale_h)

if scale < 1.0:
    new_width = int(width * scale)
    new_height = int(height * scale)
    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
else:
    resized_img = img

display_img = resized_img.copy() 

# 빨간색 테두리 검출 (색상 필터링)
hsv = cv2.cvtColor(display_img, cv2.COLOR_BGR2HSV)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

# 노이즈 제거용 모폴로지(닫힘)
kernel = np.ones((3, 3), np.uint8) 
red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel, iterations=1)


# Canny 에지 적용 
edges_from_mask = cv2.Canny(red_mask, 50, 150)
#cv2.imshow("Canny Edge from Mask", edges_from_mask) 디버그용

# 원 검출 (HoughCircles)
gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=100,
    param1=120,
    param2=30,
    minRadius=80,
    maxRadius=100
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # 검출한 원 그리기(중심 표시)
        cv2.circle(display_img, (i[0], i[1]), i[2], (0, 255, 0), 3)
        cv2.circle(display_img, (i[0], i[1]), 2, (0, 0, 255), 3)

# 삼각형 검출
# 허프 라인 변환 (HoughLinesP)
lines = cv2.HoughLinesP(edges_from_mask, 1, np.pi / 180, threshold=50, minLineLength=40, maxLineGap=10)

# 선 그리기
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(display_img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            
# 결과 출력
cv2.imshow('Detecting Circles and Triangles', display_img)
cv2.waitKey(0)
cv2.destroyAllWindows()