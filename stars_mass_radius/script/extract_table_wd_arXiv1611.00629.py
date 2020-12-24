#!/usr/bin/env python

# https://arxiv.org/abs/1611.00629

f = open('data/arXiv1611.00629_data_table.lst','w')
for line in open('data/arXiv1611.00629_data_table.tex'):
	cols = line.split('&')
	if 'noalign' in cols[0]:
		continue
	if '...' in cols[1]:
		continue
	mass = float(cols[1].split('(')[0])
	radius = float(cols[2].split('(')[0])*0.01
	print('%.3f,%.6f' % (mass,radius))
	f.write('%.3f,%.6f\n' % (mass,radius))	
f.close()	