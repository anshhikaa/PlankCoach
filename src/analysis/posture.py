import math

# function to do the analysis of the landmarks obtained from detector.py 
# function(landmarks) return hip angle
def calculate_angle(a,b,c):
    #convert points to vector a:shoulder , b:hip , c : ankle
    # hip-shoulder = ax-bx,ay-by destination-source
    ba = (a[0]-b[0],a[1]-b[1])
    # hip-ankle = cx-bx,cy-by
    bc = (c[0]-b[0],c[1]-b[1])

    #dot product a.b = ax*bx + ay*by
    # ba.bc 
    dot_product = (ba[0]*bc[0]+ba[1]*bc[1])

    #magnitude root(x^2 + y^2)
    # ba and bc 
    magnitude_ba = math.sqrt(ba[0]**2 + ba[1]**2)
    magnitude_bc = math.sqrt(bc[0]**2 + bc[1]**2)

    # calculate cos angle cos 0 = a.b/|a||b|
    cos_angle = dot_product/(magnitude_ba*magnitude_bc)
    cos_angle = max(-1,min(1,cos_angle))
    #calculate angle 0 = cos-1(val) in degrees
    inverse_cos = math.acos(cos_angle) #->radian return
    angle = math.degrees(inverse_cos)  #convert degreees

    return angle


