import cv2
import sys
import numpy as np

img = cv2.imread('../data/horse.png')
#img = cv2.imread('../data/star.png')
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

h,w = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 100, 200)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contour = contours[0]   # 가장 큰 윤곽선 선택
cv2.drawContours(img, [contour], -1, (255, 0, 255), 2)
cv2.imshow('Contour', img)

m = cv2.moments(contour)    # 모멘트 계산
print(m)    # m은 dict(딕셔너리로 제공)

area = m['m00']   # Contour 면적, cv.contourArea(contour)
cx, cy = m['m10']/area, m['m01']/area   # Contour 중심점(centroid)
perimeter = cv2.arcLength(contour, True)    # Contour 둘레 길이
print('면적=', area, '\n중점=(', cx, ',', cy, ')', '\n둘레=', perimeter)

col_dist = m['mu20']/area   # 열(가로)분산
row_dist = m['mu02']/area   # 행(세로)분산
cr_dist = m['mu11']/area    # 열행분산
p_axes = 0.5 * np.arctan(2*m['mu11']/(m['mu20']-m['mu02'])) * 180 / np.pi   # 주축(major axis) 방향 각도 계산 (degree)
print('열(가로)분산=', col_dist, '\n행(세로)분산=', row_dist, '\n열행분산= ', cr_dist, '\n주축 = ', p_axes)

cv2.waitKey()
cv2.destroyAllWindows()