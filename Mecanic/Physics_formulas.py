'''
This file contains the formulas used in the Physics problems, I'm going to update it as I put others
problems.

Alert!!! The parameters of the functions must be passed in the International Unit System. 
'''

'''
Physics Constants:
'''

g = 9.81 # Gravitational acceleration [m/s^2]

'''
Genral formulas:
'''

def Kinetic_Energy(m,v):
    from numpy import power
    v2 = power(v,2)
    K = 0.5*m*v2
    return K

def Potential_Gravitational_Energy(m,h):
    U = m*g*h
    return U

def Elastic_Energy(k,x):
    from numpy import power
    x2 = power(x, 2)
    U = 0.5*k*x2
    return U

def Mecanic_Energy(m,v,h,k=0,x=0):
    K = Kinetic_Energy(m,v)
    U = Potential_Gravitational_Energy(m,h) + Elastic_Energy(k,x)
    return K + U

'''
Nonlinear pendulum specific formulas:
'''

def specific_kinetic_energy(l, w):
    from numpy import power
    k = 0.5*power(l*w,2)
    return k

def specific_potential_gravitational_energy(l, theta):
    from numpy import cos
    u = g*l*(1-cos(theta))
    return u

def specific_mecanic_energy(l,w,theta):
    k = specific_kinetic_energy(l,w)
    u = specific_potential_gravitational_energy(l,theta)
    return k+u
