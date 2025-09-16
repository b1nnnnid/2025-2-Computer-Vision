import cv2
import sys

cap = cv2.VideoCapture('../data/slow_traffic_small.mp4')    # 비디오 파일
#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)    # 웹캠 비디오
if not cap.isOpened():
    sys.exit('동영상 연결 실패')

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),   # 프레임의 너비와 높이 얻기
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)   # 프레임 크기 출력

fps = cap.get(cv2.CAP_PROP_FPS) # 프레임 속도(FPS) 얻기
print('fps =', fps)

fourcc = cv2.VideoWriter_fourcc(*'XVID')        # 비디오 코덱 지정(XVID)
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')        # 비디오 코덱 지정(DIVX)
#fourcc = cv2.VideoWriter_fourcc(*'MJPG')        # 비디오 코덱 지정(MJPG)
#fourcc = cv2.VideoWriter_fourcc(*'X264')        # 비디오 코덱 지정(X264)
#fourcc = cv2.VideoWriter_fourcc(*'MP4V')        # 비디오 코덱 지정(MP4V)

outV = cv2.VideoWriter('./record.mp4', fourcc, fps, frame_size) # 비디오 저장 객체 생성

while True :	# 무한 반복으로 비디오 프레임 처리
    ret, frame = cap.read()  # 비디오의 한 프레임 읽기
    if not ret :
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    #outV.write(frame)  # 프레임을 비디오 파일로 저장
    cv2.imshow('Video display', frame)  # 읽은 프레임을 화면에 표시

    key = cv2.waitKey(1)  # 1밀리초 동안 키보드 입력 기다림
    if key == ord('q') :  # 'q' 키가 들어오면 루프를 빠져나감
        break

cap.release()  # 비디오 캡처 객체 해제(자원 반환)
cv2.destroyAllWindows()