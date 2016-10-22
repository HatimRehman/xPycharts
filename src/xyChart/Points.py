def clean_data(data):
	
	try:
		x=[ x[0] for x in data  ]
		y=[ y[1] for y in data  ]
	except:
		raise Exception("Inconsistent data")
		return
		
	mylist=[]

	checktype(x, y)
	
	for i in range (len(x)):
		d = {"x": x[i], "y": y[i]}
		mylist.append(d)
	return mylist

		

def checktype(x, y):
	for value in x:
		if type (value) != int and type (value) != float:
			raise Exception("Invalid input types in x")
	for value in y:
		if type (value) != int and type (value) != float:
			raise Exception("Invalid input types in y")
	checkT=True
	return





