# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from turtle import right
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas, scene_height, scene_width)
    draw_ground(canvas, scene_height, scene_width)

    cloud_height = 400
    cloud_width = 30
    for i in range(6):
        draw_cloud(canvas, cloud_height, cloud_width)
        cloud_width += 100
    
    draw_tree(canvas, 500)
    draw_tree(canvas, 650)

    fence_interval = 0
    for i in range(24):
        draw_fence(canvas, fence_interval)
        fence_interval += 25


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, height, weidth):
    draw_rectangle(canvas, 0 , height / 10, weidth, height, fill="blue4")

def draw_cloud(canvas, cloud_height, cloud_width):
    """
    Draw a cloud
    """
    draw_oval(canvas, cloud_width, cloud_height, cloud_width + 100, cloud_height + 30, fill="gray99", outline="")

def draw_ground(canvas, height, weidth):
    """Drawn the ground"""
    draw_rectangle(canvas, 0, height / 4 , weidth, 0, fill="sienna")


def draw_fence(canvas, interval = 0):
    """
    Draw a fence, but
    """
    fence_height = 75
    fence_width = 25 + interval

    draw_rectangle(canvas, fence_width, fence_height, fence_width + 20, fence_height + 100, fill="white", width=0)

def draw_tree(canvas, bottom):
    
    # Draw trunk
    trunk_height = 100
    trunk_width = bottom

    # Draw tree
    draw_rectangle(canvas, trunk_width, trunk_height, trunk_width + 30, trunk_height + 100, fill="brown", width=0)


    draw_polygon(canvas, trunk_width - 45 , 200, 60 + trunk_width, 200, 20 + trunk_width, 350, fill="green")

# Call the main function so that
# this program will start executing.
main()