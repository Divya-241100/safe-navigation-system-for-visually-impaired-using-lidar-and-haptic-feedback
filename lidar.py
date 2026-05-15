import serial

# Change port if needed
ser = serial.Serial("/dev/serial0", 115200, timeout=1)

def get_distance():
    try:
        data = ser.read(9)

        if len(data) == 9:
            distance = data[2] + data[3] * 256
            return distance
    except:
        pass

    return 999  # fallback value
