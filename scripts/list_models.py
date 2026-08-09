from google import genai
import os

api_key = "AQ.Ab8RN6KVl1L-xvHCLsfCo8vNL9ZrLruUk4tAlz3b_AnILc-7Qw"
client = genai.Client(api_key=api_key)

print("Listing available models...")
try:
    for model in client.models.list():
        print(model.name)
except Exception as e:
    print(f"Failed to list models: {e}")
