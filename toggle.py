import RPi.GPIO as GPIO
import time


ledPin = 11                        #RPi Board Pin 11 (GPIO 17)
buttonPin = 12                     #define buttonPin
ledState = False


def setup() :
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)       #Sets numbering to physical pin location
    GPIO.setup(ledPin, GPIO.OUT)   #Sets ledPin to Output Mode
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonEvent(channel) :
    global ledState
    print ('buttonEvent GPIO%d'%channel)
    ledState = not ledState
    
    if ledState :
        print ('Turn ON LED... ') 
    else :
        print ('Turn OFF LED... ')
		
    GPIO.output(ledPin, ledState)
    

def loop() :
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback = buttonEvent, bouncetime = 300)
    while True :
        pass


def destroy():
    GPIO.output(ledPin, GPIO.LOW) #Turn off LED
    GPIO.cleanup()

if __name__ == '__main__':     #program starts from here
    setup()
    try :
        loop()
    except KeyboardInterrupt: #when ctrl+c pressed, clean up resources
        destroy()
            
        
