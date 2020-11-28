import random
import time
from datetime import datetime, timedelta

def generate_race_data(start_time, 
                       lap_time_driver1, 
                       lap_time_driver2):

    time_difference = (datetime.now() - start_time).total_seconds()
    
    if int(time_difference)%lap_time_driver1 == 0:
        signal_driver1 = 35 + random.uniform(-2.0, 2.0)
    else:
        signal_driver1 = 350 + random.uniform(-5.0, +5.0)

    if int(time_difference)%lap_time_driver2 == 0:
        signal_driver2 = 35 + random.uniform(-2.0, 2.0)
    else:
        signal_driver2 = 350 + random.uniform(-5.0, +5.0)

    time.sleep(0.2)

    return signal_driver1, signal_driver2

