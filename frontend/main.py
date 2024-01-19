import subprocess
import sys
import pkg_resources

def install_libraries():
    required_libraries = ["google-generativeai", "Flask", "flask-cors"]

    installed_libraries = {package.project_name.lower(): package.version for package in pkg_resources.working_set}
    
    missing_libraries = [lib for lib in required_libraries if lib.lower() not in installed_libraries]

    if missing_libraries:
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_libraries)
    else:
        print("")

# Call the function to install libraries if necessary
install_libraries()
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as palm

app = Flask(__name__)
CORS(app) 

@app.route('/generate_response', methods=['POST'])
def generate_response():
    data = request.get_json()
    prompt = data.get('prompt', '')

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

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
