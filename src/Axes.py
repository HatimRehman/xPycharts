from Tkinter import *

master = Tk() #creates the window 
master.resizable(0,0) # turn off resizing
master.title("xPycharts") #rename the title 


w = Canvas(master, width=500, height=500)#, background='lightgrey',) # create a canvas to draw on (inside the window)


w.pack() # no idea what this does


canvas_height = int( w.cget("height") ) 
canvas_width = int( w.cget("width") )

# create line takes (x0, y0, x1, y1) and creates a line that joins the two points

# create line from middle x top, to middle x bottom (the y axis)
w.create_line(	canvas_width/2, 0, 
				canvas_width/2, canvas_height, 
				arrow= BOTH
			)
# create line from middle y & left side of the screen, to middle y right side of the screen (the x axis)
w.create_line(	0, canvas_height/2, 
				canvas_width, canvas_height/2, 
				arrow = BOTH
			)


#master.configure(background='lightgrey')
mainloop() # runs window indefinitely

#	Sarthak: 	Reading data + validating it
#	Louis:		Best scale from data
#	Hatim:		Markings