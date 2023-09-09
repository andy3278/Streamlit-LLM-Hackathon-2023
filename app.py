from dotenv import load_dotenv
import os

load_dotenv()

api_secret = os.getenv("Llama-2-13b-hf-secret")

import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-13b-hf"
headers = {"Authorization": "Bearer " + api_secret}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})
print(output)