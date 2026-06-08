# 🏡 House Price Predictor Web App

A clean, modern, single-page web application that uses a trained **K-Nearest Neighbors (KNN) Regressor** model to predict property values based on housing metrics. Built using **Flask** and styled dynamically with **Tailwind CSS**, this project is configured for seamless deployment on **Render**.

---

## 🚀 Live Demo

You can interact with the live deployed version of this application here:
👉 **[(https://house-price-predictor-deploy-on-render.onrender.com)]**

---

## ✨ Features

* **Single-File Setup:** Runs the backend and embeds the frontend interface entirely inside `app.py`, making it perfect for rapid deployment.
* **Self-Generating Artifacts:** When `app.py` is executed locally, it automatically outputs the production-ready `requirements.txt` and this `README.md` file directly to your workspace.
* **Modern UI:** Responsive dashboard designed with Tailwind CSS, supporting seamless desktop and mobile experiences.
* **State Retention:** The form retains user-inputted values after running a prediction, preventing the need to re-type data.

---

## 📊 Model Inputs

The underlying KNN machine learning model (`KNN_HP.pkl`) evaluates five specific features to compute a valuation:

1.  **Bedrooms (`beds`):** Total count of bedrooms.
2.  **Bathrooms (`baths`):** Total count of bathrooms (supports fractional values like 2.5).
3.  **Property Size (`size`):** Total living area in square feet.
4.  **Lot Size (`lot_size`):** Total lot/land area in square feet.
5.  **Zip Code (`zip_code`):** Local regional area classification code.

---

## 💻 Local Setup Instructions

To run this project locally on your machine, follow these steps:

1. **Clone or create a directory:**
   Create a project directory and place your pre-trained `KNN_HP.pkl` model file inside it.

2. **Create the application script:**
   Save the full combined Python script as `app.py` in that same directory.

3. **Install the dependencies:**
   Run the application once to auto-generate the file, or manually install them:
   ```bash
   pip install Flask==3.0.3 scikit-learn==1.6.1 numpy==2.0.0 gunicorn==22.0.0

4. **Run the application:**
  Bash
  python app.py
  
  Access the app:
  Open your browser and navigate to http://127.0.0.1:5000.

---

## ☁️ ** How to Deploy on Render**

This project is built to deploy out of the box on Render.

1. Push your repository files (app.py, requirements.txt, and KNN_HP.pkl) to a GitHub repository.

2. Log into your Render Dashboard and click New + -> Web Service.

3. Connect your GitHub repository.

4. Configure the Web Service settings with the following parameters:

    Runtime: Python
    
    Build Command: pip install -r requirements.txt
    
    Start Command: gunicorn app:app

 5. Click Deploy Web Service. Render will build your application container and provide a live URL!

---
## 📄 **License**
This project is open-source and available under the MIT License.
