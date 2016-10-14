from Axes import *

class Graph:

	def __init__(self, n):

		self.markings = n+1 # markings makes [0, n+1) markings
		self.scale = 1
		self.master = Tk() 	#creates the window
		self.master.resizable(0,0) # turn off resizing
		self.master.title("xPycharts")

		self.graph = get_axes( self.master, self.markings ) #get an axis with this many markings

		self.graph_height = int( self.graph.cget("height") )
		self.graph_width = int( self.graph.cget("width") )

		self.x_offset = ( self.graph_width/2 ) / self.markings
		self.y_offset = ( self.graph_height/2 ) / self.markings

	def plot_point(self, coord, **kwargs): #plots a coordinate, with stylings kwargs if they exist

		translated_coord = self._get_translated_point(coord) #converts (x,y) to a point on the canvas' coordinate system

		self.graph.create_circle(	translated_coord['x'],
									translated_coord['y'],
									4,
									**kwargs)
	
		# plots a list of points 
	def plot_points(self, data, **kwargs):		
		for coord in data:
			self.plot_point( coord, **kwargs )
	
	
	# plots a list of points and a polynomial that passes through all these points
	def plot_points_with_line(self, data, **kwargs):
	
		self.dx = [d['x'] for d in data]
		self.dy = [d['y'] for d in data]
		self.data = data
				
		self.plot_function(self._Lagrange)
		
		for coord in data:
			self.plot_point( coord, **kwargs )
	
	
	def plot_function(self, func, **kwargs): # plots a function, with styling kwargs if they exist

		coords = [ ]

		for x in [x / 100.0 for x in range(1, Graph.markings*100, 1)]: #computes the y value for each x in the x axis at 100th of the precision (i.e x=0.01, x= 0.02, ... x=markings)

			# add (x, f(x)) and (-x, f(-x)) to the list of coordinates
			coords.extend([	coord(x, func(x)),
							coord(-x, func(-x))
						])

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

	Graph = Graph(6)

	#Graph.plot_function( sin )

	Graph.plot_points_with_line( [	coord(1,1), coord(2,2), coord(4,5), coord(5,7) ], fill="green"), 
	
	mainloop() # runs window indefinitely
