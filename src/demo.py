from xPycharts import *


dataset =  [ (1, 1),  (2, 2), (3, 3), ( -17, -77) ]\
#dataset2 = [ (1,-1), (2,-1), (3,-2), (4,-3), (5,-5) ]

def func(x):
	return sin(x) * x


demo_graph = xy.Graph( 6)
demo_graph.plot_points(dataset, fill='blue' )



#demo_graph.plot_points_with_line( dataset2, fill='red')

#demo_graph = xy.Graph( 6 )
#demo_graph.plot_function( func )


mainloop()