import sys
import subprocess
import sys
import pkg_resources

def install_libraries():
    required_libraries = ["opencv-python", "pyzbar","google-generativeai", "Flask", "flask-cors","markupsafe"]

    installed_libraries = {package.project_name.lower(): package.version for package in pkg_resources.working_set}
    
    missing_libraries = [lib for lib in required_libraries if lib.lower() not in installed_libraries]

    if missing_libraries:
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_libraries)
    else:
        print("")

# Call the function to install libraries if necessary
install_libraries()
import cv2
from pyzbar.pyzbar import decode
from markupsafe import Markup
import io
import os
def decode_qr_code(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray)

    texts = []
    for obj in decoded_objects:
        texts.append(obj.data.decode('utf-8'))

    return texts

# Example usage:
image_path = sys.argv[1]
decoded_texts = decode_qr_code(image_path)

import google.generativeai as palm

def generate_response(text):
    prompt = "Tell whether "+ text +" is healthy or not based upon nutritional information like calorie count, fats, sugar, protein content and give reason"

    apikey = "AIzaSyCVrjd8JXl1CDUlsuKxqBjBojieVcPaRUk"
    palm.configure(api_key=apikey)
    model_id = "models/text-bison-001"

    compl = palm.generate_text(
        model=model_id,
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=800,
        candidate_count=1
    )

    outputs = [output["output"] for output in compl.candidates]
    response = outputs[0] if outputs else "No response"
    return response

if decoded_texts:
    res=" "
    for text in decoded_texts:
        res+=generate_response(text)
        res+"\n"
    print(Markup(str(res)))   
else:
    print("No QR code found in the image.") 