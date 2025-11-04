# -1104

import cv2
import numpy as np
import sys

def onCornerHarris(thresh) :
    img = img_copy.copy()   # 원본 이미지 복사본
    CN = cv2.normalize(C, 0, 1100, cv2.NORM_MINMAX)  # 트랙바는 정수만 다룸
    # 2-1) C값에 대한 thresholding
    img[CN > thresh] = [0, 0, 255]

    # 2-2) 비최대 억제, Non-Maximum Suppression(NMS)
    # 주변 8개 픽셀과 비교하여 현재 픽이 모든 이웃보다 큰 경우에만 코너로 간주
    rcorners = []
    for j in range(1, CN.shape[0] - 1) :  
        for i in range(1, CN.shape[1] - 1) :
            # CN[j,i]가 thresh보다 크고, 3x3 이웃 중 모든 값보다 큰 경우(=8)를 찾음
            if CN[j, i] > thresh and sum(sum(CN[j, i] > CN[j - 1:j + 2, i - 1:i + 2])) == 8 :  
                rcorners.append((i, j))

    for pt in rcorners:
        cv2.circle(img, pt, 5, (255, 0, 255), -1)  # 좌표 표시

    print("임계값: %2d , 코너 개수: %2d" % (thresh, len(rcorners)))

    cv2.imshow("harris corner detect", img)

img = cv2.imread('../data/shapes5-2.png', cv2.IMREAD_COLOR)
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

img_copy = img.copy()   # 원본 이미지 복사본

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(gray, 3)

blockSize = 5  # 패치 크기
apertureSize = 3  # sobel 마스크 크기
k = 0.04
C = cv2.cornerHarris(median, blockSize, apertureSize, k)  # Harris 코너 검출

# 1) C값에 대한 thresholding
img[C > 0.05*C.max()] = [0, 0, 255]	# 임계값(0.05*C.max())보다 큰 C 위치의 img 픽셀을 빨간색으로
print(C.max(), 0.05*C.max())
cv2.imshow('harris detect', img)

# 2) C값에 대한 트랙바
thresh = 5  # 초기 코너 응답 임계값
onCornerHarris(thresh)
cv2.createTrackbar("Threshold", "harris corner detect", thresh, 30, onCornerHarris)	# 트랙바 생성
# ("트랙바 이름", "윈도우 창 제목", 트랙바 현재값 변수, 트랙바 최댓값, 트랙바 콜백 함수)

cv2.waitKey()
cv2.destroyAllWindows()