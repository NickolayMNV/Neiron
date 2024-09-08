import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier("face.xml")
    results = faces.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)

    for (x, y, w, h) in results:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), thickness=3)

    cv2.imshow("camera", frame)
    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()
















