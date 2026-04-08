import requests
import pandas as pd

def get_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data)

    # Cleaning
    df.rename(columns={"userId": "user_id"}, inplace=True)
    df.drop(columns=["id"], inplace=True)

    # New column: post length
    df["post_length"] = df["body"].apply(len)

    return df