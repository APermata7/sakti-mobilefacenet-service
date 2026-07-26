import insightface
import os

print("Downloading buffalo_l model...")
os.makedirs("models_data", exist_ok=True)
insightface.app.FaceAnalysis(name='buffalo_l')
print("Model downloaded successfully")