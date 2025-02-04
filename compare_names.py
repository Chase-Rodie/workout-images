import json

# Load Exercise Metadata JSON
with open("/Users/chaserodie/Desktop/free-exercise-db/dist/exercises.json", "r") as file:  
    exercises_data = json.load(file)

# Load Image Data JSON
with open("exercise_data.json", "r") as file:  
    images_data = json.load(file)

# Convert image_data to a dictionary with normalized keys
images_dict = {item["name"].strip().lower(): item["images"] for item in images_data}

# Find missing matches
missing = []
for exercise in exercises_data:
    normalized_name = exercise["name"].strip().lower()
    if normalized_name not in images_dict:
        missing.append(exercise["name"])

# Print the missing names
if missing:
    print("\n🚨 Mismatched or Missing Names in exercise_data.json:\n")
    for name in missing:
        print(f"❌ {name}")
else:
    print("✅ All names match correctly!")

print(f"\n🔎 Total Missing: {len(missing)}")
