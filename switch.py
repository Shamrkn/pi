import RPi.GPIO as GPIO
import time


ledPin = 11                        #RPi Board Pin 11 (GPIO 17)
buttonPin = 12


def setup():
    GPIO.setmode(GPIO.BOARD)       #Sets numbering to physical pin location
    GPIO.setup(ledPin, GPIO.OUT)   #Sets ledPin to Output Mode
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            GPIO.output(ledPin, GPIO.HIGH)
            print('LED is ON\n')
        else :
            GPIO.output(ledPin, GPIO.LOW)
            print('LED is OFF\n')


def destroy():
    GPIO.output(ledPin, GPIO.LOW) #Turn off LED
    GPIO.cleanup()

if __name__ == '__main__':     #program starts from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: #when ctrl+c pressed, clean up resources
        destroy()
            
        
