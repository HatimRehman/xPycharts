from Tkinter import *
from math import *

x_coordinates = { }
y_coordinates = { }

def get_axes( window, markings, scale_x, scale_y ):
	canvas = Canvas(window, width=500, height=500)#, background='lightgrey',) # create a canvas to draw on (inside the window)

	canvas.pack() # no idea what this does

	canvas_height = int( canvas.cget("height") )
	canvas_width = int( canvas.cget("width") )

	# create line takes (x0, y0, x1, y1) and creates a line that joins the two points

	# create line from middle x top, to middle x bottom (the y axis)
	canvas.create_line(	canvas_width/8, 0,
						canvas_width/8, canvas_height*7/8
				)
	# create line from middle y & left side of the screen, to middle y right side of the screen (the x axis)
	canvas.create_line(	canvas_width/8, canvas_height*7/8,
						canvas_width, canvas_height*7/8,
				)

	_get_labels(canvas, markings, scale_x, scale_y)

	return canvas

# adds the labels to the axes
def _get_labels( canvas, markings, scale_x, scale_y ):#, scale, grid_points):

	canvas_height = int( canvas.cget("height") )
	canvas_width = int( canvas.cget("width") )

	xlabel_coordinates, ylabel_coordinates = [ ], [ ]

	x_offset = ( canvas_width/2 ) / markings
	y_offset = ( canvas_height/2 ) / markings


	for i in range(1,markings*2):
		xlabel_coordinates.extend([
			_get_translated_point({'x': i, 'y': 0}, x_offset, y_offset, canvas, scale_x, scale_y),

		])

		ylabel_coordinates.extend([
			_get_translated_point({'x': 0, 'y': i}, x_offset, y_offset, canvas, scale_x, scale_y),

		])

	for coord in xlabel_coordinates:
		canvas.create_horizontal_label(coord['x'], coord['y'], 5)

	for coord in ylabel_coordinates:
		canvas.create_vertical_label(coord['x'], coord['y'], 5)

# converts (x,y) to a point on the canvas' coordinate system
def _get_translated_point( coord, x_offset, y_offset, canvas, scale_x, scale_y ):

	canvas_height = int( canvas.cget("height") )
	canvas_width = int( canvas.cget("width") )

	x = canvas_width/8 + coord['x']*x_offset
	y = canvas_height*7/8 - coord['y']*y_offset

	x_coordinates[x] = coord['x']*scale_x
	y_coordinates[y] = coord['y']*scale_y

	return {'x': x,
			'y': y
		}

# create helper methods to add to Canvas object
def _create_horizontal_label(self, x, y, h, **kwargs):
	return self.create_line(x, y-h, x, y+h, **kwargs ) and self.create_text(x,y+15, text=x_coordinates[x])
Canvas.create_horizontal_label = _create_horizontal_label


def _create_vertical_label(self, x, y, w, **kwargs):
	return self.create_line(x-w, y, x+w, y, **kwargs ) and self.create_text(x+15,y, text=y_coordinates[y])
Canvas.create_vertical_label = _create_vertical_label


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle
