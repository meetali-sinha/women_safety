import torch
import cv2
import math
from ultralytics import YOLO
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import time
import requests  # For Telegram API

# ----------------- Twilio Credentials -----------------
account_sid = 'AC9f55656018f238892f050de5845aeb6a'
auth_token = 'c544a4d8e80b96a004fb8f150e2b2af6'
twilio_phone_number = '+13157109408'
to_phone_number = '+919348055251'
client = Client(account_sid, auth_token)

# ----------------- Telegram Bot Credentials -----------------
TELEGRAM_BOT_TOKEN = "7567998570:AAFgBOlNuAEjpDQ5Cw_lOWkW48ly1_2AGEs"  # Replace this
TELEGRAM_CHAT_ID = '93307802'               # Replace this

# Static GPS Location (You can replace this with dynamic GPS later)
latitude = 17.3850
longitude = 78.4867

# ----------------- YOLO & App Settings -----------------
classNames = ["abuse", "attack", "chain snatching", "harash", "none", "rape", "women-men-knife-gun"]
model = YOLO("C:/Users/vamsi/Desktop/women/women-safe-cam/runs/detect/train/weights/best.pt")
SOS_triggered = False
confidence_threshold = 0.9
cooldown_period = 30  # seconds
last_triggered_time = 0

# ----------------- Open Webcam -----------------
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Webcam', 1280, 720)

try:
    while True:
        success, img = cap.read()
        if not success:
            break

        results = model(img, stream=True)
        detected = False

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = box.conf[0]
                confidence_percentage = math.ceil(confidence * 100) / 100
                print("Confidence --->", confidence_percentage)

                if confidence_percentage > confidence_threshold:
                    detected = True
                    cls = int(box.cls[0])
                    class_name = classNames[cls] if cls < len(classNames) else "unknown"

                    # Draw bounding box
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                    cv2.putText(img, class_name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                    current_time = time.time()
                    if not SOS_triggered and (current_time - last_triggered_time >= cooldown_period):
                        print("🚨 Triggering SOS alert...")

                        # 1. Save image
                        image_path = "alert_frame.jpg"
                        cv2.imwrite(image_path, img)

                        # 2. Send voice call via Twilio
                        response = VoiceResponse()
                        response.say("SOS alert triggered. Immediate assistance needed.")
                        call = client.calls.create(
                            to=to_phone_number,
                            from_=twilio_phone_number,
                            twiml=response.to_xml()
                        )
                        print(f"Twilio Call SID: {call.sid}")

                        # 3. Send image to Telegram
                        with open(image_path, "rb") as photo:
                            photo_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
                            requests.post(photo_url, data={"chat_id": TELEGRAM_CHAT_ID}, files={"photo": photo})

                        # 4. Send location to Telegram
                        location_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendLocation"
                        requests.post(location_url, data={
                            "chat_id": TELEGRAM_CHAT_ID,
                            "latitude": latitude,
                            "longitude": longitude
                        })

                        # 5. Optionally, send text message to Telegram
                        text_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                        message = f"SOS Alert: '{class_name}' detected with {confidence_percentage*100:.1f}% confidence."
                        requests.post(text_url, data={
                            "chat_id": TELEGRAM_CHAT_ID,
                            "text": message
                        })

                        # Update state
                        last_triggered_time = current_time
                        SOS_triggered = True

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
