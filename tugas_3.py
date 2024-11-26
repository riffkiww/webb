import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


LED_RED = 5
LED_YELLOW = 6
LED_GREEN = 12


POT_PIN = 18


GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(POT_PIN, GPIO.IN)

def read_potentiometer():
    value = GPIO.input(POT_PIN)  
    if value == GPIO.HIGH:
        return 70  
    else:
        return 20  

while True:
    water_level = read_potentiometer()
    if water_level < 30:
        print("Level air rendah")
        GPIO.output(LED_RED, GPIO.HIGH)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.LOW)
    elif 30 <= water_level < 70:
        print("Level air sedang")
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_YELLOW, GPIO.HIGH)
        GPIO.output(LED_GREEN, GPIO.LOW)
    else:
        print("Level air penuh")
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.HIGH)

    time.sleep(1)  
