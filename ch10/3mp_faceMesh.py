import cv2 
import mediapipe as mp

mp_mesh = mp.solutions.face_mesh        # Mediapipe Face Mesh 초기화
mp_drawing = mp.solutions.drawing_utils       # Import drawing_utils and drawing_styles.
mp_styles = mp.solutions.drawing_styles

mesh = mp_mesh.FaceMesh(max_num_faces=2, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) # 얼굴검출 + mesh : 최대 2개

cap = cv2.VideoCapture('../data/face2.mp4')

while True :
    ret, frame = cap.read()
    if not ret :
      print('프레임 획득에 실패하여 루프를 나갑니다.')
      break
    
    res = mesh.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)) # Mediapipe는 RGB 이미지 변환해야 함

    if res.multi_face_landmarks : # 검출된 얼굴이 있다면

        for landmarks in res.multi_face_landmarks : # 모든 검출된 얼굴에 대해
            print(landmarks)
            mp_drawing.draw_landmarks(image=frame, landmark_list=landmarks, connections=mp_mesh.FACEMESH_TESSELATION,
                                      landmark_drawing_spec=None,
                                      connection_drawing_spec=mp_styles.get_default_face_mesh_tesselation_style())
            mp_drawing.draw_landmarks(image=frame, landmark_list=landmarks, connections=mp_mesh.FACEMESH_CONTOURS,
                                      landmark_drawing_spec=None,
                                      connection_drawing_spec=mp_styles.get_default_face_mesh_contours_style())
            mp_drawing.draw_landmarks(image=frame, landmark_list=landmarks, connections=mp_mesh.FACEMESH_IRISES,
                                      landmark_drawing_spec=None,
                                      connection_drawing_spec=mp_styles.get_default_face_mesh_iris_connections_style())
        
    cv2.imshow('MediaPipe Face Mesh', cv2.flip(frame,1))		# 좌우반전
    if cv2.waitKey(5)==ord('q'):
      break

cap.release()
cv2.destroyAllWindows()