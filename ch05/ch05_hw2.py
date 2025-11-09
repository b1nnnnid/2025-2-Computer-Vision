import cv2
import sys
import numpy as np


img = cv2.imread('../data/2.png')
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

display_img = resized_img.copy() # 검출용 복사 이미지

gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5) # 노이즈 제거(중앙값 블러)

# 원 검출 (HoughCircles)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 100, param1=150, param2=50, minRadius=100, maxRadius=150)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # 검출한 원 그리기
        cv2.circle(display_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(display_img, (i[0], i[1]), 2, (0, 0, 255), 3)
        
# --- 삼각형 검출 (Contours) ---

# Canny 에지 검출
edges = cv2.Canny(gray, 30, 100, apertureSize=3)

# 컨투어 찾기
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area = cv2.contourArea(contour)
    # 너무 작은 컨투어 무시 
    if area < 3000: 
        continue

    # 컨투어 근사화
    epsilon = 0.03 * cv2.arcLength(contour, True) 
    approx = cv2.approxPolyDP(contour, epsilon, True)

    num_corners = len(approx)
    
    # 1. 꼭짓점 개수 확인
    if num_corners == 3:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        
        # 2. 정삼각형에 가까운 비율
        if 0.8 < aspect_ratio < 1.3:
            
            # 3. 위치 조건...대략적 위치치
            if x > resized_img.shape[1] * 0.4 and y < resized_img.shape[0] * 0.5:
                
                # 검출된 삼각형 외곽선 그리기 (파란색)
                cv2.drawContours(display_img, [approx], 0, (255, 0, 0), 3)
                
                # 4. 꼭짓점 위치 표시 (노란색)
                for point in approx:
                    px, py = point[0]
                    cv2.circle(display_img, (px, py), 7, (0, 255, 255), -1)
        
        
# 결과 출력
cv2.imshow('Hough Lines Rectangles and Triangles', display_img)
cv2.waitKey(0)
cv2.destroyAllWindows()