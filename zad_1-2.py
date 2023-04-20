import math
import matplotlib.pyplot as plt
import numpy as np
import statistics



### 1

def verlet(x, v, f, dt, k, m):
    next_x = x + v*dt + (f * dt**2)/(2*m)
    next_f = policz_silę(k, next_x)
    next_v = v + ((f+next_f)*dt)/(2*m)

    return next_x, next_v, next_f

def euler(x, v, f, dt, k, m):
    next_x = x + v*dt + (f * dt**2)/(2*m)
    next_v = v + (f * dt)/(2*m)
    next_f = policz_silę(k, next_x)
    
    return next_x, next_v, next_f

# def leap_frog():
#     return None

def policz_E(m, k, x, v):
    return (m*v**2)/2 + (k*x**2)/2

def policz_silę(k, x):
    return -k*x

def main(k, m, n, dt):
    T = (2*math.pi)*(math.sqrt(k/m))
    full_time = T*n
    x, v = 0, 1
    f = policz_silę(k, x)
    dt *= T
    f_list = []
    x_list = []
    v_list = []
    e_list = []
    t_list = range(int(full_time/dt))
    for t_i in t_list:
        x, v, f = verlet(x, v, f, dt, k, m)
        # x, v, f = euler(x, v, f, dt, k, m)
        e = policz_E(m, k, x, v)
        
        f_list.append(f)
        x_list.append(x)
        v_list.append(v)
        e_list.append(e)
    return f_list, x_list, v_list, e_list, t_list

mass = 1
czas = 10
dt_list = [0.002, 0.001, 0.02, 0.04, 0.1]

for dt in dt_list:
    f_list, x_list, v_list, e_list, t_list = main(1, mass, czas, dt)
    e_avg = statistics.mean(e_list)
    e_stdev = statistics.stdev(e_list)
    p_list = [v*mass for v in v_list]

    print('średnia energii dla ' + str(round(dt, 4)) + ' : ' + str(round(e_avg, 5)) + '; odch standardowe: ' + str(round(e_stdev, 5)))

    plt.plot(t_list, x_list, label='x(t)')
    plt.title('oscylator harmoniczny dla ' + str(dt))
    plt.xlabel('czas')
    plt.ylabel('wartość')
    plt.plot(t_list, p_list, label='p(t)')
    plt.plot(t_list, e_list, label='E(t)')
    plt.legend(['x(t)', 'p(t)', 'E(t)'])
    plt.show()

    plt.plot(x_list, p_list)
    plt.title('zależność położenia i pędu')
    plt.xlabel('położenie')
    plt.ylabel('pęd')
    plt.show()

### 2
# E = m*v^2/2 + kx^2/2
