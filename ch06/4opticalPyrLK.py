# - 1113

import numpy as np
import cv2
import sys

cap = cv2.VideoCapture('../data/slow_traffic_small.mp4')
if not cap.isOpened() :
    sys.exit('동영상 연결 실패')

ret, prev_frame = cap.read()		# 첫 프레임
prev_gray = cv2.cvtColor(prev_frame,cv2.COLOR_BGR2GRAY)

# 준비 for PyrLK
color = np.random.randint(0, 255, (100,3))  # 추적 시 사용할 랜덤 색상(궤적 표시용)
# Good Features to Track 파라미터
feature_params = dict(
    maxCorners=100,     # 검출할 최대 코너 수
    qualityLevel=0.3,   # 코너 품질 임계값 (높을수록 좋은 코너만)
    minDistance=7,      # 코너 간 최소 거리
    blockSize=7         # 코너 검출에 사용하는 블록 크기
)
# Lucas-Kanade optical flow 파라미터
lk_params = dict(
    winSize=(15, 15),   # 윈도우 크기
    maxLevel=2,         # 피라미드 레벨 수
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
    # 반복 종료 기준: 최대 반복 10회 또는 변화량 0.03 이하일 때
)

# 첫 프레임에서 추적할 코너(특징점) 검출
p0 = cv2.goodFeaturesToTrack(prev_gray, mask=None, **feature_params)   
mask = np.zeros_like(prev_frame)	# 물체의 이동 궤적을 그릴 영상, 검은 영상으로 초기화

while (1) :
    ret, curr_frame = cap.read()  # 비디오를 구성하는 프레임 획득
    if not ret :
        sys('프레임 획득에 실패하여 루프를 나갑니다.')

    curr_gray = cv2.cvtColor(curr_frame,cv2.COLOR_BGR2GRAY)

    # PyrLK로 optical flow 계산: 이전 프레임의 p0에 대응되는 현재 프레임의 p1, 매칭 플래그, 에러
    p1, match, err = cv2.calcOpticalFlowPyrLK(prev_gray, curr_gray, p0, None, **lk_params)

    if p1 is not None :		# 양호한 쌍 선택 : p0(이전프레임 특징)과 매치되는 p1(현프레임 특징)이 존재하면
        good_curr = p1[match==1]  # good_curr에 현프레임 특징 p1저장
        good_prev = p0[match==1]  # good_curr에 이전프레임 특징 p0저장
        
        for i in range(len(good_curr)) : # 모든 매칭된 특징들의 이동 궤적 그리기
            x1, y1 = int(good_curr[i][0]), int(good_curr[i][1]) # 현재 프레임 좌표
            x0, y0 = int(good_prev[i][0]), int(good_prev[i][1]) # 이전 프레임 좌표

            # 마스크에 이전->현재 선을 그림 (색상은 미리 생성한 랜덤 색상 사용)
            mask = cv2.line(mask, (x1,y1), (x0,y0), color[i].tolist(), 2)

            # 현재 프레임에는 특징점 위치를 원으로 표시
            curr_frame = cv2.circle(curr_frame, (x1,y1), 5, color[i].tolist(), -1) # img = frame에 직접 특징점 표시

        # 마스크(궤적)와 현재 프레임을 합성하여 화면에 표시    
        img = cv2.add(curr_frame, mask) 
        cv2.imshow('LTK tracker', img)

        # 다음 루프를 위해 이전 프레임 및 특징점 업데이트
        prev_gray = curr_gray	        # 현재 프레임을 이전 프레임으로
        p0 = good_curr.reshape(-1,1,2)  # 현재 프레임 특징 p1을 p0로
    else:
        # p1이 None인 경우(특징점이 전혀 추적되지 않음) 현재 프레임만 표시
        cv2.imshow('LTK tracker', curr_frame)
        prev_gray = curr_gray
        # p0를 다시 검출하여 재초기화(옵션) 
        p0 = cv2.goodFeaturesToTrack(prev_gray, mask=None, **feature_params)

    key = cv2.waitKey(30)	# 30밀리초 동안 키보드 입력 기다림
    if key == ord('q') :	# 'q' 키가 들어오면 루프를 빠져나감
        break

cap.release()			# 카메라와 연결을 끊음
cv2.destroyAllWindows()