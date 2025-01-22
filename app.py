import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Generate features
n_samples = 200
data = pd.DataFrame({
    'Machine_ID': range(1, n_samples + 1),  # Unique machine IDs
    'Temperature': np.random.uniform(50, 100, n_samples),  # Random temperatures (50 to 100)
    'Run_Time': np.random.uniform(10, 200, n_samples)  # Random run times (10 to 200 seconds)
})

# Generate the target (Downtime_Flag) based on a rule
def generate_downtime_flag(row):
    # Machines with high temperature (>80) and long run times (>150) are more likely to fail
    if row['Temperature'] > 80 and row['Run_Time'] > 150:
        return 1
    elif row['Temperature'] > 90 or row['Run_Time'] > 180:  # Secondary conditions for downtime
        return 1
    else:
        return 0

data['Downtime_Flag'] = data.apply(generate_downtime_flag, axis=1)

# Save the synthetic dataset
data.to_csv('synthetic_manufacturing_data.csv', index=False)
print("Synthetic dataset generated and saved as 'synthetic_manufacturing_data.csv'.")




from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

app = Flask(__name__)
model = None  # Placeholder for the trained model

# Upload Endpoint
@app.route('/upload', methods=['POST'])
def upload_data():
    file = request.files['file']
    data = pd.read_csv(file)
    data.to_csv('uploaded_data.csv', index=False)
    return jsonify({"message": "Data uploaded successfully!"})

# Train Endpoint
@app.route('/train', methods=['POST'])
def train_model():
    global model
    data = pd.read_csv('uploaded_data.csv')
    X = data[['Temperature', 'Run_Time']]  # Features
    y = data['Downtime_Flag']  # Target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)

    # Save the model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return jsonify({"message": "Model trained successfully!", "accuracy": accuracy})

# Predict Endpoint
@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)

    # Parse JSON input
    input_data = request.json
    features = [[input_data['Temperature'], input_data['Run_Time']]]
    prediction = model.predict(features)
    confidence = max(model.predict_proba(features)[0])

    return jsonify({"Downtime": "Yes" if prediction[0] == 1 else "No", "Confidence": round(confidence, 2)})

if __name__ == '__main__':
    app.run(debug=True)