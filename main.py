
import sys
import cv2
from detect_faces import detect_faces
from identify_faces import identify_face
from fetch_criminal_info import get_criminal_info

def main(image_path):
    print(f"\n Processing Image: {image_path}\n")

    image = cv2.imread(image_path)
    if image is None:
        print(" Error: Unable to read the image.")
        return

    faces = detect_faces(image)
    if not faces:
        print(" No faces detected.")
        return

    print(f" {len(faces)} face(s) detected.\n")

    for i, face_img in enumerate(faces):
        label = identify_face(face_img)
        info = get_criminal_info(label)
        print(f"Face {i+1}:")
        print(f"  Name: {info['name']}")
        print(f"  Crime Info: {info['info']}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
    else:
        main(sys.argv[1])
