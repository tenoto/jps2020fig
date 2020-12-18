#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

fig = plt.figure()
plt.plot(x,y)
fig.savefig("stars_mass_radius.pdf")