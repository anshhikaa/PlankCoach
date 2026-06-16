from collections import deque

class AngleSmoother :

    def __init__(self,window_size =5):
        self.values = deque(maxlen=window_size)

    def smooth(self,angle):
        self.values.append(angle)
        total = sum(self.values)
        average = total / len(self.values)
        return average
