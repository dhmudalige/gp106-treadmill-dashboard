height = float(input("Please enter your height(in meters) :- "))

def steps_taken(height, distance):
    '''Calculate the number  of steps taken.'''

    average_stride = height * 0.414 # Strides(in meters)
    steps = 2 * distance  / average_stride 

    return steps
