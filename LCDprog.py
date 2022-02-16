import mraa
from upm import pyupm_jhd1313m1 as lcd
import time
mraa.addSubplatform(mraa.GROVEPI,"0")
pin = mraa.Aio(512)
my_lcd=lcd.Jhd1313m1(0,0x3E,0x62)

r=0
g=100
b=63

while True:
	my_lcd.setCursor(0,0)
	#my_lcd.setColor(100,39,249)
	my_lcd.setColor(r,g,b)
	data= pin.read()
	r=r+data
	g=g+data
	b=b+data
	if r> 255:
		r=r%255
	if g>255:
		g=g% 255
	if b> 255:
		b=b%255
	#print("R = %r "%r)
	#print("G = %r "%g)
	#print("B = %r "%b)
	data = str(data)
	print("Data ",data)
	my_lcd.setCursor(1,2)
	#time.sleep(1)
	my_lcd.write(data)
	time.sleep(1)
	my_lcd.clear()
