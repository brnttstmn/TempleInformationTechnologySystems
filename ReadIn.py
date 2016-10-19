#Take in CSV file
f = open('AlexionDataSet(WithDataSetMaster).xlsx','r') #opens CSV file in read mode 
print(f) #prints file name
for line in f:
	print(line);