from imu import MPU6050
from machine import I2C, Pin
import math
import time

i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
mpu = MPU6050(i2c)

roll = 0
pitch = 0
yaw = 0
tLoop = 0
cnt = 0

while True:
    tStart = time.ticks_ms()
    xGyro = mpu.gyro.x
    yGyro = mpu.gyro.y
    zGyro = mpu.gyro.z
    roll = roll + yGyro * tLoop
    pitch = pitch + xGyro * tLoop
    yaw = yaw + zGyro * tLoop
    cnt = cnt + 1
    if cnt == 10:
        cnt = 0
        print('R: ', roll, 'P: ', pitch, 'Y: ', yaw)
    tStop = time.ticks_ms()
    tLoop = (tStop - tStart) * .001