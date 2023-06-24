import math


class Treadmill(object):
    '''Class for Treadmill Operations'''
        
    def change_RPM(self,RPM):
        '''Change the RPM value of the treadmill motor.'''
        self.rpm = RPM

    def change_r(self,shaft_radius):
        '''Change the value of the shaft radius of the treadmill motor.'''
        self.r = shaft_radius

    def start(self):
        
        ###Calculate the speed of the treadmill in meters per second
        self.speed = (((2* (math.pi) * self.rpm) / 60) * self.r) # speed(in meters per second)        

        ###Calculate the distance walked or ran in meters        
        self.distance = self.speed * self.time # distance(in meters)

        ###Calculate the number  of steps taken
        average_stride = self.H * 0.414 # Strides(in meters)
        self.steps = 2 * self.distance  / average_stride 

        ###Calculate the total calories burnt
        s = self.speed * 60     # s --> speed in m/min

        if self.speed <= 3.7 * 0.44704:
            hc = s * 0.1   # hc --> horizontal component
        else:
            hc = s* 0.2
            
        vo2 = 3.5 + hc        
        MET = vo2 / 3.5
        self.calories = (MET * 3.5 * self.W * self.time / 60) / 200     # c --> calories burnt


class TreadmillParameters(Treadmill):
    '''Class for Instances in Treadmill Operations'''

    def __init__(self, RPM, shaft_radius):
        self.rpm = RPM
        self.r = shaft_radius

    def get_user(self, user_id, weight, height):
        self.id = user_id
        self.W = weight
        self.H = height
        
    def get_time(self, time):
        self.time = time * 60
