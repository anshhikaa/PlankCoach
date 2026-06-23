import time
import cv2
import csv
from analysis.posture import calculate_angle
from pose.detector import PoseDetector
from pose.landmarks import (LEFT_SHOULDER,LEFT_HIP,LEFT_ANKLE, get_points)
from utils.smoother import AngleSmoother
import mediapipe as mp
cam = cv2.VideoCapture(0)
detector = PoseDetector()
smoothener = AngleSmoother();
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
current_label =None
start_time = None
recording_start = None 
collecting = False
waiting = False
elapsed = 0

while True :
    #IDLE----
    success ,frame = cam.read()
    
    if not success:
        break
    key = cv2.waitKey(1)
    # check keyboard input + WAITING--- 
    if key == ord("g") and not waiting and not collecting:
        current_label = "GOOD"
        #as soon as key pressed countdown to record features start
        start_time = time.time()
        waiting = True
        print("recording starts in 20 secs for good posture ")
        
    elif key == ord("h") and not waiting and not collecting:
        current_label = "HIP_HIGH"
        start_time = time.time()
        waiting = True
        print("recording starts in 20 secs for high hip")
        
    elif key == ord("s") and not waiting and not collecting:
        current_label = "HIP_SAG"
        start_time = time.time()
        waiting = True
        print("recording starts in 20 secs for hip sag ")
        
    elif key == ord("q"):
        break
    # timer logic to start the rEcording of angle after 20 seconds
    if waiting:
        countdown = time.time()-start_time 
        if countdown > 20 :
            collecting = True
            waiting = False
            print("recording starts ")
            recording_start = time.time()
    # RECORDING-----
    #Countdown started     
    # now the collector knows for what label is it collecting the data for
    result = detector.detect(frame)
    
    if collecting:
            elapsed = time.time() - recording_start
            if elapsed > 20: 
                collecting  = False
                print("recording stopped") 
    # extract landmarks and angle -> features extraction
    if result.pose_world_landmarks:
        #draw landmarks
        mp_drawing.draw_landmarks(
                frame,
                result.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )
        landmarks = result.pose_world_landmarks.landmark
        curr_sample_row=[]
        for landmark in landmarks:
            curr_sample_row.extend([landmark.x,landmark.y,landmark.z])
        
        shoulder = get_points(landmarks,LEFT_SHOULDER)
        hip = get_points(landmarks,LEFT_HIP)
        ankle = get_points(landmarks,LEFT_ANKLE)
        angle = calculate_angle(shoulder,hip,ankle)
        smooth_angle = smoothener.smooth(angle)
        if collecting and current_label is not None :
            curr_sample_row.append(smooth_angle)
            curr_sample_row.append(current_label)
            # saving the curr-row extracted from one frame for a curr label into csv dataset file
            with open("plank_dataset.csv",mode="a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(curr_sample_row) 
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
        "Plank Coach Data collector",
        frame
    )    
cam.release()
cv2.destroyAllWindows()       

                    
            


             


