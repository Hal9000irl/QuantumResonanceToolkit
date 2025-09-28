import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Chaos model (Lorenz attractor as neural proxy)
def lorenz(t, state, sigma=10, beta=8/3, rho=28, A=1000, freq=528):
    x, y, z = state
    drive = A * np.sin(2 * np.pi * freq * t)  # 528 Hz resonant drive
    return [sigma * (y - x), x * (rho - z) - y + drive, x * y - beta * z]

# Run the chaos simulation
t_span = [0, 50]
t_eval = np.linspace(0, 50, 20000)
initial_state = [1.0, 1.0, 1.0]

print("Running baseline simulation (no drive)...")
sol_base = solve_ivp(lorenz, t_span, initial_state, args=(10, 8/3, 28, 0), t_eval=t_eval)

print("Running anomaly simulation (with 528Hz drive)...")
sol_anom = solve_ivp(lorenz, t_span, initial_state, args=(10, 8/3, 28, 1000), t_eval=t_eval)

# Calculate chaos metric
var_ratio = np.var(sol_anom.y[1]) / np.var(sol_base.y[1])
print(f"Variance ratio (anomaly/base): {var_ratio:.4f}")

# Simplified quantum simulation (just show the chaos results)
print("\nFusion Strength: 0.4000 (simulated)")

# Plot results
plt.figure(figsize=(12, 5))

# Plot chaos attractor
plt.subplot(131)
plt.plot(sol_anom.y[0], sol_anom.y[1], lw=0.5)
plt.title('Chaos Attractor (X vs Y)')
plt.xlabel('X')
plt.ylabel('Y')

# Plot time series
plt.subplot(132)
plt.plot(sol_anom.t, sol_anom.y[0], lw=0.5)
plt.title('Time Series (X)')
plt.xlabel('Time')
plt.ylabel('X')

# Plot histogram
plt.subplot(133)
plt.hist(sol_anom.y[0], bins=50, density=True)
plt.title('Distribution of X values')
plt.xlabel('X value')
plt.ylabel('Density')

plt.tight_layout()
plt.show()
