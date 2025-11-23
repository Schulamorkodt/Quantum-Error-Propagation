# CNOT Error Propagation Simulator

This project demonstrates how **Pauli X and Z errors propagate through a CNOT gate**
in both the **bit basis** and **phase basis**, using Qiskit.

It includes:

- Simulations of X / Z error propagation
- Visualizations of the resulting circuits
- Statevector simulations before and after CNOT
- A full Jupyter notebook
- A standalone Python script version

---

## Installation
This project is built around a conda environment:

Create and activate the environment:
```bash
conda env create -f environment.yml
conda activate quantum-error-prop
```

---

## Python Script

This repository walks through:

- applying CNOT in bit basis
- applying CNOT in phase basis
- injecting X or Z Pauli errors
- visualizing how they propagate
- plotting Bloch spheres and measurement outcomes

---

All code is located in:
```python
`quantum_error_prop/code.py`
```

