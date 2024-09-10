# FER
This project is a real-time face emotion recognition system using a webcam feed. It utilizes __OpenCV__ data for face detection and __DeepFace__ for analyzing emotions. The output includes displaying the dominant emotion on the live camera feed and drawing a bounding box around faces.

__Develop for course Image Processing(32479)__

## Features
- The program uses a pre-trained Haar Cascade Classifier `(haarcascade_frontalface_default.xml)` from OpenCV to detect faces.
- Emotion analysis using the DeepFace library.
- Displays the dominant emotion and draws bounding boxes around faces.

## How to run
To start the emotion recognition program, run the following command:
```zsh
python FRE.py
```
It will launch the webcam and start detecting faces.

To quit:

Press `q`  to quit the application.

