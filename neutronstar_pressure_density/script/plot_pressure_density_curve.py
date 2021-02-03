#!/usr/bin/env python

import os
import glob
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

df = pd.read_excel('data/EOS.xlsx',engine='openpyxl',sheet_name=None,header=None,names=['density','n/a','pressure'])
print(df['SLY9'])
print(df.keys())

def cm2inch(*tupl):
	inch = 2.54
	if isinstance(tupl[0], tuple):
		return tuple(i/inch for i in tupl[0])
	else:
		return tuple(i/inch for i in tupl)

plt.style.use('script/matplotlibrc.template')
# For guidance, Nature's standard figure sizes are 89 mm wide (single column) and 183 mm wide (double column). 
# The full depth of a Nature page is 247 mm. Figures can also be a column-and-a-half where necessary (120–136 mm).

#fig = plt.figure(figsize=cm2inch(12.8, 9.6))
#fig = plt.figure(figsize=cm2inch(21.0,14.8))
fig = plt.figure(figsize=cm2inch(22.0,17.0))
ax1 = fig.add_subplot(111)

#ax1.plot(df['SLY9']['density'],df['SLY9']['pressure'])

for sheet_name in df.keys():
	if sheet_name in ['SLY230a','Sheet13']:
		continue
	ax1.plot(df[sheet_name]['density'],df[sheet_name]['pressure'])

ax1.set_xlim(1e-4,1.0)
ax1.set_ylim(1e-4,70)
ax1.set_xlabel('Baryon number density (fm$^{-3}$)')
ax1.set_ylabel('Pressure (MeV fm$^{-3}$)')

#plt.xscale('log')
#plt.yscale('log')
plt.tight_layout()
fig.patch.set_alpha(0.0)
ax1.patch.set_alpha(0.0) 
fig.savefig("pressure_density.pdf")

"""

mr_dict = {}
for mrfile_path in glob.glob('data/compMR_wCrust/*'):
	print(mrfile_path)
	mrname, filetype = os.path.splitext(os.path.basename(mrfile_path))
	if filetype == '.eps':
		continue
	print(mrname)
	mr_dict[mrname] = pd.read_csv(mrfile_path,delim_whitespace=True,names=['Radius','Mass'],skiprows=1)

print(mr_dict)	

xx = np.linspace(8,16)
yy = 2 / 2.83 / 3 * xx
ax1.plot(xx,yy,color='k',linestyle='--')

zorder = 1
for mrname in mr_dict:
	print(mrname)
	ax1.plot(mr_dict[mrname]['Radius'],mr_dict[mrname]['Mass'],label=mrname,zorder=zorder)
	zorder+=1


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


ax1.legend(loc='lower left',borderaxespad=1,fontsize=8,ncol=2)

"""
