import json
import requests

def SendMessageWhatsapp(data):
    try:
        print(1)
        print(data)
        token ="EAANRHSoIIwMBO7ouaKaDrXCj4RFcK4v0IJHUZBZCqI2tv7amZBZCKUBxRvmDzorZAHk6gnwXvZB5nzl2HUcfJGg5VMvpAXEZB8fOWAXjohOLKt2aMhbDB5bqpXakb3LPjczRZAujKmBXZBC1FCyvTdORwyhRd2h30iyjgCkfOfy9kKeQYamkuAqluK5otzWRZBeZBtbWPIemg589vIW2ETWhBUZD"
        api_url = "https://graph.facebook.com/v17.0/106742419084377/messages"
        
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        print(2)
        response = requests.post(api_url, data = json.dumps(data), headers = headers)
        print(3)
        print(response)
        if response.status_code == 200:
            return True
        return False
    except Exception as exception:
        print(exception)
        return False
    
