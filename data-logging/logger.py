import serial
import time

# === CONFIGURATION ===
PORT = 'COM3' 
BAUD_RATE = 9600       
OUTPUT_FILE = 'arduino_data.txt'  

# === SETUP SERIAL CONNECTION ===
try:
    ser = serial.Serial(PORT, BAUD_RATE)
    time.sleep(2)
    print(f"Connected to {PORT}. Saving data to {OUTPUT_FILE}")
except serial.SerialException:
    print(f"Error: Could not open port {PORT}.")
    exit()

# === OPEN FILE AND START LOGGING ===
with open(OUTPUT_FILE, 'w') as f:
    try:
        while True:
            line = ser.readline().decode('utf-8', errors='replace').strip()
            if line:
                f.write(line + '\n')
    except KeyboardInterrupt:
        print("\nRecording stopped by user.")

ser.close()
print("Serial connection closed.")
