import pandas as pd
import numpy as np
from stable_baselines3 import PPO
from env.traffic_env import TrafficEnv

SUMO_CONFIG = "sumo/intersection.sumocfg"
MODEL_PATH = "ppo_traffic_model.zip"
MAX_STEPS = 1000
OUTPUT_FILE = "metrics.csv"

# Create environment
env = TrafficEnv(SUMO_CONFIG)

# Load trained PPO model
model = PPO.load(MODEL_PATH)

obs, _ = env.reset()

data = []

for step in range(MAX_STEPS):

    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)

    done = terminated or truncated

    total_queue = np.sum(obs[:8])   # adjust if needed
    phase = obs[8]
    sim_time = obs[9]

    data.append({
        "step": step,
        "reward": reward,
        "total_queue": total_queue,
        "phase": phase,
        "sim_time": sim_time
    })

    if done:
        break

df = pd.DataFrame(data)
df.to_csv(OUTPUT_FILE, index=False)

env.close()
print("Evaluation complete. Metrics saved.")