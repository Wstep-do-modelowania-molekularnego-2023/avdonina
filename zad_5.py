import numpy as np
import matplotlib.pyplot as plt

# 5.1
def quartic_function(x, a, e_2, yNz_prime, yNz):
    return a*x**4 - 6*a*e_2*x**2 + yNz_prime + yNz

a = 1.0
e_2 = 2.0
yNz_prime = 5.0
yNz = 0.2

x = np.linspace(-5, 5, 100)
potential_energy = quartic_function(x, a, e_2, yNz_prime, yNz)

plt.plot(x, potential_energy)
plt.xlabel('A')
plt.ylabel('kcal/mol')

# 5.2
# dU(x)/dx = 0
# 4x^3 - 24x + 5 = 0
# x1 = -2.55 -> min
# x2 = 0.21 -> max
# x3 = 2.34 -> min

# U(x1) = 42.28 - 78.03 - 12.75 +0.2= -48.3
# U(x2) = 0.002 - 0.53 + 1.05 + 0.2 = 0.72
# U(x3) = 29.92 -65.71 + 11.7 + 0.2 = -23,89
# Boltzmann population distribution equation Ni = const * exp (-Ei/kT)
# Stosunek populacji stanów = exp((-23.89+48.3)/0.593)=7.535
print('kalkulatorowo: ', np.exp((-23.89+48.3)/0.593))

# 5.3
# Napisz własny program Monte-Carlo z zastosowaniem algorytmu Metropolisa
# selekcjonującego 10000 reprezentatywnych dla rozkładu Boltzmanna stanów (10000
# zaakceptowanych położeń we „własnym koszyku”, prób będzie więcej) oraz pod
# wykresem funkcji energii potencjalnej lub na tym samym wykresie wykonaj
# unormowany plot rozkładu gęstości zaakceptowanych stanów. Najpierw dla ułatwienia
# przyjmij krok losowego przesunięcia „na prawo” lub „na lewo” o długości 0.25 A.
# Następnie losuj krok z rozkładu Gaussowskiego o maksimum w zerze i dyspersji 1 A

def metropolis(x, num_steps, step_size, fun):
    accepted_steps = []
    x_new = x + np.random.choice([-step_size, step_size])
    while len(accepted_steps)<num_steps:
        delta_energy = fun(x_new, a, e_2, yNz_prime, yNz) - fun(x, a, e_2, yNz_prime, yNz)

        if delta_energy < 0 or np.random.rand() < np.exp(-delta_energy):
            accepted_steps.append(x_new)
            x = x_new
        x_new = x + np.random.normal(0, 1)
    return accepted_steps

num_steps = 10000  
step_size = 0.25    
kT = 0.6      
x = 0.0

accepted_steps = metropolis(x, num_steps, step_size, quartic_function)
# Wykres rozkładu gęstości zaakceptowanych stanów, density=True daje unormowanie
plt.hist(accepted_steps, bins=100, density=True)
plt.show()

# 5.4
pos_steps = 0
neg_steps = 0
for x in accepted_steps:
    if x>=0: pos_steps+=1
    else: neg_steps+=1
if neg_steps == 0: neg_steps = 0.1
print('eksperymentalnie', pos_steps/neg_steps)
