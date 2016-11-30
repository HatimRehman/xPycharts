from Axes import *
from Scale import *
from InputParser import *

##
# xyGraph constructing class\n
# Author: Hatim Rehman\n
# This class represents a graph object that can plot points with data contained
# within a list of tuples\n[ (x1, y1), (x2, y2), \...\ , (xn, yn) ]
#
class Graph:
    ## The constructor method
    # Takes in 3 parameters. 
    # Outputs a graph with plotted data that is entered as a parameter.
    #  @param self The object pointer.
    #  @param n The number of markings to appear on the x and y axes
    #  @param data The data to plot 
	def __init__(self, n , data = None, title= None):
		self.data = clean_data(data) if data is not None else None
		
		self.markings = (n+1) 
		
		if data is not None:
			self.scale = get_scale(self.data, round_to = self.markings-1)

			self.scale_x = self.scale[0] / float(n)
			self.scale_y = self.scale[1] / float(n)

		else:
			self.scale = [1,1] if self.data is None else get_scale(self.data, round_to = self.markings-1)

			self.scale_x = 1
			self.scale_y = 1

		self.master = Tk() 	#creates the window
		self.master.resizable(0,0) # turn off resizing
		if title is None:
			self.master.title("xPycharts")
		
		else: 
			self.master.title(title)
			
		self.graph = get_axes( self.master, self.markings, self.scale_x,self.scale_y  ) #get an axis with this many markings

		self.graph_height = int( self.graph.cget("height") )
		self.graph_width = int( self.graph.cget("width") )

		self.x_offset = (( self.graph_width/2 ) / self.markings) / self.scale_x
		self.y_offset = (( self.graph_height/2 ) / self.markings) / self.scale_y
		
		if self.data is not None:
			self.plot_points(self.data, fill="blue")
			
    ## Plot points method 
    # Takes in a coordinate to plot, with keyword args that may be used to style the coordinate.
    # Outputs a graph with the coord parameter plotted. 
    #  @param self The object pointer.
    #  @param coord A dictionary with the format { 'x': <EM>value</EM>, 'y': <EM>value</EM> } 
    #  @param kwargs Keyword arguments for Tkinter's create_circle() method 
	def plot_point(self, coord, **kwargs): #plots a coordinate, with stylings kwargs if they exist

		translated_coord = self._get_translated_point(coord) #converts (x,y) to a point on the canvas' coordinate system

		self.graph.create_circle(	translated_coord['x'],
									translated_coord['y'],
									4,
									**kwargs)
	
    ## Plot points method 
    # takes in multiple coordinates and calls the plot_point() method from its own API on each method.
    # Outputs a graph with the data parameter plotted. 
    #  @param self The object pointer.
    #  @param data A list of tuples [ (x1, y1), (x2, y2), \...\ , (xn, yn) ]
    #  @param kwargs Keyword arguments for Tkinter's create_circle() method  
	def plot_points(self, data = None, **kwargs):
		try:
			self.data = clean_data(data)
		except:
			pass
			
		for coord in self.data:
			self.plot_point( coord, **kwargs )
	
	
    ## Plot points with line method 
    # takes in multiple coordinates and calls the plot_point() method from its own API on each method. Then
    # calls its private function generating method that creates a polynomial that passes through each point using
    # the Lagrange polynomial interpolation theorem.
    #  Outputs a graph with the data parameter plotted. 
    #  @param self The object pointer.
    #  @param data A list of tuples [ (x1, y1), (x2, y2), \...\ , (xn, yn) ]
    #  @param kwargs Keyword arguments for Tkinter's create_circle() method  
	def plot_points_with_line(self, data, **kwargs):
		
#		if self.data is None:
#			self.master.destroy()			
#			self.__init__(self.markings-1, data)
			
		self.data =  clean_data( data )

		self.dx = [d['x'] for d in self.data]
		self.dy = [d['y'] for d in self.data]

		
		dx_sorted = [d['x'] for d in self.data]; dx_sorted.sort()
		x_interval = [x / 1000.0 for x in range(dx_sorted[0], dx_sorted[-1]*1000,1)]

		if is_function(data):
			self.plot_function(self._Lagrange, x_interval = [x / 100.0 for x in range(dx_sorted[0]*100, dx_sorted[-1]*100, 1)])
		
		for coord in self.data:
			self.plot_point( coord, **kwargs )
	
	## Plots a python function onto the graph
    #  Outputs a graph with the func parameter plotted
    #  @param self The object pointer.
    #  @param func A python function that takes in a double value and returns a double value
    #  @param x_interval A  list of double values that the function should pass through [ x1, \...\, xn ]
    #  @param kwargs Keyword arguments for Tkinter's create_circle() method  
	def plot_function(self, func, x_interval = None, **kwargs): # plots a function, with styling kwargs if they exist
		
		x_interval = [x / 1000.0 for x in range(-self.markings*1000, self.markings*1000, 1)] if x_interval is None else x_interval
		
		coords = [ ]

		for x in x_interval: #computes the y value for each x in the x axis at 100th of the precision (i.e x=0.01, x= 0.02, ... x=markings)

			# add (x, f(x)) and (-x, f(-x)) to the list of coordinates
			coords.append(	coord(x, func(x)) )

		for xy in coords:
			# convert coordinate to canvas' coordinate system
			translated_coord = self._get_translated_point(xy)

			# plot it with a radius of 0.5
			self.graph.create_circle(	translated_coord['x'],
										translated_coord['y'],
										0.5,
										**kwargs)

	## Finds the coordinates of any (x,y) to (x2,y2) where x2, y2 are the new coordinates on the Canvas object with respect to the cartesian coordinate system.
	#  Multiplies the x coordinate by the scale ratio on the cartesian system, then moves it half the screen length to the right.
	#  Multiplies the y coordinate by the scale ratio on the cartesian system, then subtracts it from the height of the screen.
    #  @param self The object pointer.
    #  @param coord A dictionary with the format { 'x': <EM>value</EM>, 'y': <EM>value</EM> }
	def _get_translated_point(self, coord):

		x = self.graph_width/2  + coord['x']*self.x_offset
		y = self.graph_height/2 - coord['y']*self.y_offset

		x_coordinates[x] = coord['x']
		y_coordinates[y] = coord['y']

		return {'x': x,	'y': y }
	
	
	## Finds the lagrange polynomial on a value x, constructing the polynomial with the current dataset. Returns the new value y.
    #  @param self The object pointer.
    #  @param x A double value representing an x coordate
	def _Lagrange(self, x):
		
		dx = self.dx		
		def b(xi):
			z = 1.0
			for k in range(0,len(dx)+1):
					try:
						z *= (x-dx[k]) / (xi-dx[k])
					except:
						pass
			return z

		y = 0 
		for coord in self.data:
				xi, yi = coord['x'], coord['y']
				y += yi*b(xi)
		
		return y
		
# returns a dictionary to be used in the API
def coord(x,y):
	return {'x': x, 'y': y}

if __name__ == '__main__':

	#Graph = Graph(6, [ (1,1 ), (2,4 ), ( -3, -6), (7, -12 )  ])
#	Graph = Graph(1); Graph.plot_function( sin )

	Graph = Graph( 6 , [ (-4,4), (-2,1), (-1,1) , (1,1), (2,2), (4,5), (5,33) ], "Relation between x and y") 
	Graph.plot_points_with_line( [ (-4,6), (-3,-6), (-1,11) , (1,14), (2,22), (4,25), (5,13) ], fill = "red" );
	Graph.plot_points_with_line( [ (-4,4), (-2,1), (-1,1) , (1,1), (2,2), (4,5), (5,33) ], fill = "blue" );
	
	mainloop() # runs window indefinitely
