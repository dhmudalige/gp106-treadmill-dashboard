
#Unit Conversions

###Speed Conversions

def m_per_s_to_mph(speed):
    '''convert meters per second to miles per hour(mph)'''
    return speed * 2.23694 

def m_per_s_to_km_per_hr(speed):
    '''convert meters per second to kilometers per hour'''
    return speed * 3.6

def mph_to_m_per_s(speed):
    '''convert miles per hour(mph) to meters per second'''
    return speed * 2.23694 

def km_per_hr_to_m_per_s(speed):
    '''convert kilometers per hour to meters per second'''
    return speed * 3.6

###Lenght Conversions

def m_to_cm(radius):
    '''convert meters to centimeters'''
    return radius * 100

def m_to_in(radius):
    '''convert meters to inches'''
    return radius / 0.0254

def cm_to_m(radius):
    '''convert centimeters to meters'''
    return radius / 100

def in_to_m(radius):
    '''convert inches to meters'''
    return radius * 0.0254

###Distance Conversions

def m_to_km(distance):
    '''convert meters to kilometers'''
    return distance / 1000

def m_to_miles(distance):
    '''convert meters to miles'''
    return distance / 1609.344

def km_to_m(distance):
    '''convert meters to kilometers'''
    return distance * 1000

def miles_to_m(distance):
    '''convert meters to miles'''
    return distance * 1609.344


###Time Conversions

def s_to_hr(time):
    '''convert seconds to hours'''
    return time / 3600

def s_to_min(time):
    '''convert seconds to minutes'''
    return time / 60

def hr_to_s(time):
    '''convert hours to seconds'''
    return time * 3600

def min_to_sec(time):
    '''convert minutes to seconds'''
    return time * 60

###Mass Conversions

def g_to_kg(weight):
    '''convert grams to kilograms'''
    return weight / 1000

def g_to_lb(weight):
    '''convert grams to pounds'''
    return weight / 453.59237

def kg_to_g(weight):
    '''convert grams to grams'''
    return weight * 1000

def lb_to_g(weight):
    '''convert pounds to grams'''
    return weight * 453.59237
