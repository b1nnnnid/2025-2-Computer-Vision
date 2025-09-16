import cv2
import numpy as np

img = np.ones((600,300,3), np.uint8) * 255 	# 600*300*3*8bits 행렬
# 행렬을 1로 초기화 -> 255 곱하기, 즉 1*255=255 -> 흰색으로 초기화

cv2.line(img, (50,50), (150,150), (255,0,0), 3) # 파란색(Blue) 선 그리기, 시작점~끝점, 두께 3

cv2.rectangle(img, (50,50), (150,150), (0,255,0), 2) # 초록색(Green) 사각형, 좌상단~우하단, 테두리 두께 2
cv2.rectangle(img, (50,200), (150,300), (0,255,0), cv2.FILLED) # 초록색(Green) 사각형, 내부 채움

cv2.circle(img, (220,100), 50, (0,0,255), 4) # 빨간색(Red) 원, 중심점, 반지름, 두께 4
cv2.circle(img, (220,250), 30, (0,255,255), -1)  # 노란색(Yellow) 원, 내부 채움

cv2.ellipse(img, (100, 400), (75, 50), 0, 0, 360, (0,255,0), 3) # 초록색(Green) 타원, 중심, 축, 각도, 두께 3

pts = np.array([[220,350], [180,500], [260,500]], dtype=np.int32) # 다각형 꼭짓점 좌표 배열
cv2.polylines(img, [pts], True, (255,0,0), 10) # 파란색(Blue) 폴리라인, 닫지 않음(False), 두께 10
#3False : 마지막점과 첫점을 연결할 것인가?

cv2.putText(img, "text1", (50,500), cv2.FONT_HERSHEY_DUPLEX, 1, (128, 128, 0), 2) # 텍스트 추가, 위치, 폰트, 크기, 색상, 두께
cv2.putText(img, "text2", (50,570), cv2.FONT_HERSHEY_TRIPLEX, 2, (221, 160, 221), 4) # 다른 폰트와 크기로 텍스트 추가

cv2.imshow('OpenGL Graphics',img)

cv2.waitKey()
cv2.destroyAllWindows()