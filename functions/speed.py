import math

RPM = float(input("RPM value :- ")
shaft_radius = float(input("Radius of motor shaft (in meters) :- "))

def calc_speed(RPM, shaft_radius):
    '''Calculate the speed of the treadmill in meters per second.'''
    speed = (((2* (math.pi) *RPM) / 60) * shaft_radius) # speed(in meters per second) 
    
    return speed
