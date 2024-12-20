from mtcnn import MTCNN
import cv2

# Initialize MTCNN detector
detector = MTCNN()

# Open the laptop camera (default camera is index 0)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Detect faces
    results = detector.detect_faces(frame)

    # Draw rectangles around detected faces
    for result in results:
        x, y, width, height = result['box']
        confidence = result['confidence']  # Confidence score for detection
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)
        cv2.putText(frame, f"Conf: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the frame with detected faces
    cv2.imshow('MTCNN Face Detection', frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()
