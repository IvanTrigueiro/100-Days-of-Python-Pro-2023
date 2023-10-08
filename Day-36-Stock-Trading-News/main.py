import os
import requests
from twilio.rest import Client

# from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_number = os.environ["TWILIO_NUMBER"]
my_number = os.environ["MY_NUMBER"]
news_api_key = os.environ["NEWS_API_KEY"]
alpha_vantage_api_key = os.environ["ALPHA_VANTAGE_API_KEY"]

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
alpha_vantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_vantage_api_key
}
alpha_vantage_response = requests.get("https://www.alphavantage.co/query", params=alpha_vantage_params)
data = alpha_vantage_response.json()["Time Series (Daily)"]

# Getting the keys from the json
data_keys = list(data.keys())
yesterday = data_keys[0]
day_before_yesterday = data_keys[1]

# Getting the closing prices
yesterday_close = float(data[yesterday]["4. close"])
day_before_yesterday_close = float(data[day_before_yesterday]["4. close"])

# Calculating the percentage change
percentage_change = abs(((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100)
if percentage_change > 3:
    # News Api
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    all_articles = news_response.json()["articles"]
    # Slice the first three articles
    three_articles = all_articles[:3]
    formatted_articles = [
        [f"Headline: {article['title']}\nBrief: {article['description']}" for article in three_articles]]
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_=f"+{twilio_number}",
            to=f"+{my_number}"
        )
