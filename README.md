# 🚦 AI Traffic Signal Control System using Reinforcement Learning

##  Overview

Traffic congestion is a major issue in urban areas due to inefficient traffic signal timings.
This project implements an **AI-based Traffic Signal Control System** using **Model-Free Reinforcement Learning (PPO algorithm)** to dynamically optimize traffic light timings and improve traffic flow.

The system interacts with the **SUMO (Simulation of Urban Mobility)** traffic simulator and learns the optimal signal policy by observing traffic states such as vehicle queues and waiting times.

A **Streamlit Dashboard** is also integrated to visualize traffic metrics and model performance.

---

##  Objectives

* Reduce vehicle waiting time at intersections
* Minimize traffic congestion
* Optimize traffic signal phase timing
* Provide real-time traffic visualization through dashboard

---

##  Technologies Used

| Technology                   | Purpose                     |
| ---------------------------- | --------------------------- |
| Python                       | Core programming language   |
| SUMO                         | Traffic simulation          |
| Reinforcement Learning (PPO) | AI model training           |
| Stable-Baselines3            | RL algorithm implementation |
| Streamlit                    | Interactive dashboard       |
| Matplotlib / Plotly          | Data visualization          |
| Pandas / NumPy               | Data processing             |

---

##  System Architecture

Traffic Environment → RL Agent → Action (Signal Change) → Reward → Policy Update

1. The **environment** simulates traffic using SUMO.
2. The **agent observes state variables** such as:

   * Queue length
   * Waiting time
   * Vehicle density
3. The **agent selects an action** (traffic signal phase).
4. A **reward is calculated** based on traffic performance.
5. The **PPO algorithm updates the policy** to improve future decisions.

---

##  Key Features

* Model-Free Reinforcement Learning based control
* Traffic signal optimization
* Real-time traffic monitoring dashboard
* Simulation-based training using SUMO
* Data visualization for performance analysis

---

##  Project Structure

traffic_rl_project/

app.py – Streamlit dashboard
train.py – Reinforcement learning training script
intersection.net.xml – Traffic network file
routes.rou.xml – Vehicle routes
sumo_config.sumocfg – SUMO configuration
requirements.txt – Python dependencies

---

##  Installation

###  Clone the repository

```bash
git clone https://github.com/yourusername/traffic-rl-project.git
cd traffic-rl-project
```

###  Create virtual environment

```bash
python -m venv .venv
```

###  Activate environment

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

###  Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Running the Project

### Train the RL model

```bash
python train.py
```

### Run the dashboard

```bash
streamlit run app.py
```

---

##  Output

The system provides insights such as:

* Vehicle waiting time
* Traffic density
* Signal phase decisions
* Congestion trends

The dashboard visualizes these metrics in **real time graphs and charts**.

---

##  Future Improvements

* Multi-intersection traffic coordination
* Integration with real-world traffic sensors
* Deep Reinforcement Learning enhancements
* Real-time city traffic deployment
* Edge AI based smart traffic signals

---

##  Author

Rachi Rajpal
B.Tech CSE Student

---

##  License

This project is for **educational and research purposes**.
