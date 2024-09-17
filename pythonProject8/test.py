from math import pi
import pandas as pd
import matplotlib.pyplot as plt

density = 1.25  # "kg/m^3"
efficiency = 0.3  # dimensionless
diameters = [20, 40, 60, 80]  # All diameters are in "m"
velocities = [5, 10, 15, 20]  # All velocities are in "m/s"

table_data = []

for diameter in diameters:
    mass_flow_rates = []
    actual_electric_powers = []

    for velocity in velocities:
        # calculates kinectic energy of the wind.
        kinectic_energy = (velocity ** 2) / 2  # J/kg

        # calculates mass flow rates
        mass_flow_rate = density * velocity * (((pi) * (diameter ** 2)) / 4)  #

        # Actual power generation is determined by multiplying the power generation potential by efficiency.
        actual_electric_power = efficiency * mass_flow_rate * kinectic_energy  # Watt

        # appends the calculated values of mass flow rate and actual electric power to the lists of mass flow rates and actual electric powers
        mass_flow_rates.append(round(mass_flow_rate))
        actual_electric_powers.append(round(actual_electric_power, -3))

        # rows of table data
        row = {
            'D, m': diameter,
            'V, m/s': velocities,
            'm, kg/s': mass_flow_rates,
            'W_elect, W': actual_electric_powers
        }

    # appends each table row to the table_data
    table_data.append(row)

    # plots the graph of Wind turbine power vs Velocity and diameter
    plt.plot(velocities, actual_electric_powers)
    plt.xlim(4, 20)
    plt.ylim(0, 8000000)

# Displays the graph
plt.show()

# tabulate and display results.
pd.DataFrame(table_data)