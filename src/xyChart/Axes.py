##
# Axes constructing script\n
# Author: Hatim Rehman\n
# This generic script draws axes on a Canvas object

from Tkinter import *
from math import *

x_coordinates = { }
y_coordinates = { }

## On a Canvas object, constructs X and Y axes appropriately placed. Returns a new canvas with this done.
# Vertical line: Start from the middle with respect to x, draw a line from top to bottom with respect to y.
# Horizontal line: Start from the middle with respect to y, draw a line from left to right with respect to x.
# Then calls _get_labels() to add the labels to the two lines.
#  @param window The window to draw on.
#  @param markings The number of labels to put on each axis.
#  @param scale_x The scale value to use on the x axis.
#  @param scale_y The scale value to use on the y axis.
def get_axes( window, markings, scale_x, scale_y ):
	canvas = Canvas(window, width=600, height=600)#, background='lightgrey',) # create a canvas to draw on (inside the window)

	canvas.pack() 

	canvas_height = int( canvas.cget("height") )
	canvas_width = int( canvas.cget("width") )

	# create line takes (x0, y0, x1, y1) and creates a line that joins the two points

	# create line from middle x top, to middle x bottom (the y axis)
	canvas.create_line(	canvas_width/2, 0,
					canvas_width/2, canvas_height,
					arrow= BOTH
				)
	# create line from middle y & left side of the screen, to middle y right side of the screen (the x axis)
	canvas.create_line(	0, canvas_height/2,
					canvas_width, canvas_height/2,
					arrow = BOTH
				)

	_get_labels(canvas, markings, scale_x, scale_y)

	return canvas

## On a Canvas object draws labels on where the x and y axis are placed (assumes so).
# Using _get_translated_point() finds where the markings should go (x, 0) and (0, y),
# then calls create_horizontal_label() for x coordinates and create_vertical_label() for y coordinates
#  @param canvas The canvas to draw on.
#  @param markings The number of labels to put on each axis.
#  @param scale_x The scale value to use on the x axis.
#  @param scale_y The scale value to use on the y axis.
def _get_labels( canvas, markings, scale_x, scale_y ):#, scale, grid_points):

	canvas_height = int( canvas.cget("height") )
	canvas_width = int( canvas.cget("width") )

	xlabel_coordinates, ylabel_coordinates = [ ], [ ]

	x_offset = ( canvas_width/2 ) / markings
	y_offset = ( canvas_height/2 ) / markings


	for i in range(1,markings):
		xlabel_coordinates.extend([
			_get_translated_point({'x': i, 'y': 0}, x_offset, y_offset, canvas, scale_x, scale_y),
			_get_translated_point({'x': -i, 'y': 0}, x_offset, y_offset, canvas, scale_x, scale_y),
		])

		ylabel_coordinates.extend([
			_get_translated_point({'x': 0, 'y': i}, x_offset, y_offset, canvas, scale_x, scale_y),
			_get_translated_point({'x': 0, 'y': -i}, x_offset, y_offset, canvas, scale_x, scale_y),
		])

	for coord in xlabel_coordinates:
		canvas.create_horizontal_label(coord['x'], coord['y'], 5)

	for coord in ylabel_coordinates:
		canvas.create_vertical_label(coord['x'], coord['y'], 5)

## Finds the coordinates of any (x,y) to (x2,y2) where x2, y2 are the new coordinates on the Canvas object with respect to the cartesian coordinate system.
#  Multiplies the x coordinate by the scale ratio on the cartesian system, then moves it half the screen length to the right.
#  Multiplies the y coordinate by the scale ratio on the cartesian system, then subtracts it from the height of the screen.
#  @param coord A dictionary with the format { 'x': <EM>value</EM>, 'y': <EM>value</EM> }
#  @param canvas The canvas to draw on.
#  @param markings The number of labels to put on each axis.
#  @param scale_x The scale value to use on the x axis.
#  @param scale_y The scale value to use on the y axis.
def _get_translated_point( coord, x_offset, y_offset, canvas, scale_x, scale_y ):

	canvas_height = int( canvas.cget("height") )
	canvas_width = int( canvas.cget("width") )

	x = canvas_width/2 + coord['x']*x_offset
	y = canvas_height/2 - coord['y']*y_offset

	x_coordinates[x] = coord['x']*scale_x
	y_coordinates[y] = coord['y']*scale_y

	return {'x': x,
			'y': y
		}

## Draws a label for the x axis (therefore vertical line) at x and y with height h
# The line starts at y-h and stops at y+h with respect to x
#  @param x The x coordinate
#  @param y The y coordinate
#  @param h The height of the line
#  @param kwargs Styling keyword arguments
def _create_horizontal_label(self, x, y, h, **kwargs):
	return self.create_line(x, y-h, x, y+h, **kwargs ) and self.create_text(x,y+15, text=x_coordinates[x])
Canvas.create_horizontal_label = _create_horizontal_label


## Draws a label for the y axis (therefore horizontal line) at x and y with width w
# The line starts at x-w and stops at x+w with respect to y
#  @param x The x coordinate
#  @param y The y coordinate
#  @param h The height of the line
#  @param kwargs Styling keyword arguments
def _create_vertical_label(self, x, y, w, **kwargs):
	return self.create_line(x-w, y, x+w, y, **kwargs ) and self.create_text(x+15,y, text=y_coordinates[y])
Canvas.create_vertical_label = _create_vertical_label

## Draws a circle representing a point on the canvas
#  @param x The x coordinate
#  @param y The y coordinate
#  @param r The radius of the point
#  @param kwargs Styling keyword arguments
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle
