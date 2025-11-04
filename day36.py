import requests
import os
from datetime import datetime, timedelta


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_endpoint = "https://www.alphavantage.co/query"
# set up environment variable -- export AP_STOCK_API=<AP's AlphaVantage API key>
# DO THIS before running this .py!!!
# API key is found in the usual places.. HISSSSTTTT HIST...careful!
stock_api_key = os.environ.get("AP_STOCK_API")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}
#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
response = requests.get(stock_endpoint, params=stock_params)
response.raise_for_status()
stock_data = response.json()
#print(stock_data)
# yesterday_close = float(stock_data["Time Series (Daily)"]["2025-10-31"]["4. close"])
# print(yesterday_close)
day_counter = 0
last_work_day_close = 0.0
day_before_close = 0.0

for date, details in stock_data["Time Series (Daily)"].items():
    #open_price = details["1. open"]
    close_price = float(details["4. close"])
    #print(f"Date: {date}, Open: {open_price}, Close: {close_price}")
    day_counter += 1
    if day_counter == 1:
        last_work_day_close = close_price
    elif day_counter == 2:
        day_before_close = close_price
    
    if day_counter == 2:
        break

print(f"Last working day's close price: {last_work_day_close}")
print(f"The day BEFORE the last working day's close prices: {day_before_close}")

# Testing.. hard-coding the close prices so that percent change is definitely more/less than +/- 5%!!!
# last_work_day_close = 109.00
# day_before_close = 100.00

percent_price_change = ((last_work_day_close - day_before_close) / day_before_close) * 100

if (percent_price_change >= 5.00) or (percent_price_change <= -5.00):
    #print("Get News!!")
    news_endpoint = "https://newsapi.org/v2/everything"
    # set up environment variable -- export AP_NEWS_API=<AP's NewsAPI.org API key>
    # DO THIS before running this .py!!!
    # API key is found in the usual places.. HISSSSTTTT HIST...careful!
    news_api_key = os.environ.get("AP_NEWS_API")
    news_params = {
        "qInTitle": COMPANY_NAME,
        "from": (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'),  # Dynamically determining last 7 days time window
        "sortBy": "popularity",
        "apiKey": news_api_key
    }

    # print(f'The from date is: {news_params["from"]}')

    response = requests.get(news_endpoint, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    #print(news_data)
    num_articles = news_data["totalResults"]
    if num_articles == 0:
        print(f"No articles have been published for: {COMPANY_NAME}")
    else:
        articles = news_data["articles"]
        # use Python slice operator to create a list that contains the first 3
        # articles ONLY
        three_articles = articles[:3]
        print(three_articles)
        # Below lines of code was my ORIG attempt! It works 100%
        # article_count = 0
        # for article in news_data["articles"]:
        #     article_count += 1
        #     # Instead of sending SMS or WhatsApp msgs thru Twilio, I am
        #     # just printing it out to the console. --AP Nov 3, 2025
        #     print(article["title"])
        #     print(article["description"])
        #     if article_count >= 3:
        #         break
        

else:
    print("Percent difference is UNDER plus/minus 5 per cent... No news to get!!")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

