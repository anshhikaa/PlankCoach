from src.analysis.posture import calculate_angle

shoulder = (0,0)
hip = (1,0)
ankle = (2,0)
angle = calculate_angle(shoulder,hip,ankle)

print(angle)