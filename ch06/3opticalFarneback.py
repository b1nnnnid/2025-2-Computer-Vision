# - 1113

import numpy as np
import cv2
import sys

cap = cv2.VideoCapture('../data/slow_traffic_small.mp4') #piano_hands.mp4') #aerobics.mp4') #checkBoard3x3.avi')
if not cap.isOpened() :
    sys.exit('동영상 연결 실패')

ret, prev_frame = cap.read()		# 첫 프레임
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while(1) :
    ret, curr_frame = cap.read()	# 비디오를 구성하는 프레임 획득
    if not ret :
        sys('프레임 획득에 실패하여 루프를 나갑니다.')

    curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
    # Farneback 광류(optical flow) 계산
    # 0.5: pyramid scale (이미지 피라미드의 축소 비율)
    # 3: levels (피라미드 레벨 수)
    # 15: winsize (평균을 구할 윈도우 크기)
    # 3: iterations (각 레벨에서의 반복 횟수)
    # 5: poly_n (다항식 확장 윈도우 크기)
    # 1.2: poly_sigma (다항식 시그마)
    # 0: flags
    flow = cv2.calcOpticalFlowFarneback(prev_gray, curr_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)    

    # 일정 간격의 그리드 포인트에서 광류 벡터를 시각화
    # y,x를 8픽셀 간격으로 건너뛰면서 화살표(선)를 그림
    for y in range(16//2, curr_gray.shape[0], 8) :      # (8부터, h까지, +8씩)  #16): 
        for x in range(16//2, curr_gray.shape[1], 8) :  # (8부터, w까지, +8씩)  #16):
            dx, dy = flow[y, x].astype(int)
             
            if (dx*dx+dy*dy) > 1 :  # 벡터 크기가 크면
                cv2.line(curr_frame, (x,y), (x+dx,y+dy), (0,0,255), 2)  # 빨간색 선
            else :  # 벡터 크기가 작으면
                cv2.line(curr_frame, (x,y), (x+dx,y+dy), (0,255,0), 2)  # 녹색 선

    cv2.imshow('Optical flow', curr_frame)

    prev_gray = curr_gray   # 현재 프레임을 이전 프레임으로

    key = cv2.waitKey(30)	# 30밀리초 동안 키보드 입력 기다림
    if key == ord('q'):	# 'q' 키가 들어오면 루프를 빠져나감
        break 
    
cap.release()			# 카메라와 연결을 끊음
cv2.destroyAllWindows()