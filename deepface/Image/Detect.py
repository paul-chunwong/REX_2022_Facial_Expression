from deepface import DeepFace
from deepface.basemodels import VGGFace
import matplotlib.pyplot as plt
import os
import time
import pandas as pd
from glob import glob
try:
    # PIL
    import Image
except ImportError:
    # Pillow
    from PIL import Image

def process_image(img_path):
    print ("Processing image...")
    # Open the image
    img=Image.open(img_path)
    img.show()

    #Do the processing
    detected_face=DeepFace.detectFace(img_path)
    plt.imshow(detected_face)
    plt.show()

    backends = [
    'opencv', 
    'ssd', 
    'dlib', 
    'mtcnn', 
    'retinaface', 
    'mediapipe'
    ]

    # face recognition
    df = DeepFace.find(img_path, db_path = "C:/Users/ChrisRA/Desktop/URO 2022/deepface/Image",detector_backend=backends[3])

    #embeddings
    embedding=DeepFace.represent(img_path,detector_backend=backends[3])

    #facial analysis
    attributes=['age','gender','race','emotion']
    demography=DeepFace.analyze(img_path,actions=attributes)

    demo_age=print((demography["age"]),"years old")
    demo_gen=print(demography["gender"])
    percentage_race=print(demography["race"])
    demo_race=print(demography["dominant_race"])
    percentage_emotion=print(demography["emotion"])
    demo_emotion=print(demography["dominant_emotion"])

    time.sleep(10)

    #close the images
    img.close()

images_dir="C:/Users/ChrisRA/Desktop/URO 2022/deepface/Image"

if __name__ == "__main__":
    # List all JPEG files in your directory
    images_list = glob(os.path.join(images_dir, "*.jpg"))

    for img_filename in images_list:
        img_path = os.path.join(images_dir, img_filename)
        process_image(img_path)





