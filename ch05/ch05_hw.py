import cv2
import sys
import numpy as np

# 이미지 파일을 '1.png'로 저장했다고 가정합니다.
# 경로가 다르다면 '../data/1.png'를 실제 파일 경로로 수정하세요.
img = cv2.imread('../data/1.png') 
if img is None:
    sys.exit('파일을 찾을 수 없습니다. (1.png)')

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

# --- 원 검출 (수정하지 않는 부분) ---
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

# --- 사각형 검출 (수정된 부분) ---

# 1. 색상 필터링 (검은색 추출)
hsv = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 20, 150])
mask_black = cv2.inRange(hsv, lower_black, upper_black)

# (디버깅용) 검은색 마스크 확인
cv2.imshow("1. Black Mask", mask_black)

# 3. 엣지 검출
edges = cv2.Canny(mask_black, 100, 200)

# (디버깅용) 엣지 이미지 확인
cv2.imshow("3. Edges", edges)

# 4. 허프 라인 (HoughLinesP) 검출
# 'edges'는 이제 사각형 테두리의 엣지만을 가질 확률이 높습니다.
lines = cv2.HoughLinesP(
    edges, 
    rho=1, 
    theta=np.pi/180, 
    threshold=120, 
    minLineLength=80,  # 사각형 변의 최소 길이
    maxLineGap=15
)

# 5. 검출된 선 그리기
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        # 원본 이미지 위에 빨간색(0,0,255)으로 선분을 그립니다.
        cv2.line(display_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 최종 결과 이미지 표시
cv2.imshow("Detected Circles and Rectangle", display_img)
cv2.waitKey(0)
cv2.destroyAllWindows()