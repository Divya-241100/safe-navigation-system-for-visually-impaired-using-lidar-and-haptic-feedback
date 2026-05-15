import RPi.GPIO as GPIO
import time

# GPIO pins
BUZZER = 17
VIBRATION = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(VIBRATION, GPIO.OUT)

def alert_system(distance):
    """
    Triggers alerts based on LiDAR distance input
    """

    print(f"Obstacle detected at {distance} cm")

    # CRITICAL ALERT (very close object)
    if distance < 30:
        print("⚠ CRITICAL ALERT")

        GPIO.output(BUZZER, True)
        GPIO.output(VIBRATION, True)
        time.sleep(0.5)

        GPIO.output(BUZZER, False)
        GPIO.output(VIBRATION, False)

    # WARNING ALERT (near object)
    elif distance < 100:
        print("⚠ WARNING ALERT")

        GPIO.output(VIBRATION, True)
        time.sleep(0.2)

        GPIO.output(VIBRATION, False)

    # SAFE CONDITION
    else:
        print("✔ Safe Path")

        GPIO.output(BUZZER, False)
        GPIO.output(VIBRATION, False)

    time.sleep(0.1)


# Cleanup function (important for Raspberry Pi safety)
def cleanup():
    GPIO.cleanup()
