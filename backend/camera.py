# backend/camera.py
import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Fungsi untuk menghitung sudut dengan tiga titik
def calc_angle(a, b, c):
    ang = math.degrees(
        math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
    )
    return abs(ang)

def generate_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        if not success:
            break

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        angle = 0
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                lm = handLms.landmark
                h, w, _ = img.shape

                # Ambil titik untuk deteksi sudut jempol dan telunjuk
                p1 = lm[4]  # thumb_tip
                p2 = lm[8]  # index_tip
                p3 = lm[3]  # thumb_mcp
                p4 = lm[5]  # index_mcp

                # Ubah koordinat dari normalized (0-1) ke pixel
                a = [p1.x * w, p1.y * h]  # thumb_tip
                b = [p2.x * w, p2.y * h]  # index_tip
                c = [p3.x * w, p3.y * h]  # thumb_mcp
                d = [p4.x * w, p4.y * h]  # index_mcp

                # Hitung sudut antara jempol dan telunjuk
                angle1 = int(calc_angle(a, b, c))  # Sudut antara thumb_tip dan index_tip
                angle2 = int(calc_angle(b, a, d))  # Sudut antara index_tip dan thumb_tip

                # Ambil sudut rata-rata (agar lebih stabil)
                angle = (angle1 + angle2) // 2

                # Gambar landmarks dan koneksi tangan
                mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

                # Tampilkan sudut antara jempol dan telunjuk di atas gambar
                cv2.putText(img, f"Thumb-Index Angle: {angle} deg", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Encode frame menjadi JPEG
        _, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()

        # Stream frame ke browser
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
