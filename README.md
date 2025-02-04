# Manufacturing Downtime Predictor

A RESTful API to predict machine downtime using manufacturing data.

## Features
- Upload a dataset (`POST /upload`)
- Train a machine learning model (`POST /train`)
- Make predictions based on input features (`POST /predict`)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Manufacturing-Downtime-Predictor.git
   cd Manufacturing-Downtime-Predictor
---

### **4. Postman API Setup**

#### Step 1: Install Postman.
Download and install [Postman](https://www.postman.com/downloads/).

#### Step 2: Create Requests
1. **Create a Collection**:
   - In Postman, click `+ New Collection`.
   - Name it `Manufacturing Downtime API`.

2. **Add Requests**:
   - **Upload**:
     - Method: `POST`.
     - URL: `http://127.0.0.1:5000/upload`.
     - Go to the `Body` tab → Select `form-data` → Add key:
       - Key: `file` (type: File) → Attach `synthetic_manufacturing_data.csv`.

   - **Train**:
     - Method: `POST`.
     - URL: `http://127.0.0.1:5000/train`.

   - **Predict**:
     - Method: `POST`.
     - URL: `http://127.0.0.1:5000/predict`.
     - Go to the `Body` tab → Select `raw` → Choose JSON → Add:
       ```json
       {
         "Temperature": 85,
         "Run_Time": 160
       }
       ```
 <img width="1276" alt="Screenshot 2025-01-23 at 1 00 39 AM" src="https://github.com/user-attachments/assets/8476af0f-e3ba-4ab7-9141-c68a1623d107" />
 <img width="1289" alt="Screenshot 2025-01-23 at 1 00 31 AM" src="https://github.com/user-attachments/assets/2b6dc8ed-9690-424f-92b5-f052de063a2f" />
 <img width="1293" alt="Screenshot 2025-01-23 at 1 00 18 AM" src="https://github.com/user-attachments/assets/42a214de-9958-4ef2-9c36-3b903956e4f8" />
<img width="1278" alt="Screenshot 2025-01-23 at 12 59 59 AM" src="https://github.com/user-attachments/assets/979072c5-118c-4478-833b-9383367b50ed" />

3. **Test the Endpoints**:
   - Run each request and verify the response.

---




### **5. Operate the API**
1. **Start Flask App**:
   ```bash
   pip install -r requirements.txt
   python app.py
