import cv2
import sys
import matplotlib.pyplot as plt

fig = plt.figure()  # plot 창 생성
rows = 3  # plot에 포함될 subplot 행 개수
cols = 2  # plot에 포함될 subplot 열 개수


img = cv2.imread('../data/mistyroad.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)		    # 명암 영상으로 변환하고 출력
ax1 = fig.add_subplot(rows, cols, 1)    # 첫 번째 subplot으로 fig에 추가
ax1.axis("off")	# 축 숨기기 (일반적으로 이미지 표시할 때 축 숨김)
ax1.imshow(gray, cmap='gray')

h1 = cv2.calcHist([gray], [0], None, [256], [0, 256])	    # 히스토그램을 구해 출력
#print('원본 히스토그램 : ', h1)
ax2 = fig.add_subplot(rows, cols, 2)    # 두 번째 subplot으로 fig에 추가
ax2.plot(h1, color='r', linewidth=1)

equal = cv2.equalizeHist(gray)			            # 히스토그램을 평활화하고 출력
ax3 = fig.add_subplot(rows, cols, 3)    # 세 번째 subplot으로 fig에 추가
ax3.axis("off")	# 축 숨기기 (일반적으로 이미지 표시할 때 축 숨김)
ax3.imshow(equal, cmap='gray')

h2 = cv2.calcHist([equal], [0], None, [256], [0, 256])	    # 히스토그램을 구해 출력
#print('히스토그램 평활화 : ', h2)
ax4 = fig.add_subplot(rows, cols, 4)    # 네 번째 subplot으로 fig에 추가
ax4.plot(h2, color='g', linewidth=1)

# 대비 제한 적응형 히스토그램 평활화(Contrast Limited AHE, CLAHE)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) # CLAHE 객체 생성
clahe_img = clahe.apply(gray)                  # CLAHE 적용
ax5 = fig.add_subplot(rows, cols, 5)    # 다섯 번째 subplot으로 fig에 추가
ax5.axis("off")	# 축 숨기기 (일반적으로 이미지 표시할 때 축 숨김)
ax5.imshow(clahe_img, cmap='gray')

h3 = cv2.calcHist([clahe_img], [0], None, [256], [0, 256])	    # 히스토그램을 구해 출력
#print('대비 제한 AHE : ', h3)
ax6 = fig.add_subplot(rows, cols, 6)    # 여섯 번째 subplot으로 fig에 추가
ax6.plot(h3, color='b', linewidth=1)

plt.show()  # 모든 subplot을 포함한 plot 창 출력

cv2.destroyAllWindows()