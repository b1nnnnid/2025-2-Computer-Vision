import numpy as np
import cv2
# img = cv2.imread('../data/soccer.jpg')
# if img is None :
#     sys.exit('파일을 찾을 수 없습니다.')

#3)흰색 배경 이미지 수정
img = np.ones((500,500,3), np.uint8)*255


BrushSize = 5               # 붓의 크기
LColor,RColor = (255,0,0),(0,0,255)      #파란색과 빨간색
aLColor, aRColor = (255,0,255),(0,255,255)   

#2) 마우스와 함께 수식키를 눌렀을 때, 빨간색/파란색 이 아닌 2개의 다른 색상이 추가
def painting(event, x, y, flags, param) :        # 마우스 콜백 함수
    #클릭
    if event == cv2.EVENT_LBUTTONDOWN :
        if flags&cv2.EVENT_FLAG_ALTKEY: 
            cv2.circle(img, (x,y), BrushSize, aLColor, -1) #좌클릭+알트키 핑크색
        else: 
            cv2.circle(img, (x,y), BrushSize, LColor, -1)  #좌클릭 파란색
    elif event == cv2.EVENT_RBUTTONDOWN :
        if flags&cv2.EVENT_FLAG_ALTKEY:
            cv2.circle(img, (x,y), BrushSize, aRColor, -1) #우클릭+알트키 노란색
        else:
            cv2.circle(img, (x,y), BrushSize, RColor, -1)  #우클릭 빨간색

    #드래그
    elif event == cv2.EVENT_MOUSEMOVE and flags&cv2.EVENT_FLAG_LBUTTON :
        if flags&cv2.EVENT_FLAG_ALTKEY:
            cv2.circle(img, (x,y), BrushSize, aLColor, -1) #좌클릭+알트키 핑크색
        else:
            cv2.circle(img, (x,y), BrushSize, LColor, -1)  #좌클릭 파란색
        
    elif event == cv2.EVENT_MOUSEMOVE and flags&cv2.EVENT_FLAG_RBUTTON :
        if flags&cv2.EVENT_FLAG_ALTKEY:
            cv2.circle(img, (x,y), BrushSize, aRColor, -1) #우클릭+알트키 노란색
        else:
            cv2.circle(img, (x,y), BrushSize, RColor, -1)  #우클릭 빨간색

    cv2.imshow('Painting', img)  # 수정된 이미지를 다시 그림

cv2.namedWindow('Painting')
cv2.imshow('Painting', img)

cv2.setMouseCallback('Painting', painting)   # Painting 윈도우에서 마우스 이벤트가 발생하면 호출될 paint 콜백 함수 지정

while(True) :     # 마우스 이벤트가 언제 발생할지 모르므로 무한 반복
    if cv2.waitKey(1) == ord('q') : # 'q' 키를 누르면 
        cv2.imwrite('paintingPractice.png', img) # 지금까지 그린 것을 이미지로 저장
        cv2.destroyAllWindows() 
        break
    
    
    
