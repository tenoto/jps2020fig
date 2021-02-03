#!/usr/bin/env python

import pandas as pd

#df = pd.read_excel('data/EOS.xlsx')

df = pd.read_excel('data/EOS.xlsx',engine='openpyxl',sheet_name=None,header=None,names=['density','n/a','pressure'])
print(df['SLY9'])
