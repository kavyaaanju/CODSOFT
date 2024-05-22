import dlib
import cv2
import numpy as np
from imutils import face_utils

# Load pre-trained models
detector = dlib.get_frontal_face_detector()
shape_predictor_path = r"C:\Users\anju&janu\Downloads\shape_predictor_68_face_landmarks.dat"
face_rec_model_path = r"C:\Users\anju&janu\Downloads\dlib_face_recognition_resnet_model_v1.dat"

# Load models
predictor = dlib.shape_predictor(shape_predictor_path)
face_rec_model = dlib.face_recognition_model_v1(face_rec_model_path)

def load_image(file_path):
    try:
        image = cv2.imread(file_path)
        if image is None:
            raise ValueError(f"Unable to load image at path: {file_path}")
        
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return rgb_image
    except Exception as e:
        print(f"Error loading image at path {file_path}: {e}")
        return None

def get_face_encodings(image):
    face_locations = detector(image, 1)
    face_encodings = []

    for face in face_locations:
        shape = predictor(image, face)
        face_encoding = np.array(face_rec_model.compute_face_descriptor(image, shape))
        face_encodings.append(face_encoding)
    
    return face_encodings

# Load known faces
known_face_paths = [
    r"C:\Users\anju&janu\OneDrive\known_people_folder\anushka.jpg",
    r"C:\Users\anju&janu\OneDrive\known_people_folder\prabas.jpg",
    r"C:\Users\anju&janu\OneDrive\known_people_folder\allu arjun.jpeg",
    r"C:\Users\anju&janu\OneDrive\known_people_folder\chiranjeevi.jpeg",
    r"C:\Users\anju&janu\OneDrive\known_people_folder\pavan kalyan.jpeg"
]

known_face_encodings = []
known_face_names = ["Anushka", "Prabas", "Allu Arjun", "Chiranjeevi", "Pavan Kalyan"]  # Adjust names as needed

for path in known_face_paths:
    image = load_image(path)
    if image is not None:  # Check if image loaded successfully
        encodings = get_face_encodings(image)
        if encodings:
            known_face_encodings.append(encodings[0])
        else:
            print(f"No faces found in image: {path}")
    else:
        print(f"Skipping image: {path}")

# Face recognition function using Euclidean distance
def recognize_faces(frame, known_face_encodings, known_face_names):
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = detector(rgb_image, 1)
    face_encodings = [np.array(face_rec_model.compute_face_descriptor(rgb_image, predictor(rgb_image, face))) for face in face_locations]
    
    face_names = []
    for face_encoding in face_encodings:
        distances = np.linalg.norm(known_face_encodings - face_encoding, axis=1)
        min_distance = np.min(distances)
        if min_distance < 0.6:  # Threshold for face recognition
            name = known_face_names[np.argmin(distances)]
        else:
            name = "Unknown"
        face_names.append(name)
    
    return face_locations, face_names

# Main function
def main():
    # Video capture from the webcam
    video_capture = cv2.VideoCapture(0)  # Using webcam for example

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture image from webcam")
            break

        face_locations, face_names = recognize_faces(frame, known_face_encodings, known_face_names)

        for (face, name) in zip(face_locations, face_names):
            (x, y, w, h) = face_utils.rect_to_bb(face)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
