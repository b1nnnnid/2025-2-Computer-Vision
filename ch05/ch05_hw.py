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

# 그레이 이미지
gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 1) # 노이즈 제거(가우시안 블러)

# 원 검출 (HoughCircles)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 100, param1=150, param2=50, minRadius=100, maxRadius=150)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # 검출한 원 그리기(중심 표시)
        cv2.circle(display_img, (i[0], i[1]), i[2], (0, 255, 0), 3)
        cv2.circle(display_img, (i[0], i[1]), 2, (0, 0, 255), 3)

#사각형 검출
# 히스토그램 평활화
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(9, 9)) 
clahe_img = clahe.apply(gray)
# 블러: 중앙값, 가우시안
blur_rec = cv2.medianBlur(clahe_img, 5)
blur_rec2 = cv2.GaussianBlur(blur_rec, (7, 7), 10) 
# 캐니 에지 검출
edges = cv2.Canny(blur_rec2, 50, 300)

# 허프 선 검출(HoughLinesP)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=80, maxLineGap=20)
print(lines)

# 검출선 그리기(사각형)
for line in lines:             
    x1, y1, x2, y2 = line[0]          
    cv2.line(display_img, (x1,y1), (x2, y2), (0,255,0), 3)  

# 최종 결과 이미지 표시
cv2.imshow("Detected Circles and Rectangle", display_img)
cv2.waitKey(0)
cv2.destroyAllWindows()