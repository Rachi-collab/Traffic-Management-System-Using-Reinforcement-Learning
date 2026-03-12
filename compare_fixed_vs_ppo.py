st.subheader("🚗 Queue Length: Fixed vs PPO")

fig, ax = plt.subplots(figsize=(5.5, 3))

ax.plot(
    fixed_df["step"],
    fixed_df["queue"],
    label="Fixed-Time",
    color="#ef4444",
    linewidth=1.6
)

ax.plot(
    ppo_df["step"],
    ppo_df["queue"],
    label="PPO",
    color="#22c55e",
    linewidth=1.6
)

ax.set_xlabel("Simulation Step")
ax.set_ylabel("Queue Length")
ax.legend(frameon=False)
ax.grid(alpha=0.25)

st.pyplot(fig)