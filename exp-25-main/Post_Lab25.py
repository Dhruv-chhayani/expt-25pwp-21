# Python Code

import serial
import time

# Set your Arduino COM port (Windows example: COM3, Linux example: /dev/ttyUSB0)
arduino_port = "COM3"     
baud_rate = 9600          

# Open serial connection
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for Arduino to reset

# Message to send
message = "Hello Arduino!"

# Convert string to bytes and send
ser.write(message.encode())

print(f"Sent: {message}")

# Close the port
ser.close()

# Arduino Code

# void setup() {
#   Serial.begin(9600);
# }

# void loop() {
#   if (Serial.available()) {
#     String msg = Serial.readString();
#     Serial.println("Received: " + msg);
#   }
# }
