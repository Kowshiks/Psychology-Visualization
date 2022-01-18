from __future__ import division

from psychopy import visual, event, core
from psychopy.tools.coordinatetools import pol2cart
import numpy
import time

def value_init():

    tatal_dots = 1000
    maximum_speed = 0.03
    dots_size = .008

    # Define the X range to be any value to cover 360 degrees of the window
    x_range = numpy.random.rand(tatal_dots) * 360

    # The radius of each dot from the centre is defined through a normal distribution
    radius = (numpy.random.rand(tatal_dots) ** 0.5) * 2

    # The speed of all the dots are also defined through a normal distribution by limiting it to the maximum speed
    speed = numpy.random.rand(tatal_dots) * maximum_speed

    # Initialise the window ratio
    window = visual.Window([1000, 800], color=[-1, -1, -1])


    dots = visual.ElementArrayStim(window, elementTex='sin', elementMask='circle',
        nElements=tatal_dots, sizes=dots_size)

    
    return x_range,radius,speed,window,dots


x_range,radius,speed,window,dots = value_init()

timeout = time.time() + 10

# For the dots to move outwards

while True:

    # The radius of the dots keeps on increasing with respect ti the speed
    radius = radius + speed

    # If the readius of dots are greater than 2.0 then bring the radius back to the initial center frame
    outFieldDots = (radius >= 2.0)
    radius[outFieldDots] = numpy.random.rand(sum(outFieldDots)) * 2.0

    # Change the numpy values to cartesian values
    X, Y = pol2cart(x_range, radius)
    X *=  0.75  # to account for wider aspect ratio
    dots.xys = numpy.array([X, Y]).T   # Changing 2xN to Nx2
    dots.draw()

    window.flip()

    # Close the window after 5 secs
    if time.time() > timeout:
        break

window.close()

x_range,radius,speed,window,dots = value_init()

timeout = time.time() + 10

# For the dots to move inwards

while True:
    
    # Since we want to make the dots to go inside we are subtracting the radius with the speed
    radius = radius - speed


    # Once the dots reaches the centre that particular index of outFieldDots becomes False
    outFieldDots = (radius <= 0.0)
    
    # Again we are initialising that particular index to a broader index by assigning a higher value
    radius[outFieldDots] = 2.0

    X, Y = pol2cart(x_range, radius)
    X *=  0.75  # to account for wider aspect ratio

    
    dots.xys = numpy.array([X, Y]).T
    dots.draw()

    window.flip()

    # Close the window after 5 sec
    if time.time() > timeout:
        break

window.close()
core.quit()

