🚨 Women Safety AI – Real-Time Threat Detection & SOS Alert System
A deep learning–based safety surveillance system that detects abusive or violent gestures against women in real time using YOLOv8, and instantly triggers SOS alerts through Twilio voice calls and Telegram notifications.
🔍 Overview
This project uses a custom-trained YOLO model to identify harmful actions such as attack, abuse, harassment, chain-snatching, etc.
When a threat is detected with high confidence, the system:
•	Captures the alert frame
•	Sends a Telegram alert (image + location + text message)
•	Makes an automated emergency call via Twilio
•	Shows live detection on webcam
This system helps provide real-time protection and reporting in unsafe environments.
________________________________________
🧠 Tech Stack
•	Deep Learning: YOLOv8 (Ultralytics)
•	Computer Vision: OpenCV
•	Programming Language: Python
•	Cloud API Integrations: Twilio (Voice API), Telegram Bot API
•	Libraries: Torch, Requests, Twilio SDK
________________________________________
🚀 Features
✔ Real-time detection via webcam
✔ Custom-trained gesture detection for women safety
✔ Auto-triggered SOS voice call
✔ Sends alert photo, live location, and message to Telegram
✔ 30-second cooldown to avoid repeated alerts
✔ Works entirely locally with internet only for alerting
________________________________________
📁 Project Structure
safecam/
│── t2.py                  # Main file with Telegram + Twilio alert system
│── test.py                # Basic version with only Twilio call alert
│── telegram.py            # Separate script for Telegram alert automation
│── test.ipynb             # Notebook for testing model & detection pipeline
│── runs/                  # YOLO training folder (train, train2, train3)
│── alert_frame.jpg        # Auto-saved snapshot of detected threat
│── README.md              # Project documentation
________________________________________
🔧 Setup & Installation
1️⃣ Clone the project
git clone <your-repo-url>
cd safecam
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install ultralytics opencv-python torch twilio requests
4️⃣ Add your credentials
In t2.py, update:
•	TELEGRAM_BOT_TOKEN
•	TELEGRAM_CHAT_ID
•	Twilio: account_sid, auth_token, twilio_phone_number, to_phone_number
•	YOLO weights path
________________________________________
▶️ Running the System
python t2.py
Your webcam will open → model will detect → if threat detected → SOS alert triggers automatically.
Press Q to exit webcam.
________________________________________
📞 Emergency Alert Workflow
1.	Model detects a violent/abusive gesture
2.	Saves alert_frame.jpg
3.	Sends it to your Telegram bot
4.	Sends static GPS location
5.	Sends text “SOS Alert”
6.	Twilio makes a phone call to the saved number
________________________________________
👥 Team Contribution
•	Dataset creation (gesture collection, annotation)
•	Model training with YOLOv8
•	Backend integration (Twilio + Telegram APIs)
•	Real-time detection pipeline
•	Testing with live human actors (M/F teammate)

