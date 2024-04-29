from hardware_functions import *
import time

setup()
for i in range (20):
    onlyOne(i % 4)
    time.sleep(1)
    
