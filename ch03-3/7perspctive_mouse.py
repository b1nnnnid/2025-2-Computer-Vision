# -1016 ~ 1021

import cv2 
import numpy as np

def contain_pts(p, p1, p2) : # p가 p1~p2 사각형 안에 있는지 확인하는 함수
    return p1[0] <= p[0] < p2[0] and p1[1] <= p[1] < p2[1]

def draw_rect(img) : # 각 점 주변에 사각형을 그리고, 선택된 영역 밝기 증가
    rois = [(p - small, small * 2) for p in pts1]
    for (x, y), (w, h) in np.int32(rois):
        roi = img[y:y + h, x:x + w]  # 좌표 사각형 범위 가져오기
        val = np.full(roi.shape, 80, np.uint8)  # 컬러(3차원) 행렬 생성
        cv2.add(roi, val, roi)           # 관심영역 밝기 증가...80만큼
        cv2.rectangle(img, (x, y, w, h), (255, 0, 255), 2)
    cv2.polylines(img, [pts1.astype(int)], True, (255, 255, 0), 2)  # pts(numpy 배열) 4개 점 연결
    cv2.imshow("select rect", img)

def warp(img) :  # 원근 변환 행렬 계산 및 적용
    perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, perspect_mat, (400, 350), cv2.INTER_CUBIC)
    cv2.imshow("perspective transform", dst)

def onMouse(event, x, y, flags, param) :  # 마우스 이벤트 콜백 함수
    global check
    if event == cv2.EVENT_LBUTTONDOWN :  # 마우스 좌클릭 시
        for i, p in enumerate(pts1):    # 4개 점 주변 사각형 안에 클릭했는지 확인
            p1, p2 = p - small, p + small  # p점에서 우상단, 좌하단 좌표생성
            if contain_pts((x, y), p1, p2):
                check = i           # 클릭한 좌표 번호 저장

    if event == cv2.EVENT_LBUTTONUP :  # 마우스 좌클릭 해제 시
        check = -1  # 좌표 번호 초기화 => 선택 해제

    if check >= 0 :  # 좌표 사각형 선택 시, 점을 드래그하여 위치 변경
        pts1[check] = (x, y)
        draw_rect(np.copy(image))   # 변경된 위치에 사각형 다시 그림
        warp(np.copy(image))        # 변경된 위치에서 다시 원근 변환 적용

image = cv2.imread('../data/perspective2.jpg')

small = np.array((12, 12))  # 좌표 사각형 크기
check = -1  # 선택 좌표 사각형 번호 초기화
#각 쌍들이 대응됨
pts1 = np.float32([(100, 100), (300, 100), (300, 300), (100, 300)]) # 입력 이미지의 4개 점 좌표
pts2 = np.float32([(0, 0), (399, 0), (399, 349), (0, 349)]) # 출력 이미지의 4개 점 좌표

draw_rect(np.copy(image))   # 초기 사각형 및 다각형 그림

cv2.setMouseCallback("select rect", onMouse, 0) # 마우스 콜백 함수 등록

cv2.waitKey(0)
cv2.destroyAllWindows()