# Hand Gesture Cursor Control using MediaPipe

## Overview

This project implements a hand gesture recognition system that allows users to control their computer cursor using hand movements. By leveraging the MediaPipe library for hand tracking, the system detects key points on the user's hand and translates those movements into cursor movements and mouse actions (clicking and right-clicking). This technology can be particularly useful for accessibility, gaming, or simply enhancing user interaction.

## Table of Contents

- [Hand Gesture Cursor Control using MediaPipe](#hand-gesture-cursor-control-using-mediapipe)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [Implementation Details](#implementation-details)
  - [Key Steps in Implementation](#key-steps-in-implementation)
  - [Gesture Controls](#gesture-controls)
  - [Future Enhancements](#future-enhancements)
  - [Conclusion](#conclusion)

## Usage
Once the program is running, it will activate your webcam to track hand movements. You can control the cursor on your screen using your hand gestures as specified in the gesture controls section below.

To exit the program, simply press the 'q' key.

## Implementation Details
This project uses the following key components:

- MediaPipe: A cross-platform framework developed by Google for building multimodal applied machine learning pipelines. MediaPipe provides a robust hand tracking model that identifies 21 key landmarks on the hand.

- OpenCV: A library used for computer vision tasks. It captures video input from the webcam and processes frames in real time.

- PyAutoGUI: A Python library used for programmatically controlling the mouse and keyboard. It allows for mouse movement and clicking based on the hand's position.

## Key Steps in Implementation
- Video Capture: The program captures video frames from the webcam using OpenCV.

- Hand Tracking: MediaPipe processes each frame to detect hands and identify landmarks corresponding to various finger joints and tips.

- Cursor Control: The position of the cursor is calculated based on the average position of specific landmarks on the palm. The screen coordinates are adjusted according to the dimensions of the screen.

- Mouse Actions: The program detects gestures such as clicking and right-clicking based on the distance between the thumb and index finger.

## Gesture Controls
Cursor Movement: Move your hand within the camera frame to control the cursor's position on the screen. The sensitivity of the cursor movement can be adjusted in the code.

Left Click: Bring your thumb and index finger close together to perform a left click.

Right Click: Bring your thumb and middle finger close together to perform a right click.

## Future Enhancements
**This project can be further improved by:**

- Implementing additional gestures for more advanced mouse controls (e.g., scrolling, dragging).
- Enhancing hand detection accuracy and speed under varying lighting conditions.
- Integrating voice commands to provide a hands-free experience.

## Conclusion
This hand gesture-based cursor control system is a step towards creating more intuitive and accessible interfaces. With the power of MediaPipe, users can interact with their devices in a natural and innovative way.