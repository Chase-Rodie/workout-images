import firebase_admin
from firebase_admin import credentials, firestore
import json
import re

# Initialize Firebase (Skip if already initialized)
cred = credentials.Certificate("/Users/chaserodie/Downloads/fit-pantry-firebase-adminsdk-d8kbr-29d279c54f.json")  # Replace with actual path
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to clean document names (Ensures Firestore-compatible IDs)
def clean_doc_id(name):
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)  # Keeps letters, numbers, underscores, and hyphens

# Load Exercise Metadata JSON
with open("/Users/chaserodie/Desktop/free-exercise-db/dist/exercises_cleaned.json", "r") as file:  # Replace with actual path
    exercises_data = json.load(file)

# Load Image Data JSON (List of Objects) and Convert to a Dictionary
with open("exercise_data.json", "r") as file:  # Replace with actual path
    images_list = json.load(file)

# Convert image list into a dictionary for quick lookup
images_data = {item["name"]: item["images"] for item in images_list}

# Print available image keys
print("\n🔍 Available image keys in images_data:")
print(images_data.keys())  # ✅ Print all exercise names in the images JSON

# Merge Image URLs into Exercise Data and Upload to Firestore
for exercise in exercises_data:
    doc_id = clean_doc_id(exercise["name"])  # Create Firestore-compatible document ID
    
    # Debug: Print exercise name before lookup
    print(f"\n🔍 Processing Exercise: {exercise['name']}")
    
    if exercise["name"] in images_data:
        exercise["imageURLs"] = images_data[exercise["name"]]  # ✅ Assign full URLs from JSON
        print(f"✅ Match Found! Added images: {exercise['imageURLs']}")  # ✅ Confirm it's working
    else:
        print(f"❌ No match found for {exercise['name']} in images_data!")  # 🚨 Detect mismatches

    # Reference Firestore document in "exercises" collection
    doc_ref = db.collection("exercises").document(doc_id)

    # Upload/Update the document
    doc_ref.set(exercise, merge=True)  # ✅ Merges new data, preserving existing fields

    print(f"✅ Updated: {doc_id} with images")

print("\n🔥 All exercises updated with image URLs!")
