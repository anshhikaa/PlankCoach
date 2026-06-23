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
### Milestone 2.3 : Smoothening angle values
- Added AngleSmoothener utility using deque 
- Computes moving average instead of relying on single frame prediction
- Produces more stable posture measurements
- Why:
1)  Real-time pose estimation introduces small variations between frames leading to continuously changing result 
2)  Smoothing improves reliability before making posture decisions.

### Milestone 3.1 : Real time plank posture analysis (2D) 
- Added analysis layer using PostureAnalyzer class 
- Defined a range for good form and bad form 
- Angle are computer using 2D vectors 
### Milestone 3.2 : Robust Real-Time Plank Posture Analysis (3D)
#### Why?
The initial approach used 2D landmark coordinates `(x, y)` to calculate the hip angle.
Limitations:
1. The analysis depended heavily on camera placement.
2. Since a 3D body is projected onto a 2D image plane, different real-world poses can appear similar due to projection ambiguity.
3. A slightly different camera angle could change the calculated posture angle.

#### Solution
Moved from 2D geometric analysis to 3D landmark-based analysis.
Using the depth information provided by MediaPipe, the posture angle is calculated using:
- X coordinate
- Y coordinate
- Z coordinate (depth)
This provides a more robust representation of body alignment.
### Milestone 3.3 : Making Angle Calculation More Camera Distance Independent
#### Problem with `pose_landmarks`
MediaPipe's normal pose landmarks provide normalized image coordinates.
The values depend on:
- camera view
- subject position in the frame
- distance from camera
Because of this, the same plank posture could produce slightly different angles when the user moved closer or farther from the camera.
#### Solution
- Switched from pose_landmarks to pose_world_landmarks
#### Why `pose_world_landmarks`?
`pose_world_landmarks` provides an estimated 3D body representation in real-world units.
This allows angle calculation using body coordinates rather than image projection.
Benefits:
- More stable angle calculation
- Less sensitivity to camera distance
- More robust real-time posture detection
Current pipeline:
Camera  
↓
MediaPipe Pose
↓
World Landmarks
↓
3D Hip Angle Calculation
↓
Temporal Smoothing
↓
Rule-Based Posture Classification
↓
Feedback

### Milestone 4.1 : Data Collection for the ML classifier 
- Implemented labeled pose data collection 
- Stored them in a CSV file
- Formed timer logic for countdown and recording 
- Generated balanced dataset (927 samples)
- each sample contains (33 landmarks *3 coordinates + hip_angle) - 100 features + corresponding label
