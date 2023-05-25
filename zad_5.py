import numpy as np
import matplotlib.pyplot as plt

# 5.1
def quartic_function(x, a, e_2, yNz_prime, yNz):
    return .04*(x**4 - 6*e_2*x**2 + yNz_prime*x + yNz)

a = 1
e_2 = 2.0
yNz_prime = 5.0
yNz = 0.2

x = np.linspace(-5, 5, 100)
potential_energy = quartic_function(x, a, e_2, yNz_prime, yNz)

plt.plot(x, np.array(potential_energy)/12)
plt.xlabel('A')
plt.ylabel('kcal/mol')

# 5.2 
# dU(x)/dx = 0
# 0.16x^3 - 0.96x + 0.2 = 0
# x1 = -2.5477 -> min
# x2 = 0.2099 -> max
# x3 = 2.3438 -> min

# U(x1) = -1.9319
# U(x3) = -0.9530
# Boltzmann population distribution equation Ni = const * exp (-Ei/kT)
# Stosunek populacji stanów = exp((-0.9530+1.9319)/0.593) = 5.2109
print('kalkulatorowo: ', np.exp((-0.9530+1.9319)/0.593))

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
    while len(accepted_steps)<num_steps:
        x_new = x + np.random.normal(0, 0.5)
        delta_energy = fun(x_new, a, e_2, yNz_prime, yNz) - fun(x, a, e_2, yNz_prime, yNz)

        if delta_energy < 0 or np.random.rand() < np.exp(-delta_energy):
            accepted_steps.append(x_new)
            x = x_new
        
    return accepted_steps

num_steps = 10000  
step_size = 0.25    
kT = 0.593     
x = 0.0

accepted_steps = metropolis(x, num_steps, step_size, quartic_function)

# Wykres rozkładu gęstości zaakceptowanych stanów, density=True daje unormowanie
plt.hist(accepted_steps, bins=20, density=True)
plt.show()

# 5.4
accepted_steps = np.array(accepted_steps)

pos_steps = len(accepted_steps[accepted_steps>0])

neg_steps = num_steps-pos_steps
if neg_steps == 0: neg_steps=0.0001
print('eksperymentalnie', pos_steps/neg_steps)
