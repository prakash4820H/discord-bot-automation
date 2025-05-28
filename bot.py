import os
import time
import requests
import datetime

def send_discord_message(content):
    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        print("Error: DISCORD_TOKEN environment variable not found")
        return False
    
    url = "https://discord.com/api/v9/channels/690995280228646963/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {"content": content}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Sent '{content}' - Status Code: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error sending '{content}': {e}")
        return False

if __name__ == "__main__":
    # Define commands to run in sequence
    commands = [",work", ",crime", ",collect", ",dep all"]
    
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Starting Discord command sequence at {current_time}")
    
    # Execute each command with a 5-second delay
    for command in commands:
        success = send_discord_message(command)
        if not success:
            print(f"Failed to send command: {command}")
        time.sleep(5)  # Wait 5 seconds between commands
    
    print("Command sequence completed") 