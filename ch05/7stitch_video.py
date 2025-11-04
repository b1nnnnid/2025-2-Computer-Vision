import cv2
import sys

cap = cv2.VideoCapture('../data/duksung.mp4')    # 비디오 파일
if not cap.isOpened():
    sys.exit('동영상 연결 실패')

stitcher = cv2.Stitcher.create()    # Stitcher 생성 (프레임들을 이어붙여 파노라마 생성)
images = []  # 스티칭할 프레임을 저장할 리스트

i=0
STEP = 20
while True:
    i += 1
    ret, frame = cap.read()  # 비디오를 구성하는 프레임 획득

    if not ret: # ret는 프레임을 성공적으로 가져오면 true, 그렇지 않으면(동영상 종료) false
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    cv2.imshow('Video display', frame)

    #frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5)    # 필요한 경우 프레임 크기 조정

    if i%STEP == 0:		# STEP 간격으로 프레임을 골라 스티칭 입력으로 사용
        images.append(frame)
        
    key = cv2.waitKey(1)  # 1밀리초 동안 키보드 입력 기다림(정수)
    if key == ord('q'):  # 'q' 키가 들어오면 루프를 빠져나감, ord()는 문자를 아스키 값으로 변환하는 함수
        break

status, dst = stitcher.stitch(images)   # 수집한 이미지들로 스티칭 수행
if status == cv2.STITCHER_OK:
    cv2.imshow('stitching',  dst)

cv2.waitKey()
cap.release()  # 카메라와 연결을 끊음
cv2.destroyAllWindows()
