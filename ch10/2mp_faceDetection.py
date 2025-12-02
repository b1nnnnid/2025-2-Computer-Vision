import cv2
import mediapipe as mp  # 설치 : pip install mediapipe
# Mediapipe + TensorFlow + Python 3.11 조합에서 발생하는 공식적인 호환성 문제 : tensorflow 제거

mp_face_detection = mp.solutions.face_detection   # Mediapipe Face Detection 초기화
mp_drawing = mp.solutions.drawing_utils   # Import drawing_utils.

face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)   # 얼굴검출 : model_selection=0은 근거리(2m 이내), 1은 원거리(2m~5m)

cap = cv2.VideoCapture('../data/face2.mp4')

while True :
    ret, frame = cap.read()
    if not ret :
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    res = face_detection.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))   # Mediapipe는 RGB 이미지 변환해야 함
    
    if res.detections :     # 검출된 얼굴이 있다면
        for detection in res.detections :   # 모든 검출된 얼굴에 대해
            mp_drawing.draw_detection(frame, detection) # frame에 랜드마크 그리기
            
    cv2.imshow('MediaPipe Face Detection from video',  cv2.flip(frame,1))		# 좌우반전
    if cv2.waitKey(5)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()