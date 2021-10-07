#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:33:41 2021

@author: SamR
"""
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.constants import *


V_o = 1000 ##eV
V_o = V_o * electron_volt #Joules

a = 0.529E-10 #m
#h_bar = (6.63E-34)/2*np.pi # J/s
h_bar= hbar
#m = 9.10938356E-31 #kg
m = m_e
k = np.sqrt(2*m*(a**2)*V_o/(h_bar**2))
#print(k)
s = np.linspace(0, k, 600)

#func = lambda s : s * (np.cos(s)/np.sin(s))

#func2 = lambda s : -np.sqrt(k**2-s**2)

#func3 = lambda s : s * (np.cos(s)/np.sin(s)) - (-np.sqrt(k**2-s**2))

#func3 = lambda s : func(s) - func2(s)

def func(s):
    return s * (np.cos(s)/np.sin(s))
def func2(s):
    return -np.sqrt(k**2-s**2)
def func3(s):
    return func(s) - func2(s)

#plt.plot(s, func(s))
#plt.plot(s, func2(s))
plt.plot(s, func3(s))
plt.grid()
plt.show()

# Use the numerical solver to find the roots

s_initial_guess = 3
s_solution, outPutinfo, ier, mesg  = fsolve(func3, s_initial_guess, full_output = True )
print("")
print(outPutinfo)
print("")

print ("The solution is s = %f" % s_solution)
print ("at which the value of the expression is %f" % func3(s_solution))

s_initial_guess2 = 5.5
s_solution2 = fsolve(func3, s_initial_guess2)
print ("The solution is s = %f" % s_solution2)
print ("at which the value of the expression is %f" % func3(s_solution2))

s_initial_guess3 = 8
s_solution3 = fsolve(func3, s_initial_guess3)
print ("The solution is s = %f" % s_solution3)
print ("at which the value of the expression is %f" % func3(s_solution3))


print("")
print("*************")
print("")

E1 = ((s_solution**2/k**2)-1)*-V_o 
E2 = ((s_solution2**2/k**2)-1)*-V_o
E3 = ((s_solution3**2/k**2)-1)*-V_o 
print("E1:  ", E1, "Joules or ", E1*6.242E+18, "eV")
print("E2:  ", E2, "Joules or ", E2*6.242E+18, "eV")
print("E3:  ", E3, "Joules or ", E3*6.242E+18, "eV")

print("")
print("*************")
print("")