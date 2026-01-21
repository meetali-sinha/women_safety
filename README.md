# WOMEN SAFETY AI – REAL TIME THREAT DETECTION AND ALERT SYSTEM

---

## INTRODUCTION

Women safety is a critical concern in modern society, especially in public and semi-public environments. The increasing number of harassment and violence cases highlights the need for intelligent, automated safety solutions. This project presents a deep learning based real-time women safety system that detects abusive and violent gestures using a live camera feed and automatically triggers emergency alerts.

The system leverages computer vision and deep learning to identify unsafe situations and instantly notify concerned authorities or guardians through phone calls and messaging services.

---

## PROJECT OBJECTIVE

* To detect violent or abusive gestures against women in real time
* To reduce response time during emergency situations
* To provide automated alerts without manual intervention
* To assist women using AI-powered surveillance and alerting

---

## SYSTEM OVERVIEW

The system continuously monitors a live video stream using a webcam. A custom-trained YOLOv8 deep learning model processes each frame and identifies predefined unsafe actions such as attack, abuse, harassment, or chain snatching.

When a threat is detected above a confidence threshold:

* An alert image is captured
* A voice call is triggered using Twilio
* A Telegram bot sends the alert image, location, and text message
* The system enters a cooldown period to avoid repeated alerts

---

## KEY FEATURES

* Real-time detection using webcam
* Custom deep learning model trained on unsafe gesture dataset
* Automatic SOS voice call alert
* Telegram alerts with image, text, and location
* Cooldown mechanism to prevent alert spamming
* Fully automated pipeline with no manual trigger required

---

## TECH STACK

* Programming Language

  * Python

* Deep Learning and Computer Vision

  * YOLOv8
  * PyTorch
  * OpenCV

* Alert and Communication APIs

  * Twilio Voice API
  * Telegram Bot API

* Supporting Libraries

  * Requests
  * Math
  * Time

* Tools

  * VS Code
  * GitHub
  * Virtual Environment (venv)

---

## PROJECT STRUCTURE

safecam/

* t2.py                    - Main application file
* telegram.py              - Telegram alert testing script
* test.py                  - YOLO and Twilio test script
* test.ipynb               - Notebook for model testing
* runs/

  * detect/

    * train/
    * train2/
    * train3/
* venv/                    - Python virtual environment
* alert_frame.jpg          - Captured alert image
* requirements.txt         - Project dependencies
* README.md                - Project documentation

---

## DATASET DETAILS

* Dataset created manually by the team
* Includes images and video frames of unsafe and abusive gestures
* Classes include:

  * abuse
  * attack
  * harassment
  * chain snatching
  * weapon threat
* Dataset was annotated and used to fine-tune YOLOv8

---

## WORKING METHODOLOGY

* Initialize webcam and load trained YOLOv8 model
* Capture frames continuously
* Perform object detection on each frame
* Check confidence score against threshold
* If unsafe gesture detected:

  * Save alert image
  * Send Telegram alert
  * Send GPS location
  * Trigger Twilio voice call
* Apply cooldown logic
* Continue monitoring until manually stopped

---

## SETUP AND INSTALLATION

Step 1 - Clone the repository

* git clone <repository_url>
* cd safecam

Step 2 - Create virtual environment

* python -m venv venv

Step 3 - Activate virtual environment (Windows CMD)

* venv\Scripts\activate.bat

Step 4 - Install dependencies

* pip install ultralytics
* pip install opencv-python
* pip install torch
* pip install twilio
* pip install requests

---

## CONFIGURATION

Before running the project, update the following in t2.py:

* Telegram bot token
* Telegram chat ID
* Twilio account SID
* Twilio auth token
* Twilio phone number
* Alert receiver phone number
* YOLO model weights path

---

## HOW TO RUN THE PROJECT

* Open the project folder in VS Code
* Ensure the virtual environment is activated
* Run the main file:

  * python t2.py
* Webcam will start automatically
* Press 'q' to stop the system

---

## ALERT FLOW

* Unsafe gesture detected
* Alert image captured
* Telegram message sent
* GPS location shared
* Voice call triggered
* System enters cooldown period

---

## DEPLOYMENT DETAILS

* The system runs locally on a PC or laptop
* Requires internet connection for Telegram and Twilio alerts
* Can be deployed on CCTV-enabled systems
* Can be extended to mobile or cloud platforms
* Suitable for colleges, public areas, and safety monitoring setups

---

## LIMITATIONS

* Depends on camera quality and lighting conditions
* Internet connection required for alerts
* Static GPS location (can be upgraded to dynamic tracking)
* Model accuracy depends on dataset quality

---

## FUTURE ENHANCEMENTS

* Dynamic GPS tracking
* Mobile application integration
* Web dashboard for analytics
* Panic button feature
* Cloud-based deployment
* Improved dataset and multi-camera support

---

## CONCLUSION

This project demonstrates the practical application of deep learning and computer vision for real-world safety problems. By combining YOLOv8 with automated alert systems, the Women Safety AI project provides a reliable and intelligent solution to detect and respond to unsafe situations in real time.
