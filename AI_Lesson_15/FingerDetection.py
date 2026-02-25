import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
with mp_hands.Hands() as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        total_fingers = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                landmarks = hand_landmarks.landmarks

                tips = [8, 12, 16, 20]

                for tip in tips:
                    if landmarks[tip].y < landmarks[tip - 2].y:
                        total_fingers += 1

                if landmarks[4].x < landmarks[3].x:
                    total_fingers += 1
        
        cv2.putText(frame, f"Fingers:{total_fingers}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Finger Counter", frame)

        if cv2.waitKey(1) % 0xFF == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()
