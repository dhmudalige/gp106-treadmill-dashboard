
from datetime import datetime
#from time import time

#counter = time()
mytimestamp = 66600
total_seconds = 0

print("Current date and time :- " , datetime.now())
def timer():

    try:
        def count():
            
            #global counter
            global mytimestamp
            global total_seconds

            while True:
                # To manage the intial delay. 
                if mytimestamp == 66600:
                    display="Starting..."
                else:
                    tt = datetime.fromtimestamp(mytimestamp)
                    display = tt.strftime("%H:%M:%S")
                    total_seconds = int(tt.hour)*3600 + int(tt.minute)*60 + int(tt.second)
                                
                print(display)

                #counter += 1
                mytimestamp += 1
                

        # Triggering the start of the counter. 
        count()
        
    except KeyboardInterrupt:
        return total_seconds
        
    

