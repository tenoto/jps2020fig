#!/usr/bin/env python

import os
import glob
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def cm2inch(*tupl):
	inch = 2.54
	if isinstance(tupl[0], tuple):
		return tuple(i/inch for i in tupl[0])
	else:
		return tuple(i/inch for i in tupl)

mr_model_list = [
	'APR',
	'BL',	
#	'CMF',	
#	'DD2_FRG2f',		
	'DD2_FRG3f',
	'SKa',	
	'SLY9',	
	'SLY230a',
	'QHC18',	
	'QHC19-A',	
	'QHC19-B',	
	'QHC19-C',	
	'QHC19-D'
	]

##############
# MAIN
##############

# ------ Density vs. Pressure ------

#df_rhoP = pd.read_excel('data/EOS.xlsx',engine='openpyxl',
df_rhoP = pd.read_excel('data/EOS_v210221.xlsx',engine='openpyxl',
	sheet_name=None,header=None,names=['density','n/a','pressure','n/a','energy_density'])
df_rhoP['SLY230a'] = df_rhoP['SLY230a'].drop(index=0) # this sheet the header line 
del df_rhoP['Sheet13'] # this is null ssheet

df_Raai = pd.read_csv('data/Raaijmakers/fig2/wpd_datasets_mod.csv')
#Raai_core_x = 10**df_Raai['core-X'].dropna()/2.7e+14*0.17
Raai_core_x = 10**df_Raai['core-X'].dropna()*5.609e-13 
# ρ0 = 0.17 fm-3 = 2.7e+14 g/cm3
# fm = 1e-13 cm
# cm = 1e+13 fm
# for electron:
#	0.511 MeV <--> 9.109383701e-31 kg <--> 9.109383701e-28 g 
# g/cm3 = 0.511 MeV/9.109e-28 / (1e+13 fm)^3
#       = 0.05609 MeV * 1e-11 fm-3 
#       = 5.609e-13 MeV fm-3
Raai_core_y = 10**df_Raai['core-Y'].dropna()/1.60e+33
# MeV / fm3 = 1.60e+33 dyne/cm2 (http://asphwww.ph.noda.tus.ac.jp/myn/guide.pdf)

df_Raai_cont = pd.read_csv('data/Raaijmakers/fig2/wpd_datasets_Raaijmakers_fig2_leftupper.csv')
Raai_cont_x = 10**df_Raai_cont['X'].dropna()*5.609e-13 
Raai_cont_y = 10**df_Raai_cont['Y'].dropna()/1.60e+33

plt.style.use('script/matplotlibrc.template')
# For guidance, Nature's standard figure sizes are 89 mm wide (single column) and 183 mm wide (double column). 
# The full depth of a Nature page is 247 mm. Figures can also be a column-and-a-half where necessary (120–136 mm).

fig = plt.figure(figsize=cm2inch(22.0,17.0))
ax1 = fig.add_subplot(111)
#ax1.ticklabel_format(style='plain',axis='x',useOffset=False,scilimits=(0,0))
#ax1.xaxis.set_major_formatter(mticker.ScalarFormatter())

zorder = 0
#ax1.axvline(x=0.16,ls='--',color="#F39C12",zorder=zorder);zorder+=1

for sheet_name in mr_model_list:
	print(sheet_name)
	ax1.plot(df_rhoP[sheet_name]['energy_density'],df_rhoP[sheet_name]['pressure'],
		label=sheet_name,zorder=zorder)
	zorder+=1 

ax1.plot(Raai_core_x,Raai_core_y,'-')
ax1.plot(Raai_cont_x,Raai_cont_y,'--k')

#ax1.set_xlim(0.01,0.18)
#ax1.set_ylim(0.01,2.0)
ax1.set_xlim(50,1000)
ax1.set_ylim(0.5,500.0)
ax1.set_xlabel('Total energy density (MeV fm$^{-3}$)')
ax1.set_ylabel('Pressure (MeV fm$^{-3}$)')
ax1.legend(loc='upper left',borderaxespad=1,fontsize=10,ncol=2)

plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
fig.patch.set_alpha(0.0)
ax1.patch.set_alpha(0.0) 
fig.savefig("neutron_star_pressure_density.pdf")

# ------ Mass vs. Radius ------

mr_dict = {}
for mr_model in mr_model_list:
	mr_file = 'data/compEOS/%s.mr' % mr_model
	mr_dict[mr_model] = pd.read_csv(mr_file,delim_whitespace=True,
		names=['Radius','Mass'],skiprows=1)
print(mr_dict)	

plt.style.use('script/matplotlibrc.template')

# For guidance, Nature's standard figure sizes are 89 mm wide (single column) and 183 mm wide (double column). 
# The full depth of a Nature page is 247 mm. Figures can also be a column-and-a-half where necessary (120–136 mm).

#fig = plt.figure(figsize=cm2inch(12.8, 9.6))
#fig = plt.figure(figsize=cm2inch(21.0,14.8))
fig = plt.figure(figsize=cm2inch(22.0,17.0))
ax1 = fig.add_subplot(111)

xx = np.linspace(8,16)
yy = 2 / 2.83 / 3 * xx
ax1.plot(xx,yy,color='k',linestyle='--')

zorder = 1
for mrname in mr_dict:
	print(mrname)
	ax1.plot(mr_dict[mrname]['Radius'],mr_dict[mrname]['Mass'],label=mrname,zorder=zorder)
	zorder+=1
ax1.set_xlim(8,16)
ax1.set_ylim(0,3)
ax1.set_xlabel('Radius (km)')
ax1.set_ylabel('Mass (Solar mass)')

# https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.120.172702 
# R<13.76 km for 1.4 Msun
ax1.errorbar(13.76, 1.4,xerr=[2.0],yerr=[0.07],xuplims=[True],marker='',linestyle='-',color='#717D7E',linewidth=2,zorder=zorder);zorder+=1

# https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.120.172702 
# R<13.76 km for 1.4 Msun
ax1.errorbar(10.68, 1.6,xerr=[2.0],yerr=[0.07],xlolims=[True],marker='',linestyle='-',color='#717D7E',linewidth=2,zorder=zorder);zorder+=1

# https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.120.172702 
# R<13.76 km for 1.4 Msun
ax1.errorbar(12.25, 0.5,xerr=[2.0],yerr=[0.07],xlolims=[True],marker='',linestyle='-',color='#717D7E',linewidth=2,zorder=zorder);zorder+=1

# University of Maryland
#.errorbar([13.02],[1.44],xerr=[1.06,1.24],yerr=[0.14,0.15])
ax1.errorbar([13.02],[1.44],xerr=[[1.06],[1.24]],yerr=[[0.14],[0.15]],zorder=zorder,
	fmt='o',markersize=10,ecolor='r',markeredgecolor="black",linewidth=2,color='r')
zorder+=1 

# Demorest 2010, J1614-2230, 1.97+/-0.04 Msun
ax1.axhline(y=2.01,color="#F39C12",zorder=zorder);zorder+=1
ax1.axhline(y=1.93,color="#F39C12",zorder=zorder);zorder+=1


ax1.legend(loc='lower left',borderaxespad=1,fontsize=10,ncol=2)

plt.tight_layout()
fig.patch.set_alpha(0.0)
ax1.patch.set_alpha(0.0) 
fig.savefig("neutron_star_mass_radius.pdf")
