import gpiod
import time

CHIP="/dev/gpiochip0"
LINE = 144

chip = gpiod.Chip(CHIP)
line = chip.get_line(LINE)

line.request(consumer="blink", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])



for i in range(10):
    line.set_value(1)
    print("HIGH")
    time.sleep(1)
    
    line.set_value(0)
    print("LOW")
    time.sleep(1)

line.set_value(0)
line.release()
    