#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
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

plt.style.use('script/matplotlibrc_stars_mass_radius')

radius_solar_system = []
radius_km_solar_system = []
mass_solar_system = []
radius_star = []
radius_km_star = []
mass_star = []
radius_exoplanet = []
radius_km_exoplanet = []
mass_exoplanet = []
radius_whitedwarf = []
radius_km_whitedwarf = []
mass_whitedwarf = []
for line in open('data/arXiv1603.0861_data_table.lst'):
	cols = line.split(',')
	mass_solar = float(cols[1])
	radius_solar = float(cols[2]) 
	radius_km = float(cols[2]) * radius_of_Sun * 1e-5
	symbol = cols[3]
	if 'solar_system' in symbol:
		print(cols[0],mass_solar,radius_km)
		mass_solar_system.append(mass_solar)
		radius_solar_system.append(radius_solar)
		radius_km_solar_system.append(radius_km)
	if 'star' in symbol:
		print(cols[0],mass_solar,radius_km)
		mass_star.append(mass_solar)
		radius_star.append(radius_solar)		
		radius_km_star.append(radius_km)
	if 'exoplanet' in symbol:
		print(cols[0],mass_solar,radius_km)
		mass_exoplanet.append(mass_solar)
		radius_exoplanet.append(radius_solar)
		radius_km_exoplanet.append(radius_km)

for line in open('data/arXiv0908.2624_data_table.lst'):
	cols = line.split(',')
	mass_solar = float(cols[0])
	radius_solar = float(cols[1]) 	
	if radius_solar < 8:
		mass_star.append(mass_solar)
		radius_star.append(radius_solar)	

for line in open('data/arXiv1611.00629_data_table.lst'):
	cols = line.split(',')
	mass_solar = float(cols[0])
	radius_solar = float(cols[1]) 	
	mass_whitedwarf.append(mass_solar)
	radius_whitedwarf.append(radius_solar)		

fig = plt.figure(figsize=(10,12))
fig.patch.set_alpha(0.0)
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

plt.setp([ax1,ax2], xscale="log", yscale="log")
ax1.get_shared_x_axes().join(ax1, ax2)

xx = np.logspace(-7,7,100) # radius_of_Sun
yy_bh = xx * radius_of_Sun * 1e-5 / 2.95 
mass_nuclear2 = 4.0 * np.pi / 3.0 * (xx*radius_of_Sun)**3 * 2e+14 / mass_of_Sun
mass_nuclear3 = 4.0 * np.pi / 3.0 * (xx*radius_of_Sun)**3 * 3e+14 / mass_of_Sun
mass_degenerate = 4.0 * np.pi / 3.0 * (xx*radius_of_Sun)**3 * 1e+6 / mass_of_Sun
mass_one = 4.0 * np.pi / 3.0 * (xx*radius_of_Sun)**3 * 1.0 / mass_of_Sun

# last page http://www2.yukawa.kyoto-u.ac.jp/~masaru.shibata/2016.05.11.pdf 
# compactness eta = GM/Rc^2 
# -> M = eta * Rc^2/G = eta * R/3km * 2Ms
# -> M/Ms = 2/3 * eta (R/km)
mass_compact = 2.0/3.0 * 0.1 * xx * radius_of_Sun * 1e-5 

ax1.axhline(0.08,linestyle="-.",color="#99A3A4") #hydrogen burning
ax1.axhline(1.4,linestyle="-.",color="#99A3A4") #Chandrasekar 
ax1.axhline(3.0,linestyle="-.",color="#99A3A4") #maximum mass of neutron star

ax1.plot(xx,yy_bh)
ax1.plot(xx,mass_nuclear2,"--",color="#99A3A4")
ax1.plot(xx,mass_nuclear3,"--",color="#99A3A4")
ax1.plot(xx,mass_degenerate,"--",color="#99A3A4")
ax1.plot(xx,mass_one,"--",color="#99A3A4")
ax1.plot(xx,mass_compact,"--",color="#99A3A4")
ax1.plot(radius_whitedwarf,mass_whitedwarf,marker='s',markerfacecolor='w',markeredgecolor='#7F8C8D',linewidth=0)
ax1.plot(radius_exoplanet,mass_exoplanet,marker='o',markerfacecolor='w',markeredgecolor='#7F8C8D',linewidth=0)
ax1.plot(radius_star,mass_star,marker='o',markerfacecolor='#F1C40F',markeredgecolor='#E67E22',markersize=8,linewidth=0)
ax1.plot(radius_solar_system,mass_solar_system,marker='o',markerfacecolor='#873600',markeredgecolor='k',markersize=10,linewidth=0)
ax1.plot([radius_of_Earth/radius_of_Sun],[mass_of_Earth/mass_of_Sun],marker="o",color="#3498DB",markersize=20,markeredgecolor='#1B4F72')
ax1.plot([1.0],[1.0],marker="*",color="#F1C40F",markersize=40,markeredgecolor='k')
ax1.plot([0.0084],[1.018],marker="s",markersize=10) # sirius b 
ax1.plot([44.2],[1.5],marker="o",markerfacecolor='r',markeredgecolor='k',markersize=10,linewidth=0) # https://ja.wikipedia.org/wiki/アルデバラン

ax1.set_xlim(1e-6,1e+2)
ax1.set_ylim(1.5e-6,9)

#plt.grid()

SolarRadiusToKM = lambda SolarRadius:  SolarRadius * radius_of_Sun * 1e-5 
KMToSolarRadius = lambda km: km * 1e+5 / radius_of_Sun 

loc = mticker.LogLocator()
locs = loc.tick_values(*SolarRadiusToKM(np.array(ax1.get_xlim())))

ax2.set_xticks(KMToSolarRadius(locs))
ax2.set_xlim(ax1.get_xlim())

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.2e' % SolarRadiusToKM(x)))
fmt = mticker.FuncFormatter(g)
ax2.xaxis.set_major_formatter(mticker.FuncFormatter(fmt))

ax2.xaxis.set_tick_params(which='minor', top=False)

ax1.set_ylabel("Stellar Mass (Solar mass)",labelpad=14)
ax1.set_xlabel('Stellar Radius (Solar radius)',labelpad=14)
ax2.set_xlabel('Stellar Radius (km)',labelpad=14)

plt.tight_layout()
fig.patch.set_alpha(0.0)
ax1.patch.set_alpha(0.0)  
ax2.patch.set_alpha(0.0)  
fig.savefig("stars_mass_radius_solar.pdf")




