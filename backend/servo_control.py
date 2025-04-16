# backend/servo_control.py
# import serial

# arduino = serial.Serial('COM3', 9600)  # Ganti COM sesuai port kamu

# def send_angle(angle):
#     angle = max(0, min(angle, 180))  # Clamp antara 0-180
#     arduino.write(f"{angle}\n".encode())

def send_angle(angle):
    print(f"[DEBUG] Sudut dikirim: {angle}°")