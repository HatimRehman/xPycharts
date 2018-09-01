from xPycharts import *


# dataset =  [ (float("-inf"), float("-inf")),  (float("inf"), float("inf")) ]\
dataset = [ (1,-1), (2,-1), (3,-2), (4,-3), (5,-5) ]

def func(x):
	return sin(x) * x


demo_graph = xy.Graph( 6, dataset)
#demo_graph.plot_points(dataset, fill='blue' )



#demo_graph.plot_points_with_line( dataset2, fill='red')

#demo_graph = xy.Graph( 6 )
#demo_graph.plot_function( func )


mainloop()
