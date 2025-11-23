# Skill Pilot AI 🚀

A generative AI-powered platform designed to provide personalized career and skills guidance for students in India. This project was built for the Gen AI Exchange Hackathon.

---
## 📜 Description

Skill Pilot AI addresses the critical gap between academic education and the demands of the modern job market. Instead of generic advice, our platform analyzes a student's unique profile—including their subjects and interests—to generate a hyper-personalized "Success Roadmap." This roadmap outlines suitable career paths and the specific, actionable skills required to succeed, empowering students to navigate their future with clarity and confidence.

---
## ✨ Features

-   **Personalized Profile Input:** A clean interface for students to enter their academic subjects and personal interests.
-   **AI-Powered Recommendations:** Leverages Google's Gemini 1.5 Pro model to generate diverse and relevant career suggestions.
-   **Detailed Skill Roadmaps:** Each recommendation includes a title, a concise description, and a list of essential skills to learn.
-   **Dynamic UI:** A responsive and professional user interface with clear loading and error states.

---
## 🚀 Live Demo

You can view the live deployed prototype here:
**[https://skill-pilot-frontend.vercel.app/](https://skillpilot-qi.vercel.app/)** 

---
## 🛠️ Technology Stack

* **Frontend:**
    * [React](https://reactjs.org/) (with Vite)
    * Custom CSS for styling
* **Backend:**
    * [Python](https://www.python.org/)
    * [Flask](https://flask.palletsprojects.com/) (as the web framework)
    * [Gunicorn](https://gunicorn.org/) (as the production server)
* **Cloud & AI:**
    * **AI Model:** Google Gemini 1.5 Pro
    * **Backend Hosting:** Google Cloud Run
    * **Frontend Hosting:** Vercel
    * **Secrets Management:** Google Cloud Secret Manager

---
## ⚙️ Setup and Installation

To run this project locally, you will need to have Node.js, Python, and the Google Cloud SDK installed.

### Prerequisites

* Node.js (v18+)
* Python (v3.9+)
* Google Cloud SDK
* Git

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your Gemini API Key for local testing:**
    * Create a file named `.env` in the `backend` folder.
    * Add your API key to it:
        ```
        GEMINI_API_KEY="your_api_key_here"
        ```
5.  **Run the local backend server:**
    ```bash
    flask run
    ```
    The backend will be running at `http://127.0.0.1:5000`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd skill-pilot-ai-frontend
    ```
2.  **Install dependencies:**
    ```bash
    npm install
    ```
3.  **Set up your backend URL for local testing:**
    * Create a file named `.env.local` in the `skill-pilot-ai-frontend` folder.
    * Add the address of your **deployed backend** (or local backend if you changed the port):
        ```
        VITE_REACT_APP_BACKEND_URL=[https://skill-pilot-backend-542975225491.asia-south1.run.app](https://skill-pilot-backend-542975225491.asia-south1.run.app)
        ```
4.  **Run the local frontend server:**
    ```bash
    npm run dev
    ```
    The frontend will be running at `http://localhost:5173`.

---
## ☁️ Deployment

### Backend (Google Cloud Run)

The backend is deployed as a container to Google Cloud Run. Ensure you have set up your `GEMINI_API_KEY` in Google Cloud Secret Manager first.
```bash
gcloud run deploy skill-pilot-backend --source . --region asia-south1 --allow-unauthenticated --update-secrets=GEMINI_API_KEY=GEMINI_API_KEY:latest
