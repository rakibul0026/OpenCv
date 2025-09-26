import cv2

# 0 means default webcam (you can use 1,2... for external cameras)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # ret=True if frame is successfully captured
    if not ret:
        print("❌ Error: Failed to capture video")
        break

    cv2.imshow("Webcam", frame)

    # Press 'q' to stop the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Video Off ✅")
        break

cap.release()          # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows
