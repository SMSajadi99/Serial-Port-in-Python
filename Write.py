import serial
import sys

# Open the serial port
ser = serial.Serial('COM29', 9600)  # Replace 'COM29' with your serial port, and 9600 with the appropriate baud rate

while True:
    # Read one character from the keyboard (without waiting for Enter key)
    char = sys.stdin.read(1)

    # If the character is not empty
    if char:
        try:
            # Send the character over the serial port
            ser.write(char.encode())
            print(f"Sent: {char}")
        except serial.SerialException as e:
            print(f"Error sending data: {e}")
            break

        # Clear the character after processing
        char = ''

    # If the character is 'q', exit the loop
    if char == 'q':
        break

# Close the serial port
ser.close()