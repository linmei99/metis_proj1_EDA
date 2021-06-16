#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 25)
pd.set_option('display.precision', 3)

def proj1_clean(datafile):
	df=pd.read_csv(datafile)
	df['Ingress'] = pd.Series(0, index=df.index)
	df['Egress']= pd.Series(0, index=df.index)
	i,j,errcnt=1,0,0
	while i < len(df):
		# Same SCP and UNIT as previous row, find Ingress/Egress
		if( (df.iloc[i,1] == df.iloc[i-1,1]) &
			(df.iloc[i,2] == df.iloc[i-1,2])):
			#Ingress is the difference in Entries count between previous row.
			df.iloc[i,11] = df.iloc[i,9] - df.iloc[i-1,9]
			
			#Egress is the difference in Exit Count between previous row
			df.iloc[i,12] = df.iloc[i,10]-df.iloc[i-1,10]
			j += 1
			if df.iloc[i,3] != df.iloc[i-1,3]:
				print('Wrong Station')
				errcnt += 1
			
		elif j!= 41:
		# up to 6*7 data points per turnstile, if all data available in file		
			# missing data. Less than 42 rows of data in this week 
			print(f'less than  42 data points{j}')
			j = 0
			errcnt += 1
			
		#else case the default value of 0 is ok while
		# record starts for a different turnstile.
		else:
			j=0	
		i += 1
	return errcnt,df
			 

