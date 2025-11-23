# ============================================================
# CNOT ERROR PROPAGATION SIMULATION
# ============================================================

from qiskit import QuantumCircuit, QuantumRegister, Aer, execute
from qiskit.quantum_info import Statevector
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# X ERROR PROPAGATION IN BIT BASIS
# ============================================================

# Create quantum registers
qreg = QuantumRegister(2, 'q')
qc_xbit_error = QuantumCircuit(qreg)

# Apply X gate on control qubit before CNOT
qc_xbit_error.x(qreg[0])

# Apply CNOT gate
qc_xbit_error.cx(qreg[0], qreg[1])

# Draw the circuit
qc_xbit_error.draw('mpl')

# Simulate the resulting statevector
backend = Aer.get_backend('statevector_simulator')
result = execute(qc_xbit_error, backend).result()
state = result.get_statevector()

# Bloch Z-coordinates for control and target after X error + CNOT
z_control = abs(state[0])**2 - abs(state[1])**2
z_target  = abs(state[2])**2 - abs(state[3])**2

# Plot results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Control Qubit (X Error in Bit Basis)')
plt.scatter([0], [z_control], color='red')
plt.ylim(-1, 1)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.title('Target Qubit (X Error in Bit Basis)')
plt.scatter([0], [z_target], color='blue')
plt.ylim(-1, 1)
plt.grid(True)

plt.suptitle('CNOT X Error Propagation in Bit Basis')
plt.show()



# ============================================================
# Z ERROR PROPAGATION IN PHASE BASIS
# ============================================================

qreg2 = QuantumRegister(2, 'q')
qc_zphase_error = QuantumCircuit(qreg2)

# Apply Z error on target qubit before CNOT
qc_zphase_error.z(qreg2[1])

# Apply CNOT
qc_zphase_error.cx(qreg2[0], qreg2[1])

qc_zphase_error.draw('mpl')

# Simulate statevector
result2 = execute(qc_zphase_error, backend).result()
state2 = result2.get_statevector()

# Bloch Z coordinates after applying Z error then CNOT
z_control_phase = abs(state2[0])**2 - abs(state2[1])**2
z_target_phase  = abs(state2[2])**2 - abs(state2[3])**2

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Control Qubit (Z Error in Phase Basis)')
plt.scatter([0], [z_control_phase], color='green')
plt.ylim(-1, 1)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.title('Target Qubit (Z Error in Phase Basis)')
plt.scatter([0], [z_target_phase], color='purple')
plt.ylim(-1, 1)
plt.grid(True)

plt.suptitle('CNOT Z Error Propagation in Phase Basis')
plt.show()



# ============================================================
# VISUALIZE FINAL CIRCUITS
# ============================================================
print("\n=== CNOT + X error circuit (bit basis) ===")
qc_xbit_error.draw('mpl')

print("\n=== CNOT + Z error circuit (phase basis) ===")
qc_zphase_error.draw('mpl')

