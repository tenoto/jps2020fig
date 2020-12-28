#!/usr/bin/env python

import math
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

mycolor_blue = "#2874A6"
mycolor_green = "#239B56"
mycolor_orange = "#AF601A"
mycolor_purple = "#8E44AD"


plt.style.use('script/matplotlibrc.template')

fig = plt.figure(figsize=(7,12))
ax1 = fig.add_subplot(111)

num = 0
target = None

df_lmxb = pd.read_csv('data/jps2020fig_NeutronStarMassRadius - Mass_LMXB_Ozel.csv')
for index, row in df_lmxb.iterrows():
	#if row['Target'] == '4U 1700-377' or row['Target'] == 'B1957+20':
	#	continue
	target = row['Target']
	ax1.errorbar([float(row['Mass (Msun)'])],[num],
		xerr=[[float(row["M minus error"])],[float(row["M plus error"])]],
		yerr=[[0.0],[0.0]],
		fmt='o',markersize=20.0,markeredgecolor='k',
		markerfacecolor=mycolor_orange,ecolor=mycolor_orange,linewidth=4)
	ax1.text(2.5,num,target,family='serif',size=12.0,ha='right', wrap=True,color=mycolor_orange)
	num+=1

df_hmxb = pd.read_csv('data/jps2020fig_NeutronStarMassRadius - Mass_HMXB_Ozel.csv')
for index, row in df_hmxb.iterrows():
	#if row['Target'] == '4U 1700-377' or row['Target'] == 'B1957+20':
	#	continue
	target = row['Target']
	ax1.errorbar([float(row['Mass (Msun)'])],[num],
		xerr=[[float(row["M minus error"])],[float(row["M plus error"])]],
		yerr=[[0.0],[0.0]],
		fmt='o',markersize=20.0,markeredgecolor='k',
		markerfacecolor=mycolor_blue,ecolor=mycolor_blue,linewidth=4)
	ax1.text(2.5,num,target,family='serif',size=12.0,ha='right', wrap=True,color=mycolor_blue)
	num+=1

df = pd.read_csv('data/jps2020fig_NeutronStarMassRadius - Mass_DNS.csv')
for index, row in df.iterrows():
	print(row['Target'])
	print(len(str(row['Target'])))
	if str(row['Target']) != 'nan':
		target = row['Target']
	if row['Mass (Msun)'] == '--':
		continue
	ax1.errorbar([float(row['Mass (Msun)'])],[num],
		xerr=[[float(row["M minus error"])],[float(row["M plus error"])]],
		yerr=[[0.0],[0.0]],
		fmt='o',markersize=20.0,markeredgecolor='k',
		markerfacecolor='r',ecolor='r',linewidth=4)
	ax1.text(2.5,num,target,family='serif',size=12.0,ha='right', wrap=True,color='r')
	num+=1


ax1.set_xlim(0.7,2.6)
#ax1.set_ylim(-1,13)
ax1.set_xlabel('Stellar Mass (Solar mass)',labelpad=14)

plt.tight_layout()
fig.patch.set_alpha(0.0)
ax1.patch.set_alpha(0.0)  
fig.savefig("list_neutron_star_mass_dns.pdf")





fig = plt.figure(figsize=(7,12))
ax1 = fig.add_subplot(111)

num = 0
target = None

df_nswd = pd.read_csv('data/jps2020fig_NeutronStarMassRadius - Mass_NSWD.csv')
for index, row in df_nswd.iterrows():
	if row['Target'] == 'J1748-2021B':
		continue
	target = row['Target']
	ax1.errorbar([float(row['Mass (Msun)'])],[num],
		xerr=[[float(row["M minus error"])],[float(row["M plus error"])]],
		yerr=[[0.0],[0.0]],
		fmt='o',markersize=20.0,markeredgecolor='k',
		markerfacecolor=mycolor_purple,ecolor=mycolor_purple,linewidth=4)
	ax1.text(2.5,num,target,family='serif',size=12.0,ha='right', wrap=True,color=mycolor_purple)
	num+=1

"""
df = pd.read_csv('data/jps2020fig_NeutronStarMassRadius - Mass_DNS.csv')
for index, row in df.iterrows():
	print(row['Target'])
	print(len(str(row['Target'])))
	if str(row['Target']) != 'nan':
		target = row['Target']
	if row['Mass (Msun)'] == '--':
		continue
	ax1.errorbar([float(row['Mass (Msun)'])],[num],
		xerr=[[float(row["M minus error"])],[float(row["M plus error"])]],
		yerr=[[0.0],[0.0]],
		fmt='o',markersize=20.0,markeredgecolor='k',
		markerfacecolor='r',ecolor='r',linewidth=4)
	ax1.text(2.5,num,target,family='serif',size=12.0,ha='right', wrap=True,color='r')
	num+=1
"""
ax1.set_xlim(0.7,2.6)
#ax1.set_ylim(-1,13)
ax1.set_xlabel('Stellar Mass (Solar mass)',labelpad=14)

plt.tight_layout()
fig.patch.set_alpha(0.0)
ax1.patch.set_alpha(0.0)  
fig.savefig("list_neutron_star_mass_nswd.pdf")

