def clean_data(data):
	
	try:
		name=[ x[0] for x in data  ]
		number=[ y[1] for y in data  ]
	except:
		raise Exception("Inconsistent data")
		return
	total =  float(sum(number))
        
	mylist=[]

	checktype(name, number)
	
	for i in range (len(x)):
		d = {"name": name[i], "fraction": number[i]/total}
		mylist.append(d)
	print mylist
	return mylist

		

def checktype(x, y, data):
	for value in name:
		if type (value) != str:
			raise Exception("Invalid input types in x")
	for value in number:
		if type (value) != int and type (value) != float:
			raise Exception("Invalid input types in y")
	checkT=True
	return





