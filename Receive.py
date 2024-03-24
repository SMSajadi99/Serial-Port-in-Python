import serial

# Open the serial port
ser = serial.Serial('COM30', 9600)  # Replace 'COM30' with your serial port, and 9600 with the appropriate baud rate

while True:
    try:
        # Read data from the serial port
        data = ser.readline().decode().strip()

        # If data is received
        if data:
            print(f"Received: {data}")
    except serial.SerialException as e:
        print(f"Error reading data: {e}")
        break
    except KeyboardInterrupt:
        print("Exiting program...")
        break

# Close the serial port
ser.close()