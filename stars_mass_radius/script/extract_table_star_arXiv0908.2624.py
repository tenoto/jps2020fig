#!/usr/bin/env python

# https://arxiv.org/abs/0908.2624

f = open('data/arXiv0908.2624_data_table.lst','w')
for line in open('data/arXiv0908.2624_data_table.tex'):
	cols = line.split('&')
	if 'noalign' in cols[0]:
		continue
	col_mass = float(cols[5].split('\\pppp')[0])
	col_radius = float(cols[6].split('\\pppp')[0])
	print(col_mass,col_radius)
	f.write('%.3f,%.3f\n' % (col_mass,col_radius))
f.close()	