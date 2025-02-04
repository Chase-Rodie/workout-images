import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase (Make sure to use the correct path to your credentials file)
cred = credentials.Certificate("/Users/chaserodie/Downloads/fit-pantry-firebase-adminsdk-d8kbr-29d279c54f.json")  # Replace with actual path
firebase_admin.initialize_app(cred)
db = firestore.client()  # ✅ Now 'db' is defined

# Retrieve and delete the 5 most recently created documents
docs = db.collection("exercises").order_by("__name__", direction="DESCENDING").limit(5).stream()

for doc in docs:
    print(f"Deleting: {doc.id}")
    doc.reference.delete()

print("🔥 Deleted the 5 most recent documents!")
