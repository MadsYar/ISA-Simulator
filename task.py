import machine, time

led = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button.value():
        led.value(0)
    else:
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)