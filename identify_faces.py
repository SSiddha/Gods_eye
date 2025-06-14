import face_recognition
import os
import cv2

def load_known_faces(known_faces_dir='known_faces'):
    known_encodings = {}
    for filename in os.listdir(known_faces_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            label = os.path.splitext(filename)[0]
            path = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings[label] = encodings[0]
            else:
                print(f" No encoding found for {filename}")
    return known_encodings

known_encodings = load_known_faces()

def identify_face(face_img):
    rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)
    if not encodings:
        return "unknown"

    face_encoding = encodings[0]
    for name, known_encoding in known_encodings.items():
        match = face_recognition.compare_faces([known_encoding], face_encoding, tolerance=0.5)
        if match[0]:
            return name
    return "unknown"