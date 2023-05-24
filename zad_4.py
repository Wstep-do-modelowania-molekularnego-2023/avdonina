import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import random

# 4.1
# rozkład jednostajny
x = np.linspace(0, 1, 1000)
y = np.ones_like(x)
plt.plot(x, y)
plt.title("Rozkład jednostajny na odcinku [0,1]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# rozkład normalny 
x = np.linspace(-5, 5, 1000) 
y = [1 / (np.sqrt(2 * np.pi)) * np.exp(-0.5 * i ** 2) for i in x]
plt.plot(x, y)
plt.title("Rozkład normalny na R")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# 4.2
# rozkład jednostajny z liczb pseudolosowych
unif_r = [random.uniform(0, 1) for x in range(1000)] 
count, bins, ignored = plt.hist(unif_r, 10, density=True)
plt.plot(bins, np.ones_like(bins))
plt.title("Rozkład jednostajny na odcinku [0,1]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# rozkłąd normalny z liczb pseudolosowych
norm_r = [random.gauss(0, 1) for _ in range(1000)]
count, bins, ignored = plt.hist(norm_r, 10, density=True)
plt.plot(bins, 1/(1 * np.sqrt(2 * np.pi)) * np.exp(-0.5 * bins**2))
plt.title("Rozkład normalny na R")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
