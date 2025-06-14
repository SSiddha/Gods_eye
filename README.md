# GOD'S EYE – Criminal Face Detection System


## 🔍 Overview

GOD'S EYE is a facial recognition-based criminal detection system that identifies known criminals from input images. By comparing facial features with a trained dataset, it quickly flags and returns any matches, along with relevant information such as name and crime history.

## 📦 Features

- Detects faces from input images
- Matches with known criminal faces in the dataset
- Displays matched faces with associated crime data
- Clean and modular Python code

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** OpenCV, face_recognition
- **Data Format:** Image dataset + JSON metadata


## 🚀 How to Run

1. **Install required libraries:**

```bash
pip install opencv-python face_recognition
```

2. **Prepare the dataset:**

- Add criminal images to the `known_faces/` folder
- Add the data into face_db
```json
{
  "test_name": {
    "name": "John Doe",
    "info": "Robbery"
  },
  "test_name2": {
    "name": "Jane Smith",
    "info": "Fraud"
  }
}
```

3. **Run the program:**

```bash
python main.py '<path the the image file that needs to be checked>'
```

4. **View results:**
- Console will also show name and crime information.

---

## 🖼️ Demo

 python .\main.py .\Test_images\test1.jpg

 Processing Image: .\Test_images\test1.jpg

 1 face(s) detected.

Face 1:
  Name: Joel Myrie
  Crime Info: Racketeering

---

## 🔮 Future Improvements

- Real-time video feed detection
- GUI for ease of use
- Integration with police databases
- Face detection from low-light images

---

## 📜 License

This project is intended for educational and research use only.  
**Do not use it for unethical surveillance or without consent.**

---

> 👁️ *GOD'S EYE sees all – but use it responsibly.*
