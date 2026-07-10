# How to Run the Civil Engineering Insight Studio

Follow these steps to run the Streamlit application on your machine:

### 1. Prerequisites
Ensure you have Python (3.7 or higher) installed on your system.

### 2. Setup the Virtual Environment
Open your terminal or command prompt in the project root directory and run:
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
Navigate to the "7. Project Demonstration" directory where the requirements are located, and install them:
```bash
cd "7. Project Demonstration"
pip install -r requirements.txt
```

### 5. Setup your API Key
Ensure you have your `.env` file set up in the "7. Project Demonstration" directory. It should look like this:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

### 6. Run the Application
Finally, start the Streamlit server:
```bash
streamlit run app.py
```
The application will automatically open in your default web browser (usually at http://localhost:8501).
