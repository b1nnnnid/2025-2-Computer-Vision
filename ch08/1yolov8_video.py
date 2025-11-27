from ultralytics import YOLO    # pip install ultralytics
import cv2

model = YOLO("yolov8n.pt")  # 사전 학습된 YOLOv8 모델 로드

cap = cv2.VideoCapture('../data/slow_traffic_small.mp4')  # Furious.mp4    # 0,cv.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOv8은 BGR 이미지도 바로 처리 가능
    results = model(frame, verbose=False)
    result = results[0] # 첫번째(단일) 이미지의 예측

    annotated = result.plot()   # bbox/라벨 등이 그려진 주석된 이미지(BGR numpy 배열)를 반환
    cv2.imshow("YOLOv8 Detection", annotated)

    if cv2.waitKey(1)==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()