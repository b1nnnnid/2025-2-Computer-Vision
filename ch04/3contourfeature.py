# - 1021

import cv2
import sys
import numpy as np

img = cv2.imread('../data/star.png')
#img = cv2.imread('../data/horse.png')
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

h,w = img.shape[:2]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,100,200)
#cv2.imshow('contours-canny',canny)

# 외곽 윤곽선 검출
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contour = contours[0]   # 하나의 객체 윤곽선 선택
cv2.drawContours(img, [contour], -1, (255, 0, 255), 2)  # contour 그리기
#cv2.imshow('contours',img)

# 1) perimeter & area : 윤곽선 길이와 면적 계산
# closed=True이면 폐곡선 도형 만들어 길이 계산, false면 시작점-끝점 연결 x
perimeter = cv2.arcLength(contour, closed=True)
print('perimeter=', perimeter)

area = cv2.contourArea(contour)
print('area=', area)

# 2) 최근접 직사각형(축에 평행한 직사각형)
x, y, width, height = cv2.boundingRect(contour)
cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 2)

# 3) 최소면적 직사각형(회전 가능한 직사각형)
rect = cv2.minAreaRect(contour) # (중심, (가로,세로), 기울기)
(cx, cy), (w, h), angle = rect
cv2.circle(img, (int(cx),int(cy)), 3, (0,0,255), -1)    # 중심점 표시
box = cv2.boxPoints(rect)   # (중심, (가로,세로), 기울기) => 4개의 꼭지점 좌표값(실수형) 계산
box = np.int32(box)         # 정수 좌표로 변환
print(box)
cv2.drawContours(img, [box], 0, (0, 255, 0), 2)    #cv2.polylines(img, [box], True, (0, 255,0), 2)

# 4) 최근접 원
(x, y), radius = cv2.minEnclosingCircle(contour)
cv2.circle(img, (int(x), int(y)), int(radius), (255, 0, 0), 2)

# 5) 최근접 다각형 : 꼭지점의 수를 줄여 단순화(근사)시킨 다각형
poly10 = cv2.approxPolyDP(contour, epsilon=10, closed=True)
poly20 = cv2.approxPolyDP(contour, epsilon=20, closed=True)
poly50 = cv2.approxPolyDP(contour, epsilon=50, closed=True)
# 2 : epsilon. 원래 contour와 근사 다각형 사이의 허용 거리. 값이 크면 저장되는 좌표점의 개수가 작아짐
# 3 : closed?(닫힌 다각형?)
#print(poly10.shape)
#print(poly20.shape)
#print(poly50.shape)
#cv2.drawContours(img, [poly10], 0, (0, 0, 255), 2) # cv2.polylines(img, [poly10], True, (0, 0, 255), 2)
#cv2.drawContours(img, [poly20], 0, (0, 255, 0), 2) # cv2.polylines(img, [poly20], True, (0, 255, 0), 2)
#cv2.drawContours(img, [poly50], 0, (255, 0, 0), 2) # cv2.polylines(img, [poly50], True, (255, 0, 0), 2)

# 6) 내부 점
for y in range(h) :
    for x in range(w) :
        if cv2.pointPolygonTest(contour, (x, y), False) > 0:  # 내부 점이면
            #img[y, x] = (255, 200, 255)
            pass
#cv2.fillPoly(img, [contour], (255,200,255))

# 7) 볼록 다각형
hull = cv2.convexHull(contour, returnPoints=True)
#cv2.drawContours(img, [hull], 0, (100, 100, 100), 2)
#print(hull.shape)

# 8) 블록 다각형의 결함 찾기
hull2 = cv2.convexHull(contour, returnPoints=False) # convexityDefects를 찾기 위해 returnPoints=False로
#print(hull2.shape)

defects = cv2.convexityDefects(contour, hull2)
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    print(i,' : ', s, e, f, d)
    #cv2.circle(img, tuple(contour[s][0]), 5, [128, 0, 255], -1)
    #cv2.circle(img, tuple(contour[e][0]), 5, [255, 0, 128], -1)
    #cv2.circle(img, tuple(contour[f][0]), 5, [128, 255, 0], -1)

cv2.imshow('contours', img)

cv2.waitKey()
cv2.destroyAllWindows()