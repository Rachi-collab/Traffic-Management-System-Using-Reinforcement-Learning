import traci
import time
import os

os.makedirs("logs", exist_ok=True)

while True:
    if traci.isLoaded():
        traci.gui.screenshot("View #0", "logs/sumo_live.png")
    time.sleep(1)