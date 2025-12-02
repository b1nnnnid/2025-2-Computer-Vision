import cv2
import mediapipe as mp

mp_hand=mp.solutions.hands          # Mediapipe Hands 초기화
mp_drawing=mp.solutions.drawing_utils       # Import drawing_utils and drawing_styles.
mp_styles=mp.solutions.drawing_styles

hand=mp_hand.Hands(max_num_hands=2, static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)   # 손 검출 : 최대 2개
# static_image_mode : True는 이미지, False는 비디오

cap = cv2.VideoCapture('../data/piano_hands.mp4')

while True:
    ret,frame=cap.read()
    if not ret:
      print('프레임 획득에 실패하여 루프를 나갑니다.')
      break
    
    res=hand.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    
    if res.multi_hand_landmarks:
        print(len(res.multi_hand_landmarks))

        for landmarks in res.multi_hand_landmarks:
            print(landmarks)

            mp_drawing.draw_landmarks(frame, landmarks, mp_hand.HAND_CONNECTIONS,
                                      mp_styles.get_default_hand_landmarks_style(),
                                      mp_styles.get_default_hand_connections_style())

    cv2.imshow('MediaPipe Hands',cv2.flip(frame,1))	 # 1은 좌우 반전(대칭), 0은 상하 반전, -1은 상하&좌우 반전
    if cv2.waitKey(5)==ord('q'):
      break

cap.release()
cv2.destroyAllWindows()