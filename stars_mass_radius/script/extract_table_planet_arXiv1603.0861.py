#!/usr/bin/env python

mass_of_Sun = 1.99e+33 # g 
mass_of_Earth = 5.98e+27 #g
mass_of_Jupiter = 1.898e+30 # g
radius_of_Sun = 6.96e+10 # cm
radius_of_Earth = 6.38e+8 # cm
radius_of_Jupiter = 6.9911e+9 # cm

f = open('data/arXiv1603.0861_data_table.lst','w')
for line in open("data/arXiv1603.0861_data_table.tex"):
	cols = line.split('&')
	if cols[0][0] == '%':
		continue
	name = cols[0].replace('\t','')
	unit = cols[1].split('\\,')[-1]
	if 'msun' in unit:
		mass_in_solar_mass = float(cols[1].split('$')[1].split('\\pm')[0].replace('(',''))
		radius_in_solar_radius = float(cols[2].split('$')[1].split('\\pm')[0].replace('(',''))
		symbol = 'star'
	if 'Earth' in name:
		mass_in_solar_mass =  mass_of_Earth / mass_of_Sun
		radius_in_solar_radius = radius_of_Earth / radius_of_Sun
		symbol = 'solar_system'
	elif 'mearth' in unit:
		tmp_mass = float(cols[1].split('$')[1])
		mass_in_solar_mass = tmp_mass * mass_of_Earth / mass_of_Sun
		tmp_radius = float(cols[2].split('$')[1])
		radius_in_solar_radius = tmp_radius * radius_of_Earth / radius_of_Sun		
		symbol = 'solar_system'		
	if 'mjup' in unit:
		tmp_mass = float(cols[1].split('$')[1].split('\\pm')[0].replace('(',''))
		mass_in_solar_mass = tmp_mass * mass_of_Jupiter / mass_of_Sun
		tmp_radius =  float(cols[2].split('$')[1].split('\\pm')[0].replace('(',''))
		radius_in_solar_radius = tmp_radius * radius_of_Jupiter / radius_of_Sun		
		symbol = 'exoplanet'		
	dump = '%s,%.5e,%.5e,%s\n' % (name,mass_in_solar_mass,radius_in_solar_radius,symbol)
	f.write(dump)	
f.close()