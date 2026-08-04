import cv2

# Read the captured video
video = cv2.VideoCapture("C:/Users/saimo/OneDrive/Videos/video.mp4")

# Check if video is opened
if not video.isOpened():
    print("Error: Cannot open video.")
else:
    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Resize the frame (optional)
        frame = cv2.resize(frame, (800, 600))

        # Display the video
        cv2.imshow("Video", frame)

        # Press 's' for slow motion, 'f' for fast motion, 'q' to quit
        key = cv2.waitKey(30) & 0xFF

        if key == ord('s'):
            cv2.waitKey(100)   # Slow motion
        elif key == ord('f'):
            cv2.waitKey(5)     # Fast motion
        elif key == ord('q'):
            break

# Release video and close windows
video.release()
cv2.destroyAllWindows()
