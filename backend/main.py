import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import json

load_dotenv() # Used for local testing with a .env file

app = Flask(__name__)
# Allow requests from your deployed frontend
CORS(app) 

# Configure the Gemini API using the secret from Secret Manager
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    model = None

@app.route('/generate', methods=['POST'])
def generate_careers():
    if model is None:
        return jsonify({"error": "AI model not configured correctly"}), 500
    
    try:
        data = request.json
        subjects = data.get('subjects')
        interests = data.get('interests')

        if not subjects or not interests:
            return jsonify({"error": "Subjects and interests cannot be empty"}), 400

        prompt = f"""
        Act as an expert career advisor for a student in India.
        The student's main subjects are: {subjects}.
        Their personal interests are: {interests}.

        Based on this, suggest 3 diverse career paths. For each career, provide:
        1. A "title".
        2. A short "description" (2 sentences).
        3. A list of 3 essential "skills" needed.

        Return the response ONLY as a valid JSON object in the following format:
        {{
          "recommendations": [
            {{
              "title": "Career Title",
              "description": "Short description.",
              "skills": ["Skill 1", "Skill 2", "Skill 3"]
            }}
          ]
        }}
        """

        response = model.generate_content(prompt)
        
        # Clean the response text to ensure it's valid JSON
        cleaned_response_text = response.text.strip().replace("```json", "").replace("```", "")
        
        # Validate that the cleaned text is proper JSON before returning
        json.loads(cleaned_response_text) # This will raise an error if it's not valid JSON
        
        return cleaned_response_text, 200, {'Content-Type': 'application/json'}

    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from AI response")
        return jsonify({"error": "Received an invalid response from the AI model"}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred on the server"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)