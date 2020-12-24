#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
import pandas as pd

mass_of_Sun = 1.99e+33 # g 
mass_of_Earth = 5.98e+27 #g
mass_of_Jupiter = 1.898e+30 # g
radius_of_Sun = 6.96e+10 # cm
radius_of_Earth = 6.38e+8 # cm
radius_of_Jupiter = 6.9911e+9 # cm

# Rsch = 2.95e+5 cm (M/Msun) = 2.95 km (M/Msun)
# M/Msun = R/2.95 km

# nuclear density 2.3e+17 kg/m3 = 2.3e+14 g/cm3 

plt.style.use('../style/matplotlibrc_stars_mass_radius')

radius_solar_system = []
mass_solar_system = []
radius_star = []
mass_star = []
radius_exoplanet = []
mass_exoplanet = []
for line in open('data/arXiv1603.0861_data_table.lst'):
	cols = line.split(',')
	mass_solar = float(cols[1])
	radius_km = float(cols[2]) * radius_of_Sun * 1e-5
	symbol = cols[3]
	if 'solar_system' in symbol:
		print(cols[0],mass_solar,radius_km)
		mass_solar_system.append(mass_solar)
		radius_solar_system.append(radius_km)
	if 'star' in symbol:
		print(cols[0],mass_solar,radius_km)
		mass_star.append(mass_solar)
		radius_star.append(radius_km)
	if 'exoplanet' in symbol:
		print(cols[0],mass_solar,radius_km)
		mass_exoplanet.append(mass_solar)
		radius_exoplanet.append(radius_km)

radius_blackhole = np.logspace(-4,3,10)
mass_blackhole = radius_blackhole / 2.95 

radius_template = np.logspace(-4,7,10)
mass_nuclear = 4.0 * np.pi / 3.0 * (radius_template*1e+5)**3 * 2.3e+14 / mass_of_Sun
mass_one = 4.0 * np.pi / 3.0 * (radius_template*1e+5)**3 * 1.0 / mass_of_Sun

df_kip = pd.read_csv('data/kipthorne.csv',names=["perimeter_km","mass_solar"])
curve_km = df_kip["perimeter_km"]/2.0/np.pi
curve_mass = df_kip["mass_solar"]

#fig = plt.figure()
fig, ax = matplotlib.pyplot.subplots(1,figsize=(10,12),sharex=True,squeeze=True)
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)  

ax.plot(radius_exoplanet,mass_exoplanet,marker='o',markerfacecolor='w',markeredgecolor='#7F8C8D',linewidth=0)
ax.plot(radius_star,mass_star,marker='o',markerfacecolor='#F1C40F',markeredgecolor='#E67E22',markersize=8,linewidth=0)
ax.plot(radius_solar_system,mass_solar_system,marker='o',markerfacecolor='#873600',markeredgecolor='k',markersize=10,linewidth=0)
ax.plot(radius_blackhole,mass_blackhole,color='k')
#ax.plot(curve_km,curve_mass)
ax.plot(radius_template,mass_nuclear,"--",color="#99A3A4")
ax.plot(radius_template,mass_one,"--",color="#99A3A4")
ax.plot([radius_of_Earth*1e-5],[mass_of_Earth/mass_of_Sun],marker="o",color="#3498DB",markersize=20,markeredgecolor='#1B4F72')
ax.plot([radius_of_Sun*1e-5],[1.0],marker="*",color="#F1C40F",markersize=40,markeredgecolor='#B9770E')
ax.plot([radius_of_Sun*0.0084*1e-5],[1.018],marker="s")
ax.axhline(0.08,linestyle="-.",color="#99A3A4")

ax.set_xlim(1,1e+7)
#ax.set_ylim(1e-5,1e+2)  
ax.set_ylim(1.5e-6,9)
ax.set_xscale('log')
ax.set_yscale('log')
#ax.set_yscale('linear')
ax.set_xlabel("Stellar Radius (km)",labelpad=14)
ax.set_ylabel("Stellar Mass (Solar mass)",labelpad=14)

plt.tight_layout()
fig.savefig("stars_mass_radius.pdf")






