import numpy as np
import matplotlib.pyplot as plt

# ------------ Profit as function of allocation between PT-rsETH and PT-weETH

# Fee Profit = a * (Allocation to PT-rsETH)^2 + b * (Allocation to PT-rsETH) + c

# ---------------------

# Define the range of allocaiton to PT-rsETH
# from 0 to 10 WETH
# from 0 to 10, generating 100 evenly spaced samples to generate within the interval
allocations = np.linspace(0, 10, 100)

# Define the coefficients for the quadratic equation
# We use the vertex form of a parabola: f(x) = a*(x-h)^2 + k
# Here, h=5 (x-coordinate of the vertex), k=3.2 (maximum value of the parabola)
a = -0.08  # Adjust 'a' to set the width of the parabola
h = 5
k = 3.2

# Calculate fee profit for each allocation
fee_profits = a * (allocations - h) ** 2 + k


# Plot the fee profits vs. allocations
plt.figure(figsize=(10, 6))
plt.plot(allocations, fee_profits, label="Fee Profit vs. Allocation to PT-rsETH")
plt.title("Fee Profit vs. PT-rsETH Allocation")
plt.xlabel("Allocation to PT-rsETH (WETH)")
plt.ylabel("Fee Profit")
plt.ylim(2.0, 3.5)  # Setting the y-axis limits to match your specification
plt.axvline(x=5, color="r", linestyle="--", label="Optimal Allocation (50/50 split)")
plt.legend()
plt.grid(True)
plt.show()
