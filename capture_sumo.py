import traci
import sumolib
import time
import os

SUMO_CFG = r"E:\traffic_rl\sumo\intersection.sumocfg"
OUTPUT = "logs/sumo_screenshot.png"

os.makedirs("logs", exist_ok=True)

sumoBinary = sumolib.checkBinary("sumo-gui")

traci.start([
    sumoBinary,
    "-c", SUMO_CFG,
    "--start"
])

time.sleep(3)  # allow GUI to load

# Capture screenshot
traci.gui.screenshot(
    viewID="View #0",
    filename=OUTPUT,
    width=1024,
    height=768
)

print("✅ Screenshot saved:", OUTPUT)

time.sleep(1)
traci.close()