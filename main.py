import pandas as pd
import requests

API_URL = "https://corona.lmao.ninja/v2/countries?yesterday&sort"


def get_covid_csv(URL: str) -> None:
    response = requests.get(API_URL)
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv("Data.csv", index=False)


if __name__ == "__main__":
    get_covid_csv(API_URL)
