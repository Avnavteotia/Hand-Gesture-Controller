import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()
prev_x = None  # Previous hand position for smoother movement

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    image = cv2.flip(image, 1)  # Mirror effect
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_image)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get important points
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            index_x = int(index_tip.x * screen_width)  # Convert to screen coordinates
            index_y = int(index_tip.y * screen_height)
            wrist_x = int(wrist.x * screen_width)

            # Jump & Roll Detection
            if index_y < (screen_height // 3):  # If hand is high -> Jump
                print("Jump")
                pyautogui.press("up")

            elif index_y > (2 * screen_height // 3):  # If hand is low -> Roll
                print("Roll")
                pyautogui.press("down")

            # Left-Right Movement (Based on Hand Shift)
            if prev_x is not None:
                if index_x < prev_x - 50:  # Hand moved left
                    print("Move Left")
                    pyautogui.press("left")
                elif index_x > prev_x + 50:  # Hand moved right
                    print("Move Right")
                    pyautogui.press("right")

            prev_x = index_x  # Update previous hand position

    cv2.imshow("Hand Tracking", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
