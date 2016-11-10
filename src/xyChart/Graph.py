from Axes import *
from Scale import *
from InputParser import *

class Graph:

	def __init__(self, n , data = None):
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
		self.master.title("xPycharts")

		self.graph = get_axes( self.master, self.markings, self.scale_x,self.scale_y  ) #get an axis with this many markings

		self.graph_height = int( self.graph.cget("height") )
		self.graph_width = int( self.graph.cget("width") )

		self.x_offset = (( self.graph_width/2 ) / self.markings) / self.scale_x
		self.y_offset = (( self.graph_height/2 ) / self.markings) / self.scale_y
		
		if self.data is not None:
			self.plot_points(self.data, fill="blue")
			

	def plot_point(self, coord, **kwargs): #plots a coordinate, with stylings kwargs if they exist

		translated_coord = self._get_translated_point(coord) #converts (x,y) to a point on the canvas' coordinate system

		self.graph.create_circle(	translated_coord['x'],
									translated_coord['y'],
									4,
									**kwargs)
	
		# plots a list of points 
	def plot_points(self, data = None, **kwargs):
		try:
			self.data = clean_data(data)
		except:
			pass
			
		for coord in self.data:
			self.plot_point( coord, **kwargs )
	
	
	# plots a list of points and a polynomial that passes through all these points
	def plot_points_with_line(self, data, **kwargs):

		self.data = data = clean_data( data )

		self.dx = [d['x'] for d in data]
		self.dy = [d['y'] for d in data]

		
		dx_sorted = [d['x'] for d in data]; dx_sorted.sort()
		x_interval = [x / 100.0 for x in range(dx_sorted[0], dx_sorted[-1]*100,1)]

		self.plot_function(self._Lagrange, x_interval = [x / 100.0 for x in range(dx_sorted[0]*100, dx_sorted[-1]*100, 1)])
		
		for coord in data:
			self.plot_point( coord, **kwargs )
	
	
	def plot_function(self, func, x_interval = None, **kwargs): # plots a function, with styling kwargs if they exist
		
		x_interval = [x / 1000.0 for x in range(-Graph.markings*1000, Graph.markings*1000, 1)] if x_interval is None else x_interval
		
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


	# converts (x,y) to a point on the canvas' coordinate system
	def _get_translated_point(self, coord):

		x = self.graph_width/2  + coord['x']*self.x_offset
		y = self.graph_height/2 - coord['y']*self.y_offset

		x_coordinates[x] = coord['x']
		y_coordinates[y] = coord['y']

		return {'x': x,	'y': y }
	
	
	#Lagrange method for polynomial interpolation ( a polynomial of degree <= n that passes through n+1 points )			
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

	#Graph = Graph(6); Graph.plot_function( sin )

	Graph = Graph( 6 , [ (-4,4), (-2,1), (-1,1) , (1,1), (2,2), (4,5), (5,3) ]) 
	#Graph = Graph(6); Graph.plot_points_with_line( [ (-4,4), (-2,1), (-1,1) , (1,1), (2,2), (4,5), (5,3) ], fill = "blue" );

	mainloop() # runs window indefinitely
