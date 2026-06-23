import mediapipe as mp 

# create poseDetector class
class PoseDetector :
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
    """the main-detect function that catches the frame captured in main.py
     and sends those frame into the pre-trained model(BlazePose) which processes the frame and 
     sends the outpit(all 33 landmarks)"""
    def detect(self,frame):
        results = self.pose.process(frame)
        return results

