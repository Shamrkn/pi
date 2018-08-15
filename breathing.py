import RPi.GPIO as GPIO
import time


ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]


def setup() :
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)       #Sets numbering to physical pin location
    for pin in ledPins:
        GPIO.setup(pin, GPIO.OUT)

#Test1234
def loop() :
    while True :
        for pin in ledPins:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)
        for pin in ledPins[10:0:-1]:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(.1)
            GPIO.output(pin, GPIO.HIGH)


def destroy():
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':     #program starts from here
    setup()
    try :
        loop()
    except KeyboardInterrupt: #when ctrl+c pressed, clean up resources
        destroy()
            
        
