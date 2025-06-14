import face_recognition
import cv2

def detect_faces(image):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_image)

    cropped_faces = []
    for top, right, bottom, left in face_locations:
        face_img = image[top:bottom, left:right]
        cropped_faces.append(face_img)

    return cropped_faces