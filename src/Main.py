from xPycharts import *


xy.Graph( 6 , [ (-4,4), (-2,1), (-1,1) , (1,1), (2,2), (4,5), (5,33) ], "Relation between x and y") 

colors = ['red', 'white', 'blue']
data = [("five percent", 5) , ("ten percent", 10), ("85 percent", 10)]
pie.PieChart(data, colors)


mainloop()