#Take in CSV file
f = open('AlexionPOSTTrans(Big).csv','r') #opens CSV file in read mode 
print(f) #prints file name
for line in f:
	print(line);
