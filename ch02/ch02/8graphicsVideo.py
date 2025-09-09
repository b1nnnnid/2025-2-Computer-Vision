import cv2
import sys
import numpy as np

cap = cv2.VideoCapture('../data/slow_traffic_small.mp4') # 동영상을 가져오는 클래스
if not cap.isOpened():
    sys.exit('카메라 연결 실패')
    
while True :
    ret, frame = cap.read()
    if not ret :
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    # 1. 고정 도형 드리기
#    pts = np.array([[180, 100], [190, 210], [300, 340]], dtype=np.int32) # 다각형 꼭짓점 좌표
#    cv2.polylines(frame, [pts], False, (255, 0, 0), 10) # 파란색 폴리라인
#    cv2.line(frame, (400, 100), (640, 200), (0, 255, 0), 10) # 초록색 직선

    # 2. 랜덤 원 그리기
#    y = np.random.rand() * frame.shape[0] # 랜덤 y좌표 : 0~1 * 이미지 높이
#    x = np.random.rand() * frame.shape[1] # 랜덤 x좌표 : 0~1 * 이미지 너비
#    cv2.circle(frame, (int(x),int(y)), 20, (0,255,255), -1)    # 노란색 원

    cv2.imshow('Video display', frame) # 읽은 프레임에 도형을 그린 프레임을 화면에 표시

    key = cv2.waitKey(1)
    if key == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()