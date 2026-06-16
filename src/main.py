import cv2
import mediapipe as mp 
from pose.detector import PoseDetector
from analysis.posture import calculate_angle
from pose.landmarks import (LEFT_SHOULDER,LEFT_HIP,LEFT_ANKLE, get_points)
from utils.smoother import AngleSmoother 

def main():

    # starts connection to webcam - SETUP CAPTURE
    camera = cv2.VideoCapture(0)
    # initialize 
    detector = PoseDetector()
    smoother = AngleSmoother()
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    while True:

        # here frame is grabbing video frame , and success to break the loop when camera turned off
        success,frame = camera.read()
        if not success :
            break
        
        # stores results
        results = detector.detect(frame)   

        #if results exists then draw the landmarks
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )
        #sending the landmarks to the getpoint function along with the index we need to get the coordinates and send it to calculate angle 
            landmarks = results.pose_landmarks.landmark
            shoulder = get_points(landmarks,LEFT_SHOULDER)
            hip = get_points(landmarks,LEFT_HIP)
            ankle = get_points(landmarks,LEFT_ANKLE)
            angle = calculate_angle(shoulder,hip,ankle)
        #adding angle smoother to reduce noise from the output 
            smooth_angle = smoother.smooth(angle)
            print(smooth_angle)

        
        # displays image in new window 
        cv2.imshow(
            "AI Plank Coach",
            frame
        )

        # pauses window 
        if cv2.waitKey(1) == ord("q"):
            break

    # as soon as out of loop turn off camera & close video files   
    camera.release()
    # close all window image
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

