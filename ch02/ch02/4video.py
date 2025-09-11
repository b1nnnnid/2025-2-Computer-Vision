import cv2
import sys

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture('../data/slow_traffic_small.mp4')    # 비디오 파일에서 동영상 읽기
#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)        # 웹캠에서 동영상 읽기

if not cap.isOpened() : # 비디오 파일 또는 웹캠 연결 실패 시 프로그램 종료
    sys.exit('동영상 연결 실패')

while True :	# 무한 반복으로 비디오 프레임 처리
    ret, frame = cap.read()  # 비디오의 한 프레임 읽기

    if not ret : # ret는 프레임을 성공적으로 가져오면 true, 그렇지 않으면(비디오 종료) false(루프 종료)
        print('프레임 획득에 실패하여 루프를 나갑니다.') # 동영상 재생이 끝나서 더이상 가져올 프레임이 없을 때
        break

    cv2.imshow('Video display', frame)  # 읽은 프레임을 화면에 표시

    key = cv2.waitKey(1) # 1밀리초 동안 키보드 입력 기다림(정수)
    if key == ord('q') :  # 'q' 키가 들어오면 루프를 빠져나감, ord()는 문자를 아스키 값으로 변환하는 함수
        cv2.imwrite('./captured.png', frame)  # 현재 프레임을 이미지로 저장
        break

cap.release()  # 비디오 캡처 객체 해제(자원 반환)
cv2.destroyAllWindows()