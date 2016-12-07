#!/usr/bin/env python3

import pandas as pd
import numpy as np

def prodsale(season):
	sItem={}
	qItem={}
	show=20
	count=0
	
	for i in range(len(season.PROD_NBR)):
		prod = (season['PROD_NBR']).iloc[i]
		qty = (season['SLS_QTY']).iloc[i]
		pos = (season['POS_AMT']).iloc[i]
		if prod in sItem:
			qItem[prod] = qItem[prod] + qty
			sItem[prod] = sItem[prod] + pos
		else:
			qItem[prod] = qty
			sItem[prod] = pos
			
	print("{:25} {:>6} {:>6}".format("Product Number","Gross Income","Qty"))
	for i in sorted(sItem, key=sItem.get, reverse=True):
		value = sItem[i]
		quant = qItem[i]
		print("{:25} {:6.2f} {:>10}".format(i, value, quant))
		count=count+1
		if(count>show):
			break

def zipSale(season):
	sItem={}
	
	for i in range(len(season['3_ZIP'])):
		zipcode = (season['3_ZIP']).iloc[i]
		pos = (season['EXT_SLS_AMT']).iloc[i]
		if zipcode in sItem:
			sItem[zipcode] = sItem[zipcode] + pos
		else:
			sItem[zipcode] = pos
	return sItem