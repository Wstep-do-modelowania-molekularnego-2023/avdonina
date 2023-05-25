### 3 
# mass(CO) = 4.65 * 10**(-26) kg
# frequency of oscillation (CO) = 6.42 * 10**13 Hz
# reduced mass miu = m(c)*m(o)/(m(c)+m(o)) => 1.139 * 10**(-26) kg
# konstant k = 1842 N/m
# what change in vibrational energy can lead to an electron transition <=> delta E = h*f (freq) = 0.265eV 

# Mx1'' = F(1,2)(x1,x2)
# mx2'' = F(2,1)(x1,x2) = -F(1,2) (z 3 zasady dynamiki)
# Mx1'' + mx2'' = F(1,2)+F(2,1) = 0 
# (Mx1'' + mx2'') / (M+m) = 0 = X''
# (położenie środka masy) X= (Mx1'' + mx2'')/(M+m)
# (różnica położeń) x = x1-x2                                               (siły centralne) F(1,2)(x1,x2) = F(1,2)(x1-x2)
# x'' = x1'' - x2'' = F(1,2)/M - F(2,1)/m = F(1,2)/M + F(1,2)/m = (1/M+1/m)*F(1,2) = (1/M+1/m)*F(1,2)(x)
# 1/(1/M+1/m) * x'' = F(1,2)(x) = -k*x (-> prześliśmy do kulki na sprężynce, która doczepiona do ściany)
# k - z eksperymentu
#  1/(1/M+1/m) = m*M/(m+M) -> masa bezwymiarowa miu 
# 
# (1) mała kulka bardzo mała: m<<M  => Mm/M = m (mała kulka na ścianie)
# (2) m=M => miu = MM/M+M = M/2

# freq = d_e/h

import math
import matplotlib.pyplot as plt
import numpy as np

def verlet(x, v, f, dt, k, m):
    next_x = x + v*dt + (f * dt**2)/(2*m)
    next_f = policz_silę(k, next_x)
    next_v = v + ((f+next_f)*dt)/(2*m)

    return next_x, next_v, next_f

def policz_E(m, k, x, v):
    return (m*np.power(v,2))/2 + (k*np.power(x,2))/2

def policz_silę(k, x):
    return -k*x

def main(k, m, n, dt):
    T = 2*math.pi*(np.sqrt(m/k))
    x, v = 0, 1
    f = policz_silę(k, x)
    print('f', f)
    dt = dt*T
    full_time = T*n
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


u = (15.99*12.01)/(15.99+12.01)
miu = 1.139 * 10**(-26) 
k_co = 1842
e_transition = 4.24* 1/np.power(10,20)
dt = 0.2
h = 6.626 * np.power(10.,-34)
k_przez_m = k_co/miu
print(math.sqrt(k_przez_m))

f_list, x_list, v_list, e_list, t_list = main(k_co, miu, 10, dt)
p_list = np.array(v_list)*miu


for i in range(len(e_list)-1):
    if e_list[i+1]-e_list[i] >= e_transition:
        print('przejście')

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
