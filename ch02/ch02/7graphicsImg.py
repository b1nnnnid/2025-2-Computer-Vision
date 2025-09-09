import cv2
import sys

img = cv2.imread('../data/girl_laughing.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

#cv2.rectangle(img, (830,30), (1000,200), (0,0,255), 2)	# 빨간색 직사각형, 좌상단~우하단, 두께 2
#cv2.putText(img, 'laugh', (830,24), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)	# 파란색 글씨 쓰기, 위치, 폰트, 크기, 두께

#cv2.line(img, (830,30), (1000,200), (0,0,255), 2)	# 빨간색 직선, 시작점~끝점, 두께 2
#cv2.circle(img, (915,115), 85, (0,255,0), -1)    # 초록색 원, 중심, 반지름, 내부 채움

cv2.imshow('Draw', img)

cv2.waitKey()
cv2.destroyAllWindows()