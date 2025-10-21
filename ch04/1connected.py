# - 1021

import cv2
import sys
import numpy as np

img = cv2.imread('../data/coins.png')
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(gray, 3)    # 미디언 블러로 노이즈 제거
_, gray_bin = cv2.threshold(median, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # Otsu 이진화
#cv2.imshow('Binary', gray_bin)

# 1) 연결 요소 분석 (Connected Components Analysis)
cnt, labels = cv2.connectedComponents(gray_bin) # connectivity=8 기본값
print(cnt)
cv2.imshow('labelling',(labels*60).astype(np.uint8))

# 2) labelled 객체 (통계) 정보
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(gray_bin)
print(stats)
print(centroids)

# 영역 표시 : 라벨 값에 따라 이미지 색상 지정, 즉 같은 라벨을 갖는 픽셀을 같은 색으로 지정
img[labels == 0] = [127, 127, 127]  # 배경 회색
img[labels == 1] = [127, 0, 0]      # labels이 1인 모든 img 픽셀 = 파랑
img[labels == 2] = [0, 127, 0]      # labels이 2인 모든 img 픽셀 = 초록
img[labels == 3] = [0, 0, 127]      # labels이 3인 모든 img 픽셀 = 빨강
img[labels == 4] = [0, 127, 127]    # labels이 4인 모든 img 픽셀 = 청록 

for i in range(1, cnt) : # 모든 라벨 영역에 대해, 0(배경) 제외
    (x, y, w, h, area) = stats[i]   # i번째 라벨 영역의 통계 정보 추출
    (cx, cy) = centroids[i]         # i번째 라벨 영역의 중심점 좌표 추출

    if area < 20 :    # 면적이 20 미만인 영역 스킵(노이즈 제거)
        continue

    cv2.rectangle(img, (x, y, w, h), (255, 0, 255), 2) # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2) # 각 영역마다 크기에 맞는 사각형 그리기
    cv2.circle(img, (int(cx), int(cy)), 2, (0, 0, 255), -1) # 각 영역의 중심점 표시

cv2.imshow('Connected components', img)

cv2.waitKey()
cv2.destroyAllWindows()