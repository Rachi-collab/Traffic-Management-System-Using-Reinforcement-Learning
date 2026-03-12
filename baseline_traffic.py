import traci
import sumolib
import csv
import os

SUMO_CFG = "sumo/intersection.sumocfg"
TLS_ID = "C"
MAX_STEPS = 1000

os.makedirs("logs", exist_ok=True)

sumo_binary = sumolib.checkBinary("sumo")

traci.start([
    sumo_binary,
    "-c", SUMO_CFG,
    "--start",
    "--quit-on-end",
    "--no-step-log", "true"
])

queue_log = []

for step in range(MAX_STEPS):
    traci.simulationStep()

    edges = ["N2C", "S2C", "E2C", "W2C"]
    total_queue = 0
    for e in edges:
        for l in range(2):
            total_queue += traci.lane.getLastStepHaltingNumber(f"{e}_{l}")

    queue_log.append((step, total_queue))

traci.close()

with open("logs/queue_baseline.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["step", "queue"])
    writer.writerows(queue_log)

print("✅ Baseline queue saved to logs/queue_baseline.csv")