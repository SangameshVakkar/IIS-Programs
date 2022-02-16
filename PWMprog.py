import mraa
import time

mraa.addSubplatform(mraa.GROVEPI,"0")

x= mraa.Pwm(517)
x.period_us(700)
x.enable(True)

value =0.0

while True:
	x.write(value)
	time.sleep(0.05)
	value= value+0.01
	print("Value ",value)
	if value >=1:
		value = 0.0
