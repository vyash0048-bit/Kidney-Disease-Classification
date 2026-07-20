# Kidney-Disease-Classification

**🔴 Live Demo:** [https://kidney-disease-classification-cp9h.onrender.com/](https://kidney-disease-classification-cp9h.onrender.com/)

An End-to-End Deep Learning project utilizing a VGG16 CNN architecture to classify Kidney CT Scans into four categories: **Cyst, Normal, Stone, and Tumor**.

## 🚀 Features
- **VGG16 Architecture:** Utilizes transfer learning with a custom densely connected classifier head.
- **DVC Pipeline:** Fully reproducible MLOps pipeline covering Data Ingestion, Base Model Preparation, Training, and Evaluation.
- **MLflow Tracking:** Logs experiment parameters, metrics (accuracy, loss), and model artifacts to DagsHub.
- **Web Interface:** Built with Flask, featuring a modern, premium, drag-and-drop glassmorphism UI.
- **Production Ready:** Stripped down lightweight container deployed to Render via Docker.

## 💻 Tech Stack
- **Deep Learning:** TensorFlow & Keras
- **Web Framework:** Flask
- **MLOps:** DVC, MLflow, DagsHub
- **Deployment:** Render (Dockerized)

## 🛠️ Local Setup
1. Clone the repository
2. Create a virtual environment (`python -m venv .venv`) and activate it
3. Install dependencies: `pip install -r requirements.txt` (Note: if you wish to run the training pipeline, you will need to add `dvc`, `mlflow`, `pandas`, and `scipy` back to your requirements).
4. Run the web application: `python app.py`
5. Navigate to `http://localhost:8080` in your browser.