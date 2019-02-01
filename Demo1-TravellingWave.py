
# coding: utf-8

# In[1]:

from vpython import *
from numpy import *
from vpython import rate

scene.background = color.white

from ThreeD_QM_Models import TravellingWaveModel

"""
A 3D representation of free particle wavefunctions using the y and z directions
 to represent the phasor wave function.
"""

omega = 1.0 # radians per second
L = 3.0 # m
N = 400 # number of phasors to model line..
xarray = linspace(-L/2, L/2, N)
t=0.0 #s
dt=0.03 #s
k=5*pi*3/L #radians per meter
#k=0.0

def state(k, x, t):
    """
    return the value of the (not normalized) psi(x,t) for the nth quantum state
    """
    return exp(1j*(k*x - omega*t))

TWM = TravellingWaveModel(xarray, state, k, phaseToColor=True)

def keyInput(evt):
    s = evt.key
    if s in ('1','2','3','4'):
        TWM.toggleVisible(int(s))
    if s == ' ':
        paused ^= 1

scene.bind('keydown', keyInput)

paused = False

print("Ready to go...")

while True:
    rate(1/dt)
    if not paused:
        TWM.update(t)
        t+=dt
    else:
        pass


