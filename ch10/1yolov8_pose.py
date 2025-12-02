from ultralytics import YOLO
import cv2

pose_model = YOLO("yolov8n-pose.pt")    # 사전 학습된 YOLOv8 포즈 모델 로드

#cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap = cv2.VideoCapture('../data/aerobics.mp4')  #'face2.mp4')

while True :
    ret, frame = cap.read()
    if not ret :
        break

    # YOLOv8은 BGR 이미지도 바로 처리 가능
    results = pose_model(frame, verbose=False)
    result = results[0] # 첫번째(단일) 이미지의 예측

    annotated = result.plot()   # 관절(keypoints) 그려진 이미지
    cv2.imshow("YOLOv8 Pose", annotated)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()