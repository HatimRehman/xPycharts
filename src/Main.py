from xPycharts import *
from math import *

#test = xy.Graph( 6 , [ (-4,4), (-2,1), (-1,1) , (1,1), (2,2), (4,5), (5,33) ], "Relation between x and y") 
#test.plot_points_with_line([ (2,2), (3,3) ] )
#test = xy.Graph(6)
#test.plot_function( sin , outline='blue')
#colors = ['red', 'white', 'blue']
#data = [("five percent", 5) , ("ten percent", 10), ("85 percent", 10)]
#pie.PieChart(data, colors)

def func( x ):
	return sin(x)+x
	
	
demo_graph = xy.Graph( 6 );

#demo_graph.plot_points_with_line( [ (1, 2), (2, 4), (-1, 6), (4, 3)  ], fill='blue')

demo_graph.plot_function( func )



	
	
mainloop()