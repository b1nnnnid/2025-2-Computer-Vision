from ultralytics import YOLO
import cv2
import sys
import numpy as np

seg_model = YOLO("yolov8n-seg.pt")  # 사전 학습된 YOLOv8 분할 모델 로드, 자동 다운로드

img = cv2.imread('../data/busy_street.jpg')   # london_street.png
if img is None : 
    sys.exit('파일이 없습니다.')

results = seg_model(img)
result = results[0]         # 첫번째(단일) 이미지의 예측

annotated = result.plot()        # mask + bbox 그려진 결과 이미지
cv2.imshow("YOLOv8 Segmentation", annotated)

# result.masks : 분할(segmentation) 결과(있을 때). 마스크 텐서/비트맵 포함
#if result.masks is not None:
    # result.masks.data -> (N, H, W) (또는 boolean mask 형태일 수 있음)
#    mdata = result.masks.data.cpu().numpy()   # tensor -> numpy

#    H_img, W_img = img.shape[:2]
#    for i, mask in enumerate(mdata):
        # bbox: result.boxes가 있으면 대응 인덱스 사용
#        x1, y1, x2, y2 = result.boxes.xyxy[i].cpu().numpy().astype(int)
#        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

        # 마스크 후처리: 원본 이미지 크기에 맞추기        
#        mask_uint8 = (mask * 255).astype(np.uint8)  # 0~255 스케일
#        mask_resized = cv2.resize(mask_uint8, (W_img, H_img), interpolation=cv2.INTER_NEAREST) # 결과 mask 배열이 원본 img 크기와 다를 수 있으므로 반드시 img 크기와 동일하게 만들어줘야 함
#        bin_mask = (mask_resized > 127).astype(np.uint8)   # # 이진 마스크 생성

        # 마스크에서 외곽선(컨투어) 추출 및 박스 얻기
#        contours, _ = cv2.findContours((bin_mask * 255).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#        cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
               
#        area = int(bin_mask.sum())
#        h_m, w_m = bin_mask.shape
#        print(f'instance {i}: area={area}, relative_area={area/(h_m*w_m):.3f}, contours={len(contours)}')

#    cv2.imshow('contours', img)

#else:
#   print('mask 정보가 없습니다.')

cv2.waitKey()
cv2.destroyAllWindows()