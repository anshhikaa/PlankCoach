# landmarks of points we want to use in calculate_angle
LEFT_SHOULDER = 11
LEFT_HIP = 23 
LEFT_ANKLE = 27

# function to get these landmarks.x  landmark.y ->coordinates 
def get_points(landmark,index):
    point = landmark[index]
    return (point.x , point.y)
    