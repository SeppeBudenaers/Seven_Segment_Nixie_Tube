import time
from neopixel import Neopixel

numpix = 6  # Number of NeoPixels corresponding to the segments of a digit
brightness = 50
# Pin where NeoPixels are connected

def display_digit(digit, strip, colors,segment):
    # Define the segments for each digit
    segments = {
        0: [1, 1, 1, 1, 1, 1, 0, 0, 0],
        1: [0, 1, 1, 0, 0, 0, 0, 0, 0],
        2: [1, 1, 0, 1, 1, 0, 1, 0, 0],
        3: [1, 1, 1, 1, 0, 0, 1, 0, 0],
        4: [0, 1, 1, 0, 0, 1, 1, 0, 0],
        5: [1, 0, 1, 1, 0, 1, 1, 0, 0],
        6: [1, 0, 1, 1, 1, 1, 1, 0, 0],
        7: [1, 1, 1, 0, 0, 0, 0, 0, 0],
        8: [1, 1, 1, 1, 1, 1, 1, 0, 0],
        9: [1, 1, 1, 1, 0, 1, 1, 0, 0]
    }

    # Get the segment configuration for the given digit
    digit_segments = segments.get(digit, [0, 0, 0, 0, 0, 0, 0, 0, 0])
   
    for i in range(3):
        r,g,b = 0,0,0
        if digit_segments[i*3] == 1:
            g = brightness
        if digit_segments[i*3+1] == 1:
            r = brightness
        if digit_segments[i*3+2] == 1:
            b = brightness
            
        strip.set_pixel((segment*3)+i,(r,g,b))
        
    strip.show()

strip = Neopixel(numpix, 1, 16, "GRB")
strip.fill((0,0,0))

colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255)]  # Colors for the segments

while True:
    for x in range(10):
        display_digit(x, strip, colors,0)
        for i in range(10):
            display_digit(i, strip, colors,1)
            time.sleep(1)