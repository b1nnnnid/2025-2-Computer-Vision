from ultralytics import YOLO    
import cv2
import sys

model = YOLO("yolov8n.pt")  # 사전 학습된 YOLOv8 모델 로드 (작은 모델 yolov8n), 자동 다운로드

img = cv2.imread('../data/busy_street.jpg')   # london_street.png
if img is None : 
    sys.exit('파일이 없습니다.')

# YOLOv8은 BGR 이미지도 바로 처리 가능
results = model(img, verbose=False)
result = results[0] # 첫번째(단일) 이미지의 예측

annotated = result.plot()   # bbox/라벨 등이 그려진 주석된 결과 이미지(BGR numpy 배열)를 반환
cv2.imshow("YOLOv8 Detection", annotated)

# result.boxes : Boxes 객체 — 바운딩박스 정보(.xyxy, .xywh), 신뢰도(.conf), 클래스 id(.cls) 등
# result.boxes.xyxy 등은 PyTorch 텐서이므로 .cpu().numpy()로 numpy 변환 필요
# 박스 정보 확인 및 numpy 변환
#if result.boxes is not None:
#    boxes = result.boxes.xyxy.cpu().numpy().astype(int)
#    confs  = result.boxes.conf.cpu().numpy()  # (N,)
#    cls_ids = result.boxes.cls.cpu().numpy().astype(int)  # (N,)
#    for (x1,y1,x2,y2), c, cid in zip(boxes, confs, cls_ids):
#        print(result.names[cid], c, (x1,y1,x2,y2))
        #if (result.names[cid]=="person") :
#        cv2.rectangle(img, (x1,y1), (x2,y2), (255, 255, 0), 2)
#    cv2.imshow('boxes', img)

cv2.waitKey()
cv2.destroyAllWindows()