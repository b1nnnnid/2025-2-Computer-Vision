import cv2
import numpy as np

color=cv2.imread('../data/lenna256.png')

# Special effects
bila = cv2.bilateralFilter(color, d=9, sigmaColor=75, sigmaSpace=75)  # 양방향 필터(노이즈 제거, 경계 보존)

edgep = cv2.edgePreservingFilter(color, flags=1, sigma_s=60, sigma_r=0.4)  # 경계 보존 필터

sty = cv2.stylization(color, sigma_s=60, sigma_r=0.45)  # 스타일화(만화 효과)

graySketch, colorSketch = cv2.pencilSketch(color, sigma_s=60, sigma_r=0.7, shade_factor=0.02)   # 연필 스케치 효과(흑백, 컬러)

oil = cv2.xphoto.oilPainting(color, 7, 1)   # 유화 효과

cgraySketch = cv2.cvtColor(graySketch, cv2.COLOR_GRAY2BGR) # 흑백 스케치를 컬러로 변환(결과 합치기 위해)
special = np.hstack((color, bila, edgep, sty, cgraySketch, colorSketch, oil))
cv2.imshow('Special Effects', special)

cv2.waitKey()
cv2.destroyAllWindows()