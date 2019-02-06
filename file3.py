def tuple_required(filename):
	fin = open(filename,'r')
	for line in fin:
		line = line.split(",")
		tup = (line[2],line[4],line[6],line[7])
		print(tup)
    

fin = open('Street_Centrelines.csv','r')

print(tuple_required('Street_Centrelines.csv'))


