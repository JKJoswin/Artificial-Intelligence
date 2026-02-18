import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open the cameras.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 8, minSize = (30, 30))

    for (x, y, w, h) in faces:
        face_roi = frame[x:x+w, y:y+h]
    
    try:
        result = DeepFace.analyze(
            face_roi,
            actions = ['emotion', 'age'],
            enforce_detection = False
        )

        emotion = result[0]['dominant_emotion']
        age = result[0]['age']

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"(Mood:{emotion}, Age:{age})", (x-150, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    except:
        pass

    cv2.imshow("Real-Time Face Emotion Detection - Press 'Q' to Quit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()