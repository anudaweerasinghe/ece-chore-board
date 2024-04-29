from hardware_functions.py import setup, onlyOne
import time

setup()
for i in range (20):
    onlyOne(i % 4)
    time.sleep(1)
    
