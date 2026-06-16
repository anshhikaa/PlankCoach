# PlankCoach

AI-powered real-time plank posture correction system using computer vision and pose estimation to analyze body alignment and provide live feedback.

# Motivation 

While doing exercises like planks, maintaining the correct form is often more important than increasing duration. Without a trainer, users may unknowingly perform planks with incorrect hip position, back alignment, or neck posture.
This project aims to provide an accessible AI-based solution that acts as a virtual posture assistant .

## Tech Stack

- Python
- OpenCV
- MediaPipe Pose Estimation - using 0.10.11 version
- NumPy
- Computer Vision
- Machine Learning

## How It Works

Camera Input
      ↓
Pose Detection Model
      ↓
Body Landmark Extraction
      ↓
Posture Analysis
      ↓
Form Score + Real-time Feedback
      ↓
Timer Tracking

## Project Status

Currently under development
The current focus is implementing real-time pose detection, posture evaluation rules, and an interactive feedback system.

## Current Progress

### Milestone 1: Pose Detection Pipeline 
Implemented real-time human pose detection using OpenCV and MediaPipe.
The system:
- Captures webcam frames using opencv
- Processes frames using a pose estimation model (BlazePose)
- Extracts human body landmarks
- Displays a real-time skeleton overlay

### Milestone 2.1: Posture analysis
Implemented 
- Landmark based geometry analysis
- Converted extracted landmarks to vector for angle calculation 
- Vector based angle calculation
### Milestone 2.2 : Integrated real-time pose landmarks with posture analysis
The system now :
- extract human pose landmarks using mediapipe 
- indentifies shoulder,hip and ankle coordinates
- calculates real-time hip joint angle
- responds to body movement changes

