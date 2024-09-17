import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 0.1  # Diffusivity
rho = 1000  # Density of the fluid
g = 9.81  # Gravitational acceleration
r_min, r_max = 0.0, 100.0  # Radial domain (in meters)
z_min, z_max = 0.0, 50.0  # Vertical domain (in meters)
t_max = 10.0  # Time duration (in seconds)
dr = 0.05  # Reduced radial spacing (in meters)
dz = 0.05  # Reduced vertical spacing (in meters)
dt = 0.0005  # Reduced time step (in seconds)

# Discretize the domain
Nr = int((r_max - r_min) / dr) + 1  # Number of radial nodes
Nz = int((z_max - z_min) / dz) + 1  # Number of vertical nodes
Nt = int(t_max / dt)  # Number of time steps

# Initialize pressure field (p) at all grid points (time t=0)
p = np.zeros((Nr, Nz))  # Pressure at time t
p_new = np.zeros_like(p)  # Pressure at time t+1

# Initial condition (arbitrary example)
p[:, :] = 10.0  # Set initial pressure

# Radial grid points
r = np.linspace(r_min, r_max, Nr)

# Time-stepping loop
for n in range(Nt):
    # Apply Dirichlet boundary conditions (fixed pressure at boundaries)
    p[0, :] = 50000  # Fix pressure at r=0 (inner boundary)
    p[-1, :] = 10000  # Fix pressure at r=r_max (outer boundary)

    for i in range(1, Nr - 1):  # Skip boundaries for now
        for j in range(1, Nz - 1):  # Skip boundaries for now
            r_i = r[i]  # Radial position

            # Finite difference for spatial derivatives
            d2p_dr2 = (p[i + 1, j] - 2 * p[i, j] + p[i - 1, j]) / dr ** 2
            dp_dr = (p[i + 1, j] - p[i - 1, j]) / (2 * dr)
            d2p_dz2 = (p[i, j + 1] - 2 * p[i, j] + p[i, j - 1]) / dz ** 2

            # Update pressure field using finite difference scheme
            p_new[i, j] = p[i, j] + dt * (
                    alpha * (d2p_dr2 + (1 / r_i) * dp_dr + d2p_dz2) + rho * g
            )

    # Update pressure field for the next time step
    p[:, :] = p_new[:, :]

# Plot the pressure field after time evolution
plt.imshow(p, extent=[r_min, r_max, z_min, z_max], origin='lower', cmap='viridis')
plt.colorbar(label="Pressure")
plt.xlabel("Radial direction (m)")
plt.ylabel("Vertical direction (m)")
plt.title("Pressure Field at Final Time")
plt.show()

