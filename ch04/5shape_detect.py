import cv2
import sys
import numpy as np

def shape_detect(c) :   # 객체 모양 판별 함수
    shape = "undefined"
    peri = cv2.arcLength(c, True)   # 윤곽선 길이 계산
    approx = cv2.approxPolyDP(c, 0.03 * peri, True) # 윤곽선 단순화(꼭짓점 개수로 도형 판별)
    #print(len(approx))

    # 꼭짓점이 3개면 삼각형
    if len(approx) == 3 :
        shape = "triangle"
    # 꼭짓점이 4개면 사각형(정사각형/직사각형 구분)
    elif len(approx) == 4 :
        (x, y, w, h) = cv2.boundingRect(approx) # 외접 사각형 정보
        ar = w / float(h)   # 가로세로 비율
        # 비율이 1에 가까우면 정사각형, 아니면 직사각형
        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
    # 꼭짓점이 5개면 오각형
    elif len(approx) == 5 :
        shape = "pentagon"
    # 꼭짓점이 10개면 별 모양
    elif len(approx) == 10 :
        shape = "star"
    else :   # 그 외
        roundness = (4.0 * np.pi * cv2.contourArea(c)) / (peri * peri) # 원형 여부 판단(둥근 정도 계산)
        # 비율이 1에 가까우면 원형
        if roundness >= 0.85 and roundness <=1.15 :
            shape = "circle"

    return shape

img = cv2.imread('../data/shapes2.png')
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')
cv2.imshow('img', img)

h,w = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 100, 200)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for contour in contours :
    cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)

    shape = shape_detect(contour)   # 도형 종류 판별 함수 호출

    # 도형 중심에 도형 이름 표시
    m = cv2.moments(contour)
    #print(m)
    area = m['m00']  # Contour 면적, cv.contourArea(contour)
    cx, cy = int(m['m10'] / area), int(m['m01'] / area) # Contour 중심점(centroid)
    #print(cx,cy,area)
    cv2.putText(img, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)

    cv2.imshow("Image", img)

    k = cv2.waitKey()
    if k == ord('q') :
        cv2.destroyAllWindows()
        break