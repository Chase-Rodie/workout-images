import os
import json

# Your GitHub raw URL (change to match your repo)
GITHUB_RAW_URL = "https://raw.githubusercontent.com/Chase-Rodie/workout-images/main"

# Path to the local images folder
local_folder = "exercises"

# JSON structure to store the data
exercise_data = []

# Loop through each exercise folder
for exercise in sorted(os.listdir(local_folder)):
    exercise_path = os.path.join(local_folder, exercise)
    if os.path.isdir(exercise_path):  # Check if it's a folder
        images = []
        for image in sorted(os.listdir(exercise_path)):
            if image.endswith((".jpg", ".png")):
                image_url = f"{GITHUB_RAW_URL}/{local_folder}/{exercise}/{image}"
                images.append(image_url)

        exercise_data.append({
            "name": exercise.replace("_", " "),  # Format name
            "images": images
        })

# Save as JSON file
with open("exercise_data.json", "w") as json_file:
    json.dump(exercise_data, json_file, indent=4)

print("✅ JSON file generated: exercise_data.json")
