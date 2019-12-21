
# coding:utf-8
import RPi.GPIO as GPIO
import time
import sys


 

#########定义模式############

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

 

########电机驱动接口定义############

ENA = 13  # //L298使能A

ENB = 20  # //L298使能B

IN1 = 16  # //电机接口1

IN2 = 19  # //电机接口2

IN3 = 21  # //电机接口3

IN4 = 26  # //电机接口4

OUTL = 23 # //左边红外探测器

OUTR = 24 # //右边红外探测器

 

#########电机初始化为LOW##########

GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

#初始化红外探测器接口

GPIO.setup(OUTL, GPIO.IN)

GPIO.setup(OUTR, GPIO.IN)
 

########定义左右电机初始速度#########

pwm1 = GPIO.PWM(ENA, 100)  # 第一个参数为引脚号，第二个参数为频率（HZ）

pwm2 = GPIO.PWM(ENB, 100)

pwm1.start(5)  # 以百分比设置速度

pwm2.start(5)

 

 

#########定义电机正转函数##########

def forward():
    print('正在向前....')

    GPIO.output(ENA, True)

    GPIO.output(IN1, False)

    GPIO.output(IN2, True)

 

    GPIO.output(ENB, True)

    GPIO.output(IN3, True)

    GPIO.output(IN4, False)


 

 

#########定义电机反转函数##########

def back():
    stop()

    print('正在后退....')

    GPIO.output(ENA, True)

    GPIO.output(IN1, True)

    GPIO.output(IN2, False)

 

    GPIO.output(ENB, True)

    GPIO.output(IN3, False)

    GPIO.output(IN4, True)


 

 

#########定义电机停止函数##########

def stop():

    GPIO.output(ENA, False)

    GPIO.output(ENB, False)

    GPIO.output(IN1, False)

 

    GPIO.output(IN2, False)

    GPIO.output(IN3, False)

    GPIO.output(IN4, False)

 

 

########左转弯函数#######

def left():

    GPIO.output(ENA, True)

    GPIO.output(IN1, True)

    GPIO.output(IN2, False)

 

    GPIO.output(ENB, True)

    GPIO.output(IN3, True)

    GPIO.output(IN4, False)

 

 

########左转弯函数#######

def right():

    GPIO.output(ENA, True)

    GPIO.output(IN1, False)

    GPIO.output(IN2, True)

 

    GPIO.output(ENB, True)

    GPIO.output(IN3, False)

    GPIO.output(IN4, True)

 

while(True):
	
	
	sensor_L = GPIO.input(OUTL)
	sensor_R = GPIO.input(OUTR)
	
	if sensor_R == 0 and sensor_L == 1:
		left()
		tik = time.time()
		while time.time()-tik < 0.05:
			left()
	
	elif sensor_R == 1 and sensor_L == 0:
		right()
		tik = time.time()
		while time.time() - tik < 0.05:
			right()
		
	elif sensor_R == 0 and sensor_L == 0:
		stop()
		
	else:
		forward()
	
	#if sensor_L == 1 and sensor_R == 1:
	#	forward()
	
	#elif sensor_L == 0 and sensor_R == 1:
	#	right()
	#	time.sleep(100)
	
	#elif sensor_L == 1 and sensor_R == 0:
	#	left()
	#	time.sleep(100)
	
	#elif sensor_L == 0 and sensor_R == 0:
	#	stop()
