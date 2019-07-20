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

from ThreeD_QM_Models import PhasorModel

"""
A 3D representation of free particle wavefunctions using the y and z directions
 to represent the phasor wave function.
"""

omega = 1.0
L = 1.0
N = 100 # number of phasors to model line..
xarray=zeros(1)*1.0
t=0.0
dt=0.01
k=2*pi*3/L

cylinder(pos=vec(-.1,0,0), axis=vec(0.2,0,0), radius=0.001, color=color.green)

def state(k, x, t):
    """
    return the value of the (not normalized) psi(x,t) for the nth quantum state
    """
    return exp(1j*(k*x - omega*t))

PM = PhasorModel(xarray, state, k, phaseToColor=False)
paused = False

def keyInput(evt):
    global paused
    s = evt.key
    if s in ('1','2','3'):
        TWM.toggleVisible(int(s))
    elif s == ' ':
        paused ^= 1

scene.bind('keydown', keyInput)

while True:
    rate(100)
    if not paused:
        PM.update(t)
        t+=dt

