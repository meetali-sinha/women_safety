import torch
import cv2
import math
from ultralytics import YOLO
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import time

# Twilio credentials
account_sid = 'AC9f55656018f238892f050de5845aeb6a'
auth_token = 'c544a4d8e80b96a004fb8f150e2b2af6'
twilio_phone_number = '+12569527929'
to_phone_number = '+919348055251'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Define object classes for detection
classNames = ["abuse", "attack", "chain snatching", "harash", "none", "rape", "women-men-knife-gun"]

# Load the YOLO model
model = YOLO("C:/Users/vamsi/Desktop/women/women-safe-cam/runs/detect/train/weights/best.pt")  # Load YOLOv8 model with pre-trained weights

# Initialize variables
SOS_triggered = False
confidence_threshold = 0.9  # Set confidence threshold to 90%
cooldown_period = 30  # Cooldown period in seconds
last_triggered_time = 0

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set frame width to 1280 pixels
cap.set(4, 720)  # Set frame height to 720 pixels

# Set the display window size
cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Webcam', 1280, 720)

try:
    while True:
        # Read a frame from the camera
        success, img = cap.read()

        if not success:
            break  # Exit loop if the frame is not captured correctly

        # Perform object detection using the YOLO model on the captured frame
        results = model(img, stream=True)

        # Initialize flag to check if any detection exceeds the threshold
        detected = False

        # Iterate through the results of object detection
        for r in results:
            boxes = r.boxes  # Extract bounding boxes for detected objects

            for box in boxes:
                # Extract coordinates of the bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integer values

                # Calculate and print the confidence score of the detection
                confidence = box.conf[0]
                confidence_percentage = math.ceil(confidence * 100) / 100
                print("Confidence --->", confidence_percentage)

                # Only display and draw bounding box if confidence is greater than 90%
                if confidence_percentage > confidence_threshold:
                    detected = True

                    # Draw the bounding box on the frame
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                    # Determine and print the class name of the detected object, handling out-of-bounds error
                    cls = int(box.cls[0])
                    if cls < len(classNames):
                        print("Class name -->", classNames[cls])

                        # Draw text indicating the class name on the frame
                        org = (x1, y1)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        fontScale = 1
                        color = (255, 0, 0)
                        thickness = 2
                        cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
                    else:
                        print("Unknown class ID:", cls)

                    # Check if confidence exceeds the threshold and trigger SOS if not already triggered
                    current_time = time.time()
                    if confidence_percentage >= confidence_threshold and not SOS_triggered:
                        if current_time - last_triggered_time >= cooldown_period:
                            print("Confidence exceeds threshold. Triggering SOS call...")

                            # Generate TwiML instructions
                            response = VoiceResponse()
                            response.say("SOS alert triggered. Immediate assistance needed.")

                            # Send the SOS call with TwiML instructions
                            call = client.calls.create(
                                to=to_phone_number,
                                from_=twilio_phone_number,
                                twiml=response.to_xml()  # Pass the TwiML instructions directly
                            )

                            # Print call SID
                            print(f"SOS call initiated with SID: {call.sid}")

                            # Update last triggered time
                            last_triggered_time = current_time
                            SOS_triggered = True

        # Display the frame with detected objects in a window named "Webcam"
        cv2.imshow('Webcam', img)

        # Check for the 'q' key press to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

finally:
    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()