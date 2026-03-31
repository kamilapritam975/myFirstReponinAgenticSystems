import requests

# API URL
url = "https://api.github.com/search/repositories"

# Query parameters
params = {
    "q": "python",        # search keyword
    "sort": "stars",      # sort by stars
    "order": "desc",      # descending order
    "per_page": 5         # limit to 5 results
}

# API request
response = requests.get(url, params=params)

# Convert response to JSON
data = response.json()

# Extract and print data
for repo in data["items"]:
    print("Repository Name:", repo["name"])
    print("Stars:", repo["stargazers_count"])
    print("-" * 30)