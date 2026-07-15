# Traffic Management System Using Reinforcement Learning

An AI-based traffic signal control system that uses Reinforcement Learning to reduce congestion at a 4-way intersection, built with SUMO (Simulation of Urban Mobility) and trained using Proximal Policy Optimization (PPO).

## Overview

Traditional traffic signals run on fixed timers, regardless of actual traffic conditions. This project replaces that with an RL agent that observes real-time traffic at an intersection and dynamically decides which signal phase to activate, aiming to minimize vehicle wait times and queue lengths.

A custom Gymnasium environment wraps a SUMO traffic simulation, allowing the agent to be trained and evaluated using standard RL tooling.

## Features

- Custom Gymnasium environment built on top of SUMO
- Multi-lane traffic handling via edge-based aggregation
- State representation using a 2x2 spatial grid, suitable for CNN-based policies
- Reward function based on minimizing queue length and vehicle stops
- Agent trained using Proximal Policy Optimization (PPO)
- Performance comparison against traditional fixed-time traffic signals
- Streamlit interface for visualization/interaction

## Tech Stack

- **Language:** Python
- **Simulation:** SUMO (Simulation of Urban Mobility)
- **RL Environment:** Gymnasium
- **RL Algorithm/Training:** Stable-Baselines3 (PPO)
- **Deep Learning:** PyTorch
- **UI/Visualization:** Streamlit

## Results

The trained RL agent showed significant improvements over fixed-time signal control, particularly in reducing average vehicle waiting time and increasing intersection throughput under medium and high traffic density conditions.

## Getting Started

### Prerequisites

- Python 3.x
- [SUMO](https://eclipse.dev/sumo/) installed and added to your system PATH
- pip

### Installation

```bash
git clone https://github.com/Rachi-collab/Traffic-Management-System-Using-Reinforcement-Learning.git
cd Traffic-Management-System-Using-Reinforcement-Learning
pip install -r requirements.txt
```

### Usage

```bash
# Train the agent
python train.py

# Evaluate / run the trained agent
python evaluate.py

# Launch the Streamlit dashboard
streamlit run app.py
```

> Note: Adjust the commands above to match your actual script names if they differ.

## Project Structure

```
Traffic-Management-System-Using-Reinforcement-Learning/
├── env/               # Custom Gymnasium + SUMO environment
├── models/            # Saved/trained PPO models
├── sumo_config/        # SUMO network and simulation config files
├── train.py             # Training script
├── evaluate.py           # Evaluation script
├── app.py                # Streamlit app
└── requirements.txt
```

## Future Improvements

- Extend to multi-intersection / network-wide traffic control
- Incorporate real-world traffic data
- Experiment with alternative RL algorithms (e.g., DQN, A2C) for comparison

## Acknowledgments

Built using SUMO, Gymnasium, and Stable-Baselines3.
