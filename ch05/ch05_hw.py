import cv2
import sys
import numpy as np


img = cv2.imread('../data/1.png')
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
        
        
        
        
# 사각형 검출
# Canny 에지 검출 (HoughLinesP의 입력)
edges = cv2.Canny(blur, 50, 150)

# HoughLinesP를 사용하여 선분 검출
# threshold=100
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=80, maxLineGap=10)

# 사각형 표지판 ROI 정의 및 각도 임계값
Y_THRESHOLD = resized_img.shape[0] * 0.70  # 이미지 높이 70% 지점 아래만
ANGLE_TOLERANCE = np.pi / 45              # 각도 허용 오차?

horizontal_lines = []
vertical_lines = []

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        
        # 1. ROI 필터링: 표지판 영역 아래의 선분만 고려
        if min(y1, y2) < Y_THRESHOLD:
            continue
            
        # 각도 계산 (라디안)
        angle = np.arctan2(y2 - y1, x2 - x1)
        
        # 각도를 0 ~ pi 범위로 정규화
        if angle < 0:
            angle += np.pi
            
        # 2. 수평선 필터링 (각도 0 또는 pi 근처)
        is_horizontal = (0 <= angle < ANGLE_TOLERANCE) or (np.pi - ANGLE_TOLERANCE <= angle <= np.pi)
        
        # 3. 수직선 필터링 (각도 pi/2 근처)
        is_vertical = (np.pi / 2 - ANGLE_TOLERANCE <= angle <= np.pi / 2 + ANGLE_TOLERANCE)
        
        if is_horizontal:
            horizontal_lines.append(line[0])
        elif is_vertical:
            vertical_lines.append(line[0])


# --- Bounding Box 및 코너 계산 ---

# 검출된 수평선/수직선 좌표를 클러스터링하여 대표 선분을 찾음
def get_dominant_lines(lines, is_horizontal):
    coords = []
    # 1. 수평선(Y)은 선분 끝점 사용, 수직선(X)은 선분 끝점 사용
    for line in lines:
        coords.extend([line[1], line[3]]) if is_horizontal else coords.extend([line[0], line[2]])
    
    if not coords: return []

    coords.sort()
    
    # 클러스터링: 20픽셀 이내의 가까운 좌표
    coord_clusters = []
    current_cluster = [coords[0]]
    for i in range(1, len(coords)):
        if coords[i] - current_cluster[-1] < 20: 
            current_cluster.append(coords[i])
        else:
            coord_clusters.append(current_cluster)
            current_cluster = [coords[i]]
    coord_clusters.append(current_cluster)

    # 2. 클러스터 크기를 기반으로 상위 2개의 대표 좌표만 선택 (배경 노이즈 제거)
    coord_clusters.sort(key=len, reverse=True)
    
    dominant_coords = []
    
    # 상위 2개 클러스터의 평균 좌표를 대표 좌표로 사용...
    for cluster in coord_clusters[:2]:
        dominant_coords.append(int(np.mean(cluster)))
    
    # 3. 대표 좌표가 2개 미만인 경우 실패 방지
    if len(dominant_coords) < 2:
        return []
        
    return sorted(dominant_coords) # 정렬된 2개의 대표 좌표 (min, max) 반환


# Canny 에지 검출
edges = cv2.Canny(blur, 50, 150)

# HoughLinesP를 사용하여 선분 검출
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=80, maxLineGap=10)

Y_THRESHOLD = resized_img.shape[0] * 0.70  
ANGLE_TOLERANCE = np.pi / 45              

horizontal_lines = []
vertical_lines = []

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        
        if min(y1, y2) < Y_THRESHOLD:
            continue
            
        angle = np.arctan2(y2 - y1, x2 - x1)
        if angle < 0:
            angle += np.pi
            
        is_horizontal = (0 <= angle < ANGLE_TOLERANCE) or (np.pi - ANGLE_TOLERANCE <= angle <= np.pi)
        is_vertical = (np.pi / 2 - ANGLE_TOLERANCE <= angle <= np.pi / 2 + ANGLE_TOLERANCE)
        
        if is_horizontal:
            horizontal_lines.append(line[0])
        elif is_vertical:
            vertical_lines.append(line[0])

dom_y = get_dominant_lines(horizontal_lines, True)
dom_x = get_dominant_lines(vertical_lines, False)


# 4. 4개 꼭짓점 계산 및 시각화
if len(dom_y) == 2 and len(dom_x) == 2:
    
    top_y = min(dom_y)
    bottom_y = max(dom_y)
    left_x = min(dom_x)
    right_x = max(dom_x)
    
    # Bounding Box 그리기
    cv2.rectangle(display_img, (left_x, top_y), (right_x, bottom_y), (255, 0, 0), 3)

    # 4개의 꼭짓점 표시
    corners = [
        (left_x, top_y),
        (right_x, top_y),
        (right_x, bottom_y),
        (left_x, bottom_y)
    ]
    for cx, cy in corners:
        cv2.circle(display_img, (cx, cy), 7, (0, 255, 255), -1)

# 결과 출력
cv2.imshow('Hough Lines Rectangles and Circles', display_img)
cv2.waitKey(0)
cv2.destroyAllWindows()