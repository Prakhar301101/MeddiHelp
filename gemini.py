from dotenv import load_dotenv
import os
import google.generativeai as genai
import requests

# Initial prompt customized for PillPaw
preLoadData = """You are PillPaw, a medical help assistant. Provide short, direct answers in simple, plain text to questions specifically related to health, symptoms, wellness, and general medical advice. Keep responses to a maximum of 2-3 sentences. If the user asks about something unrelated, politely inform them that you can only provide health-related information."""

class PillPawChatbot:
    def __init__(self):
        print("""Hi! This is PillPaw, your virtual assistant for general medical inquiries.
Please remember to create a .env file and set your GOOGLE_API_KEY environment variable before using this program.
Thank you!
================= Start Your Query =================""")
        load_dotenv()  # Load environment variables from .env file
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            print("Invalid/No API Key in .env file")
            return

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat(history=[])

    def check_internet_connection(self):
        try:
            requests.get("https://www.google.com", timeout=1)
            return True
        except requests.ConnectionError:
            return False

    def get_pillpaw_response(self, user_message):
        # Prompt with medical focus for PillPaw
        full_prompt = f"{preLoadData} User asked: '{user_message}' Please provide assistance."
        print(full_prompt)
        if not self.check_internet_connection():
            return {"message": "Sorry, can't connect to the internet. Please check your connection."}

        response = self.chat.send_message(full_prompt, stream=True)

        # Collect and process the response text
        response_text = ""
        for chunk in response:
            if hasattr(chunk, 'safety_ratings'):
                print(f"Safety Ratings: {chunk.safety_ratings}")  # Log safety ratings
            if hasattr(chunk, 'text'):
                response_text += chunk.text

        # Ensure we return a coherent message
        if response_text:
            return {"message": response_text.strip()}
        
        return {"message": "No valid response received from the AI model."}
