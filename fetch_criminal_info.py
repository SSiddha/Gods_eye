
import json

def get_criminal_info(label, json_path='face_db.json'):
    with open(json_path, 'r') as f:
        face_db = json.load(f)
    return face_db.get(label, {"name": "Unknown", "info": "No record found."})
