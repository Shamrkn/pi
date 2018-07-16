import RPi.GPIO as GPIO
import time


ledPin = 11                        #RPi Board Pin 11 (GPIO 17)


def setup():
    GPIO.setmode(GPIO.BOARD)       #Sets numbering to physical pin location
    GPIO.setup(ledPin, GPIO.OUT)   #Sets ledPin to Output Mode
    GPIO.output(ledPin, GPIO.LOW)  #Turn Off the LED
    print('Using pin %d' %ledPin)

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH) #Turn on LED
        print('LED is ON\n')
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW) #Turn off LED
        print('LED is OFF\n')
        time.sleep(1)



def destroy():
    GPIO.output(ledPin, GPIO.LOW) #Turn off LED
    GPIO.cleanup()

if __name__ == '__main__':     #program starts from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: #when ctrl+c pressed, clean up resources
        destroy()
            
        
