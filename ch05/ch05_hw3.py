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

gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# 히스토그램 평활화: 대비 높이기
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
gray_equalized = clahe.apply(gray)

kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])
sharpened_img = cv2.filter2D(gray_equalized, -1, kernel_sharpening)

blur = cv2.medianBlur(sharpened_img, 5) 


# --- 원 검출 (HoughCircles) ---
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 30, param1=70, param2=20, minRadius=30, maxRadius=140) 

if circles is not None:
    circles = np.uint16(np.around(circles))
    valid_circles = []
    for i in circles[0, :]:
        cx, cy, r = i[0], i[1], i[2]
        
        # 1. 위치 필터링 
        if cx > resized_img.shape[1] * 0.6 and cy < resized_img.shape[0] * 0.8: 
             # 2. 반지름 필터링: 노이즈 제거
             if 45 <= r <= 130: 
                valid_circles.append(i)

    # 가장 확실한 원만 표시
    if len(valid_circles) > 0:
        i = valid_circles[0] 
        cv2.circle(display_img, (i[0], i[1]), i[2], (0, 255, 0), 2) 
        cv2.circle(display_img, (i[0], i[1]), 2, (0, 0, 255), 3)   
        

# --- 삼각형 검출: 색 기반 모폴로지지
hsv = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

# 빨간 색 범위: HSV에서 두 구간으로 나눠 처리 
lower_red1 = np.array([0, 80, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 80, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

# 모폴로지: 닫힘으로 테두리 잡음 메우고 외곽 연결
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
red_closed = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel, iterations=2)
red_closed = cv2.dilate(red_closed, kernel, iterations=1)

# 작은 노이즈 제거
red_closed = cv2.medianBlur(red_closed, 5)

# 외곽선 찾기
contours, _ = cv2.findContours(red_closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area = cv2.contourArea(contour)
    if area < 1500:   # 표지판 경계는 충분히 큰 면적이므로 임계값을 높게 잡음
        continue

    # 근사화
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    num_vertices = len(approx)

    x, y, w, h = cv2.boundingRect(approx)
    if w < 60 or h < 60:
        continue

    aspect_ratio = float(w) / (h + 1e-6)

    # 위치 필터 완화: 상단 60% 까지 허용 
    if y > resized_img.shape[0] * 0.6:
        continue

    # 꼭짓점 세기, 비율
    if num_vertices== 3 and 0.4 < aspect_ratio < 1.6:
        # 외곽 그리기 (파란색)
        cv2.drawContours(display_img, [approx], 0, (255, 0, 0), 3)
        for point in approx:
            px, py = point[0]
            cv2.circle(display_img, (px, py), 6, (0,255,255), -1)
        

# 결과 출력
cv2.imshow('Traffic Sign Detection', display_img)
cv2.waitKey(0)
cv2.destroyAllWindows()