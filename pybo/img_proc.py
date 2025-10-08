import cv2
import numpy as np

# 과제1) otsu, 히스토그램 평활화, CLAHE 실행
def otsu_binarization(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    th, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return th, binary

def histogram_equalization(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eqaulized = cv2.equalizeHist(gray)
    
    return eqaulized

def clahe_equalization(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_img = clahe.apply(gray)
    
    return clahe_img
    
# 과제2) 영역연산 함수 5개 추가(가우시안/샤프닝/양방향/에지보존/스타일)    
def gaussian_blur(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (13,13), 2.0)
    
    return blurred

def sharpening(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    sharpen = np.array([[0.0, -1.0, 0.0],     # 샤프닝 필터(중앙값 7)
                    [-1.0, 7.0, -1.0],
                    [ 0.0, -1.0, 0.0]])
    sharpened = cv2.filter2D(gray, -1, sharpen)    # 샤프닝 필터 적용
    
    return sharpened


def bilateral(image):
    bila = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)  # 양방향 필터(노이즈 제거, 경계 보존)
    
    return bila

def edge_preserving(image):
    preserved = cv2.edgePreservingFilter(image, flags=1, sigma_s=60, sigma_r=0.4)  # 경계 보존 필터
    
    return preserved

def style_filter(image):
    style = cv2.stylization(image, sigma_s=60, sigma_r=0.45)  # 스타일화(만화 효과)
    
    return style