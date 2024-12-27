# !pip install firebase-admin boto3 flask flask-ngrok pycryptodome
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/your-firebase-key.json")  # Update this path
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://your-database.firebaseio.com"  # Replace with your database URL
})

# Add sample data
ref = db.reference("/patient_data")
ref.push({"patient_id": 1, "heart_rate": 72, "status": "stable"})
print("Firebase initialized and sample data added.")
