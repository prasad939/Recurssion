
import cv2
import os

cap = cv2.VideoCapture(0)  # 0 = default webcam
count = 0
save_dir = "frames"
os.makedirs(save_dir, exist_ok=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam - Press 's' to save, 'q' to quit", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        filename = os.path.join(save_dir, f"img_{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
