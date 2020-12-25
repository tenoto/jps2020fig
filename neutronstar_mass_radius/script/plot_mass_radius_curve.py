#!/usr/bin/env python

import os
import glob
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

mr_dict = {}
for mrfile_path in glob.glob('data/compMR_wCrust/*'):
	print(mrfile_path)
	mrname, filetype = os.path.splitext(os.path.basename(mrfile_path))
	if filetype == '.eps':
		continue
	print(mrname)
	mr_dict[mrname] = pd.read_csv(mrfile_path,delim_whitespace=True,names=['Radius','Mass'],skiprows=1)

print(mr_dict)	

plt.style.use('script/matplotlibrc.template')

fig = plt.figure(figsize=(12,10))
ax1 = fig.add_subplot(111)

for mrname in mr_dict:
	print(mrname)
	ax1.plot(mr_dict[mrname]['Radius'],mr_dict[mrname]['Mass'])
ax1.set_xlim(8,16)
ax1.set_ylim(0,3)
ax1.set_xlabel('Radius (km)')
ax1.set_ylabel('Mass (Solar mass)')

plt.tight_layout()
fig.patch.set_alpha(0.0)
ax1.patch.set_alpha(0.0) 
fig.savefig("mass_radius_curve.pdf")
