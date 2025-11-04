import cv2
import sys

img = cv2.imread('../data/apples.jpg')
#img = cv2.imread('../data/coins.png')
#img = cv2.imread('../data/eye_iris.jpg')
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 200, param1=150, param2=20, minRadius=50, maxRadius=120)    # 허프 원 검출 ---② # apples
#circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 80, param1=150, param2=20, minRadius=20, maxRadius=40)   # coins, eye_iris
# 2method : 검출방법, HOUGH_GRADIENT => Sobel 기반. 에지의 방향 정보 활용
# 3dp : 이미지해상도 : accumulator해상도, 1이면 두 해상도 같음
# 4dist : 검출된 원 중심 사이의 최소 거리
# 5param1 : canny의 높은 threshold  => 별도의 canny 적용 없이 에지 검출을 내부적으로 수행
# 6param2 : 누적 threshold
# 7minRadius, 8maxRadius : 검출할 원 반지름 범위
print(circles)
    
if circles is not None :
    for i in circles[0] :
        cv2.circle(img, (int(i[0]), int(i[1])), int(i[2]), (255, 0, 0), 2) # 검출된 원 그리기 ---③

cv2.imshow('Hough circles', img)

cv2.waitKey()
cv2.destroyAllWindows()