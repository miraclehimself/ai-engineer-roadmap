import json
import os

FILE = "patients.json"

def load_patients():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
        
    return {}

def save_patients(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)