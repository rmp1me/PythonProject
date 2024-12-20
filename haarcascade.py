# import cv2
#
# # Load the pre-trained Haar Cascade classifier for face detection
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
# # Open the laptop camera (default camera is index 0)
# cap = cv2.VideoCapture(0)
#
# # Check if the camera is opened successfully
# if not cap.isOpened():
#     print("Error: Could not open camera.")
#     exit()
#
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Could not read frame.")
#         break
#
#     # Convert frame to grayscale
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Detect faces in the frame
#     faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#     print(faces)
#
#     # Draw rectangles around detected faces
#     for (x, y, w, h) in faces:
#         print("-----------------")
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#     # Display the frame with detected faces
#     cv2.imshow('Real-Time Face Detection', frame)
#
#     # Break the loop on pressing 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the camera and close the windows
# cap.release()
# cv2.destroyAllWindows()
import cv2
import time

# Load the pre-trained Haar Cascade classifier for face detection
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Check if the cascade file is loaded
if face_cascade.empty():
    print("Error: Could not load Haar cascade classifier.")
    exit()

# Open the laptop camera (default camera is index 0)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Get the starting time for FPS calculation
start_time = time.time()
frame_count = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to improve contrast
    gray_frame = cv2.equalizeHist(gray_frame)

    # Apply Gaussian blur to reduce noise
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.05,
        minNeighbors=8,
        minSize=(30, 30)
    )

    # Draw rectangles around detected faces and log coordinates
    for (x, y, w, h) in faces:
        print(f"Face detected at [X: {x}, Y: {y}, Width: {w}, Height: {h}]")
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Calculate and display FPS
    frame_count += 1
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display the frame with detected faces
    cv2.imshow('Real-Time Face Detection', frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()
