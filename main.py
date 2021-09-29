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

def mycallback(signal):
  if(signal==y):
    pwm.start(0)
    for dc in range(100):
      pwm.ChangeDutyCycle(dc)
      sleep(0.01)
    for ic in range(100,0,-1):
      pwm.ChangeDutyCycle(ic)
      sleep(0.01)
      
  if(signal==s):
    pwmm.start(0)
    for pc in range(100):
      pwmm.ChangeDutyCycle(pc)
      sleep(0.01)
    for mc in range(100,0,-1):
      pwmm.ChangeDutyCycle(mc)
      sleep(0.01)
    
pwmmm = GPIO.PWM(p,1)


try:
  GPIO.add_event_detect(y,GPIO.RISING,callback = mycallback)
  GPIO.add_event_detect(s,GPIO.FALLING,callback = mycallback)
  pwmmm.start(50)
  while True:
    pass
except KeyboardInterrupt:
  print('\nExiting')
pwm.stop()
GPIO.cleanup()