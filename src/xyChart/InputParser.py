## This function breaks apart the user input and assigns the coordinate pairs to a dictionary (data structure).
##If there are inconsistencies in the user input (for example a missing y value)the function prints an exception message.\n
# Author: Sarthak Desai\n
#@param data is the list of co-ordinate pairs inputted by the user.
#
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
	print mylist
	return mylist

		
## This function checks if the data input type is correct(i.e. integers or floats).
#If data type is not correct function outputs an exception message.\n
# Author: Sarthak Desai\n
#@param x is a list of x values from all the co-ordinate pairs.
#@param y is a list of y values from all the co-ordinate pairs.
#
def checktype(x, y):
	for value in x:
		if type (value) != int and type (value) != float:
			raise Exception("Invalid input types in x")
	for value in y:
		if type (value) != int and type (value) != float:
			raise Exception("Invalid input types in y")
	checkT=True
	return





