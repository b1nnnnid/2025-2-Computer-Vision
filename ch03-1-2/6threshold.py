#-- 0923
import cv2
import numpy as np


#변환 전 원본 이미지
gray=cv2.imread('../data/grayscale.png', cv2.IMREAD_GRAYSCALE) # BGR 컬러 영상을 명암 영상으로 변환하여 저장

# 다양한 임계값 방식으로 이진화 및 변환...바이너리(인버스)가 가장 많이 쓰임
# threshold = 120 ... 값이 클수록 검정이, 작을수록 흰색이 많아짐

ret, img_binaryB = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # 임계값 이하: 0, 초과: 255
cv2.putText(img_binaryB,"BINARY",(20,30),cv2.FONT_HERSHEY_PLAIN,1.5, 255, 2)  

ret, img_binaryBINV = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)  # 임계값 이하: 255, 초과: 0
cv2.putText(img_binaryBINV,"BINARY_INV",(20,30),cv2.FONT_HERSHEY_PLAIN,1.5, 0, 2)

ret, img_binaryT = cv2.threshold(gray, 120, 255, cv2.THRESH_TRUNC)  # 임계값 이하: 원본값, 초과: 임계값
cv2.putText(img_binaryT,"TRUNC",(20,30),cv2.FONT_HERSHEY_PLAIN,1.5, 0, 2)

ret, img_binaryT0 = cv2.threshold(gray, 120, 255, cv2.THRESH_TOZERO)  # 임계값 이하: 0, 초과: 원본값
cv2.putText(img_binaryT0,"TOZERO",(20,30),cv2.FONT_HERSHEY_PLAIN,1.5, 255, 2)

ret, img_binaryT0INV = cv2.threshold(gray, 120, 255, cv2.THRESH_TOZERO_INV)  # 임계값 이하: 원본값, 초과: 0
cv2.putText(img_binaryT0INV,"TOZERO_INV",(20,30),cv2.FONT_HERSHEY_PLAIN,1.5, 0, 2)

img_binary=np.vstack((gray,img_binaryB, img_binaryBINV, img_binaryT, img_binaryT0, img_binaryT0INV))
cv2.imshow('threshold',img_binary)

cv2.waitKey()
cv2.destroyAllWindows()