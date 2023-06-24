
#weight = int(input("Please enter your weight(in kilograms) :- "))

def calories_burnt(speed,weight,time):
    '''Calculate the total calories burnt.'''

    s = speed * 60     # s --> speed in m/min

    if speed <= 8.2767:
        hc = s * 0.1   # hc --> horizontal component
    else:
        hc = s* 0.2
        
    vo2 = 3.5 + hc
    
    MET = vo2 / 3.5

    calories = (MET * 3.5 * weight * time) / 200    # c --> calories burnt

    return calories

