import pandas as pd
import requests

API_URL = "https://corona.lmao.ninja/v2/countries?yesterday&sort"
response = requests.get(API_URL)
data = response.json()
df = pd.DataFrame(data)
df.to_csv("Data.csv", index=False)
