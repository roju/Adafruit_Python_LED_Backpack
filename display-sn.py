from Adafruit_LED_Backpack import SevenSegment
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('sn', type=int)
args = parser.parse_args()


# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = SevenSegment.SevenSegment(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()

display.clear()
display.print_float(args.sn, decimal_digits=0)
display.set_colon(False)
display.write_display()
