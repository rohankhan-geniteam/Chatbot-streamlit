import requests
import json

def get_chatbot_response(user_input):
    api_url = "https://stitch-warm-clef.glitch.me/chat"
    payload = {'message': user_input}
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return response.json().get("response", "Sorry, I couldn't process your message.")
        else:
            return "Error communicating with the API."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
