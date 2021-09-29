import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
p = 4
e = 17
n = 27
y = 23
s = 24
GPIO.setup(p, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(n, GPIO.OUT)
GPIO.setup(y, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(s, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

pwm = GPIO.PWM(e, 1)
pwmm = GPIO.PWM(n, 1)

def mycallback(y):
  pwm.start(0)
  pwmm.start(0)
  while 1:
    if(y==1):
      for dc in range(101):
        pwm.ChangeDutyCycle(dc)
        sleep(0.01)
      for ic in range(101,0,-1):
        pwm.ChangeDutyCycle(ic)
    if(y==0):
      for pc in range(101):
        pwmm.ChangeDutyCycle(pc)
        sleep(0.01)
      for mc in range(101,0,-1):
        pwmm.ChangeDutyCycle(mc)



try:
  GPIO.output(p,1)
  sleep(1)
  GPIO.output(p,0)
  GPIO.wait_for_edge(y,GPIO.RISING)
  GPIO.wait_for_edge(s,GPIO.FALLING)
  GPIO.add_event_detect(y,GPIO.RISING,callback = mycallback, bouncetime = 100)
  GPIO.add_event_detect(s,GPIO.FALLING,callback = mycallback, bouncetime = 100)
except KeyboardInterrupt:
  print('\nExiting')
pwm.stop()
GPIO.cleanup()