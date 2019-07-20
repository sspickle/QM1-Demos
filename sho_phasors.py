#!/Library/Frameworks/Python.framework/Versions/2.6/bin/python
"""

Copyright (c) 2011, Steve Spicklemire

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
from vpython import *
from numpy import *
from vpython import rate

import scipy.special as sp
from ThreeD_QM_Models import SHOSupDemo

"""
A 3D representation of a superposition of two 1D quantum states using the y and z directions
 to represent the phasor wave function.
"""

omega = 5.0
L = 5.0
N = 150 # number of phasors to model line..
xarray = linspace(-L, L, N)
t=0.0
dt=0.01
gndPhase = 0.0  # phase of gnd state, useful for "rotating" with the gnd state

NTerms=10
polys = [sp.hermite(n) for n in range(NTerms+1)]
vecs = [polys[i](xarray)*exp(-xarray**2/2.0)/sqrt(2**i*factorial(i)) for i in range(len(polys))]

def state(n, j, t):
    """
    return the value of the (not normalized) psi(x,t) for the nth quantum state
    """
    if j>=0:
        return vecs[n][j]*exp(-1j*(1.0*n+0.5)*t*omega)  # individual position
    else:
        return vecs[n]*exp(-1j*(1.0*n+0.5)*t*omega)     # array calculation
        
            
TSM = SHOSupDemo(xarray, state, Nterms=10)
updateScreen = False
TSM.update(0.0)

def keyInput(evt):
    global relPhase, gndPhase, t, updateScreen
    s = evt.key
    if s in ('1','2','3','4','5','6','7','s','p'):
        if s=='s':
            s=8
        if s=='p':
            s=9
        TSM.toggleVisible(int(s))
    elif s=='r':
        t=0.0
        TSM.update(t)
        updateScreen=False
    elif s==' ':
        updateScreen ^= 1
    elif s=='right':
        t+=dt
        TSM.update(t)
        updateScreen=False
    elif s=='left':
        t-=dt
        TSM.update(t)
        updateScreen=False
    elif s=='up':
        TSM.bumpVisible(+1)
    elif s=='down':
        TSM.bumpVisible(-1)

scene.bind('keydown', keyInput)

while True:
    rate(100)
    if updateScreen:
        TSM.update(t)
        t+=dt
