import time
import spidev as SPI
import datetime
import includes.waveshare as logo
from includes.epd import Epd
from includes.progressbar import ProgressBar

# Possible displays
DISPLAY_TYPE = "EPD_2X9"
# DISPLAY_TYPE = "EPD_2X13"
# DISPLAY_TYPE = "EPD_1X54"

# Select fitting logo
if DISPLAY_TYPE == "EPD_2X9":
  waveshare = logo.waveshare_128x296
elif DISPLAY_TYPE == "EPD_2X13":
  waveshare = logo.waveshare_122x250
elif DISPLAY_TYPE == "EPD_1X54":
  waveshare = logo.waveshare_200x200
else:
  raise "Unsupported display!"

# Circle
circle3232 = [
  0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xE0, 0x3F, 0xFF, 0xFF, 0x80, 0x07, 0xFF, 
  0xFE, 0x00, 0x03, 0xFF, 0xFC, 0x00, 0x01, 0xFF, 0xF8, 0x00, 0x00, 0x7F, 0xF0, 0x0F, 0x80, 0x7F, 
  0xE0, 0x3F, 0xE0, 0x3F, 0xE0, 0x7F, 0xF0, 0x1F, 0xC0, 0xFF, 0xF8, 0x1F, 0xC1, 0xFF, 0xFC, 0x1F, 
  0x81, 0xFF, 0xFC, 0x0F, 0x83, 0xFF, 0xFE, 0x0F, 0x83, 0xFF, 0xFE, 0x0F, 0x83, 0xFF, 0xFE, 0x0F, 
  0x83, 0xFF, 0xFE, 0x0F, 0x83, 0xFF, 0xFE, 0x0F, 0x81, 0xFF, 0xFC, 0x0F, 0xC1, 0xFF, 0xFC, 0x1F, 
  0xC0, 0xFF, 0xF8, 0x1F, 0xC0, 0x7F, 0xF8, 0x1F, 0xE0, 0x3F, 0xE0, 0x3F, 0xF0, 0x0F, 0x80, 0x7F, 
  0xF8, 0x00, 0x00, 0x7F, 0xF8, 0x00, 0x00, 0xFF, 0xFE, 0x00, 0x03, 0xFF, 0xFF, 0x00, 0x07, 0xFF, 
  0xFF, 0xE0, 0x3F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 
]

# Line
line3232 = [
  0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 
  0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 
  0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 
  0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 
  0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 
  0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 
  0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 
  0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 0xFF, 0xFE, 0x3F, 0xFF, 
]

bus = 0
device = 0

spi = SPI.SpiDev(bus, device)
display = Epd(spi, DISPLAY_TYPE)

print('--> Init and clear full screen')
display.clearDisplayFull()

# Show full pic
print('--> Show waveshare logo')
display.showImageFull(waveshare)
time.sleep(2)

# Init and clear part screen
print('--> Init and clear part screen')
display.clearDisplayPart()

# Show part inage
print('--> Show part of an image (logo)')
display.showImagePart(0, display.xDot-1, 0, display.yDot-1, waveshare)
time.sleep(2)

# Show image with size
print('--> Show circle and line')
display.showImage((display.yDot-32)/8-2, 0, circle3232, 32, 32) # Circle
display.showImage((display.yDot-32)/8-2, 4, line3232, 32, 32) # Line
time.sleep(2)

# String
print('--> Show strings')
display.showString(0, 10, "WELCOME EPD", "Font16")
display.showString(0, 26, "I am an electronic paper display", "Font12")
time.sleep(1)

# Progress bar
print('--> Show progress bar')
progress = ProgressBar(display, 10)
for i in range(0, 10):
  progress.showProgress(i)

