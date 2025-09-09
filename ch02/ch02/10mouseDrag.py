import cv2
import sys

img = cv2.imread('../data/girl_laughing.jpg')
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event, x, y, flags, param) :        # 마우스 콜백 함수
    global ix, iy

    if event == cv2.EVENT_LBUTTONDOWN :	# 마우스 왼쪽 버튼 클릭했을 때 초기 위치 저장
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP :		# 마우스 왼쪽 버튼 클릭했을 때 직사각형 그리기
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)

    # 1. RBUTTON에 대해 사각형 그리기
    elif event == cv2.EVENT_RBUTTONDOWN :	# 마우스 왼쪽 버튼 클릭했을 때 초기 위치 저장
        ix, iy = x, y
    elif event == cv2.EVENT_RBUTTONUP :	# 마우스 왼쪽 버튼 클릭했을 때 직사각형 그리기
        cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 255), 2)

    cv2.imshow('Drawing',img)
    
cv2.namedWindow('Drawing')   # 창에 이름 부여, 이벤트가 적용될 창을 부를 이름 명시
cv2.imshow('Drawing', img)

cv2.setMouseCallback('Drawing', draw)	# Drawing 윈도우에서 마우스 이벤트가 발생하면 호출될 draw 콜백 함수 지정

while(True) :		# 마우스 이벤트가 언제 발생할지 모르므로 무한 반복
    if cv2.waitKey(1) == ord('q') : # 'q' 키를 누르면 종료
        cv2.destroyAllWindows() 
        break