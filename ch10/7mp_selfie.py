import cv2
import mediapipe as mp  
import numpy as np
import sys

mp_selfie_segmentation = mp.solutions.selfie_segmentation  # Mediapipe Selfie Segmentation 초기화

selfie = mp_selfie_segmentation.SelfieSegmentation(model_selection=1) # 배경 분리 모델 선택 (0: 일반, 1: 고화질)

cap = cv2.VideoCapture('../data/aerobics.mp4')    

# 배경 이미지 불러오기
bg = cv2.imread('../data/ds_zoombg11.png')   
if bg is None:
    sys.exit('파일을 찾을 수 없습니다.')
bg = cv2.resize(bg, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while True :
    ret, frame = cap.read()
    if not ret :
      print('프레임 획득에 실패하여 루프를 나갑니다.')
      break
    
    res = selfie.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    mask = res.segmentation_mask  # [H, W] 형태의 float32 mask (0~1) 
    condition = mask > 0.5        # 마스크 이진화 (임계값 0.5 기준으로 사람/배경 분리) True: 사람, False: 배경

    # 배경 이미지를 블러 처리해서 만들기
    #blurred = cv2.GaussianBlur(frame, (55, 55), 0)

    #output = np.where(condition[..., None], frame, blurred) # 마스크를 이용해 원본과 블러 배경을 합성
    output = np.where(condition[..., None], frame, bg) # 마스크를 이용해 원본과 지정 배경을 합성
    cv2.imshow("Selfie Segmentation (Background Blurred)", output)

    if cv2.waitKey(5) == ord('q') :
      break

cap.release()
cv2.destroyAllWindows()