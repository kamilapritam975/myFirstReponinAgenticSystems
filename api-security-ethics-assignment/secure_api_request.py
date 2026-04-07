import os
import requests

# Step 1: Get API key from environment variable
api_key = os.getenv("API_KEY")

if not api_key:
    print("API key not found. Please set the API_KEY environment variable.")
    exit()

# Step 2: API endpoint
url = "https://api.example.com/data"

# Step 3: Headers with Authorization Bearer
headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    # Step 4: Send GET request
    response = requests.get(url, headers=headers)

    # Step 5: Handle status codes
    if response.status_code == 200:
        print(response.json())
    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")