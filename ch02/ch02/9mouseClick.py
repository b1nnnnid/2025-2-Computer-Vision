import cv2
import sys

img = cv2.imread('../data/girl_laughing.jpg')
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event, x, y, flags, param) :		# 마우스 콜백 함수
    # x,y는 마우스 위치
    # flags는 마우스 이벤트가 발생할 때의 특정 조건 : shift, Ctrl, Alt 등 키 조합 생성

    if event == cv2.EVENT_LBUTTONDOWN :	# 마우스 왼쪽 버튼 클릭했을 때
        # 1. Mouse + 특수키
#        if flags&cv2.EVENT_FLAG_SHIFTKEY:  # Shift 키를 눌렀을 때
#        if flags == cv2.EVENT_FLAG_SHIFT : # Shift 키"만" 눌렀을 때
        cv2.rectangle(img, (x, y), (x+200, y+200), (0, 0, 255), 2)
    elif event == cv2.EVENT_RBUTTONDOWN :	# 마우스 오른쪽 버튼 클릭했을 때
        cv2.rectangle(img, (x, y), (x+100, y+100), (255, 0, 0), 2)

    cv2.imshow('Drawing', img)
    
cv2.namedWindow('Drawing')   # 창에 이름 부여, 이벤트가 적용될 창을 부를 이름 명시
cv2.imshow('Drawing', img)

cv2.setMouseCallback('Drawing', draw)	# Drawing 윈도우에서 마우스 이벤트가 발생하면 호출될 draw 콜백 함수 지정

while(True) :		# 마우스 이벤트가 언제 발생할지 모르므로 무한 반복
    if cv2.waitKey(1) == ord('q') : # 'q' 키를 누르면 종료
        cv2.destroyAllWindows() 
        break