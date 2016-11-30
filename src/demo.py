from xPycharts import *

demo_graph = xy.Graph(6);

#demo_graph.plot_function( sin )

#demo_graph.plot_points_with_line( [ (1,1), (2,1), (3,3) ], fill='blue')

demo_graph.plot_points_with_line( [ (1,1), 
									(2,1), 
									(3,2), 
									(4,3), 
									(5,5),
									(6,8),
									(7,21) ], fill='red')
#demo_graph.plot_points( [ (2,1), (3,1), (4,3) ], fill='blue')

mainloop()