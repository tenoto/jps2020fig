#!/usr/bin/env python

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

mycolor_blue = "#2874A6"
mycolor_green = "#239B56"
mycolor_orange = "#AF601A"
mycolor_purple = "#8E44AD"

df = pd.read_csv('data/jps2020fig_NeutronStarMassRadius - Radius.csv')

plt.style.use('script/matplotlibrc.template')

fig = plt.figure(figsize=(7,12))
ax1 = fig.add_subplot(111)

num = 0
for index, row in df.iterrows():
	if row['Method'] == 'X-ray profile':
		ax1.errorbar([float(row['Radius (km)'])],[num],
			xerr=[[float(row["R minus error "])],[float(row["R plus error"])]],
			yerr=[[0.0],[0.0]],
			fmt='o',markersize=20.0,markeredgecolor='k',
			markerfacecolor='r',ecolor='r',linewidth=4)
		#ax1.text(8.2,num-0.2,"hoge",color='r',ha='left',fontsize=18)
	if row['Method'] == 'qLMXB in GC' and row['Radius (km)'] != '--':
		ax1.errorbar([float(row['Radius (km)'])],[num],
			xerr=[[float(row["R minus error "])],[float(row["R plus error"])]],
			yerr=[[0.0],[0.0]],
			fmt='o',markersize=20.0,markeredgecolor='k',
			markerfacecolor=mycolor_blue,ecolor=mycolor_blue,linewidth=4)	
	if row['Method'] == 'qLMXB in GC' and row['Radius (km)'] == '--':
		ax1.plot(
			[float(row["R minus error "]),float(row["R plus error"])],[num,num],
			color=mycolor_blue,linewidth=4)		
	if 'X-ray bursts' in row['Method'] and row['Radius (km)'] != '--':		
		ax1.errorbar([float(row['Radius (km)'])],[num],
			xerr=[[float(row["R minus error "])],[float(row["R plus error"])]],
			yerr=[[0.0],[0.0]],
			fmt='o',markersize=20.0,markeredgecolor='k',
			markerfacecolor=mycolor_green,ecolor=mycolor_green,linewidth=4)		
	if 'X-ray bursts' in row['Method'] and row['Radius (km)'] == '--':		
		ax1.plot(
			[float(row["R minus error "]),float(row["R plus error"])],[num,num],
			color=mycolor_green,linewidth=4)								
	if 'thermal emission' in row['Method'] and row['Radius (km)'] != '--':		
		ax1.errorbar([float(row['Radius (km)'])],[num],
			xerr=[[float(row["R minus error "])],[float(row["R plus error"])]],
			yerr=[[0.0],[0.0]],
			fmt='o',markersize=20.0,markeredgecolor='k',
			markerfacecolor=mycolor_orange,ecolor=mycolor_orange,linewidth=4)	
	if 'Gravitational wave' in row['Method'] and row['Radius (km)'] != '--':		
		ax1.errorbar([float(row['Radius (km)'])],[num],
			xerr=[[float(row["R minus error "])],[float(row["R plus error"])]],
			yerr=[[0.0],[0.0]],
			fmt='o',markersize=20.0,markeredgecolor='k',
			markerfacecolor=mycolor_purple,ecolor=mycolor_purple,linewidth=4)	
		#print(row)									
	print(row['Radius (km)'],num)
	num+=1

ax1.set_xlim(8,16)
ax1.set_ylim(-1,13)
ax1.set_xlabel('Stellar Radius (km)',labelpad=14)

plt.tight_layout()
fig.patch.set_alpha(0.0)
ax1.patch.set_alpha(0.0)  
fig.savefig("list_neutron_star_radius.pdf")



