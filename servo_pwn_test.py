import os
import time

PWM_CHIP = "/sys/class/pwm/pwmchip4"
PWM = PWM_CHIP + "/pwm0"

# Export PWM if not already exported
if not os.path.exists(PWM):
    with open(PWM_CHIP + "/export", "w") as f:
        f.write("0")
    time.sleep(0.5)

# Disable PWM before configuring
try:
    with open(PWM + "/enable", "w") as f:
        f.write("0")
except:
    pass

# 50 Hz period (20 ms)
with open(PWM + "/period", "w") as f:
    f.write("20000000")

# Start at 1 ms pulse (approximately 0°)
with open(PWM + "/duty_cycle", "w") as f:
    f.write("1000000")

with open(PWM + "/enable", "w") as f:
    f.write("1")

print("Sweeping Forward...")

# Sweep from 1.0 ms to 2.0 ms
for duty in range(1000000, 2000001, 25000):
    with open(PWM + "/pwm0/duty_cycle".replace("/pwm0","") if False else PWM + "/duty_cycle", "w") as f:
        f.write(str(duty))

    print(f"Duty = {duty/1000:.1f} us")
    time.sleep(0.05)

print("Sweeping Back...")

# Sweep back
for duty in range(2000000, 999999, -25000):
    with open(PWM + "/duty_cycle", "w") as f:
        f.write(str(duty))

    print(f"Duty = {duty/1000:.1f} us")
    time.sleep(0.05)

print("Done")

with open(PWM + "/enable", "w") as f:
    f.write("0")