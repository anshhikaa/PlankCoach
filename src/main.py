import cv2
import mediapipe as mp 
from pose.detector import PoseDetector
from analysis.posture import calculate_angle , PostureAnalyzer 
from pose.landmarks import (LEFT_SHOULDER,LEFT_HIP,LEFT_ANKLE, get_points)
from utils.smoother import AngleSmoother 

def main():

    # starts connection to webcam - SETUP CAPTURE
    camera = cv2.VideoCapture(0)

    # initialize 
    detector = PoseDetector()
    smoother = AngleSmoother()
    analyzer =  PostureAnalyzer()
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    while True:

        # here frame is grabbing video frame , and success to break the loop when camera turned off
        success,frame = camera.read()
        if not success :
            break
        #default feedback for frame without pose 
        result = {
            "feedback" : "NO POSE",
            "color" : (0,0,255)
        }
        smooth_angle = 0

        # stores results
        results = detector.detect(frame)   

        #if results exists then draw the landmarks
        if results.pose_world_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

        #sending the landmarks to the getpoint function along with the index we need to get the coordinates and send it to calculate angle 
            landmarks = results.pose_world_landmarks.landmark
            shoulder = get_points(landmarks,LEFT_SHOULDER)
            hip = get_points(landmarks,LEFT_HIP)
            ankle = get_points(landmarks,LEFT_ANKLE)
            angle = calculate_angle(shoulder,hip,ankle)
        #adding angle smoother to reduce noise from the output 
            smooth_angle = smoother.smooth(angle)
        # feedback -GOOD/BAD
            result = analyzer.analyze(smooth_angle)

        # feedback all the angle(plank) calculated printed in terminal
            # print(result["status"])
            # print(result["feedback"])

        # feedback overlays on the frame
        # text feedback
        cv2.putText(
            frame,
            result["feedback"],
            (50,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            result["color"],
            2
        )
        # angle
        cv2.putText(
            frame,
            f"Angle : {smooth_angle:.2f}",
            (50,100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,255,255),
            2
        )
        
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

