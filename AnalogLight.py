import mraa
import time
mraa.addSubplatform(mraa.GROVEPI,"0")
light =mraa.Aio(512)
while True:
	val=light.read()
	time.sleep(0.5)
	print("Light value = %r"%val)


