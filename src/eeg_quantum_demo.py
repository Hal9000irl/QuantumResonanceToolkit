import numpy as np
import matplotlib.pyplot as plt

# Mock EEG generation (e.g., 40 Hz gamma waves for consciousness proxy)
t = np.linspace(0, 0.1, 1000)  # 100 ms sample
freq = 40  # Gamma frequency (Orch-OR relevant)
eeg_signal = np.sin(2 * np.pi * freq * t) + 0.2 * np.random.randn(len(t))  # Noisy signal

# Map EEG to quantum amplitudes (basic normalization)
amplitudes = np.abs(eeg_signal) / np.max(np.abs(eeg_signal))  # 0-1 scale for qubit weights

# Simple quantum state from EEG (demo: superposition based on mean amplitude)
from qutip import basis, ket2dm
mean_amp = np.mean(amplitudes)
psi = np.sqrt(mean_amp) * basis(2, 0) + np.sqrt(1 - mean_amp) * basis(2, 1)
rho = ket2dm(psi)  # Density matrix

# Coherence score (simplified metric)
coherence = abs(rho[0,1])**2  # Off-diagonal element
print(f"Coherence Score from EEG: {coherence:.4f}")

# Visuals
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.plot(t, eeg_signal, label='Mock EEG (40 Hz)')
plt.legend()
plt.title('EEG Signal Input')
plt.subplot(122)
plt.bar(['|0>', '|1>'], [abs(psi[0])**2, abs(psi[1])**2])
plt.title('Quantum State from EEG')
plt.show()

# Teaser for premium: "Full EEG integration with QEEGNet available in consulting services."