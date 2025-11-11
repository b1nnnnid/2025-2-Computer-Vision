import cv2
import sys

cap = cv2.VideoCapture('../data/slow_traffic_small.mp4')    # 비디오 파일
if not cap.isOpened() :
    sys.exit('동영상 연결 실패')

ret, prev_frame = cap.read()		# 첫 프레임
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_RGB2GRAY)

while True :

    ret, curr_frame = cap.read()	# 비디오를 구성하는 프레임 획득
    if not ret :
        sys('프레임 획득에 실패하여 루프를 나갑니다.')

    curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_RGB2GRAY)

    # 두 프레임의 차 영상 계산
    diff = cv2.absdiff(curr_gray, prev_gray)
    cv2.imshow('Difference in Video', diff)

    prev_gray = curr_gray   # 현재 프레임을 이전 프레임으로

    key = cv2.waitKey(30)	# 30밀리초 동안 키보드 입력 기다림
    if key == ord('q'):	# 'q' 키가 들어오면 루프를 빠져나감
        break 

cap.release()  # 카메라와 연결을 끊음
cv2.destroyAllWindows()
