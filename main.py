import translators as ts


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "MSTFE8SBM0PKJMUG"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
data_name = ""
data_money = ""
data_exchange = 0
tester = 1888.65
namer = []
stop = 0
news = []
news_tr = []
inc = 0
dnc = 0
import requests




dats = requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=5946ea1d0cd84f6fbaa53947e48dfa42")
json_data = dats.json()
for abc in range(100):
    name = json_data["articles"][abc]["source"]["id"]
    if name == "google-news" and stop < 3:
        title = json_data["articles"][abc]["title"]
        news.append(title)
        stop += 1

parameters = {
    "function":"CURRENCY_EXCHANGE_RATE",
    "from_currency":"ETH",
    "to_currency":"USD",
    "apikey":API_KEY

}

def finder():
    global data_name, data_money, data_exchange
    data = requests.get("https://www.alphavantage.co/query",params=parameters).json()
    data_name = data["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
    data_money = data["Realtime Currency Exchange Rate"]["3. To_Currency Code"]
    data_exchange = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return data_name, data_money, data_exchange


finder()

print(data_exchange)

#print(float(data_exchange)/ tester)
######### INCREASES - DECREASES #########
def increase():
    global inc, dnc
    if float(data_exchange) > tester:
        inc = int(100*(float(data_exchange)/tester)) - 100
        #print(f"inc{inc}")
        return inc
    elif tester >= float(data_exchange):
        dnc = int(100 * (tester / float(data_exchange))) - 100
        #print(f"dnc{dnc}")
        return dnc
    else:
        pass

increase()

#######TESTER EQUALER##########
def equal():
    global tester
    tester = float(data_exchange)
    return tester

equal()
print(inc)
print(dnc)
print(tester)

##### NEWS#####
for a in range(3):
    q_text = news[a]
    news_tr.append(ts.translate_text(query_text=q_text,to_language="tr"))

if inc > 0:
    percent = f"🔺 {inc}% "
else:
    percent = f"🔻 {dnc}% "

#print(percent)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.







## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

from twilio.rest import Client


account_sid = 'ACe9cc4d4cebb0eaf3813f2df871558dd9'
auth_token = '5850958c147eeb9a442ba06294258821'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18144812129',
  body=f"\nETH: {percent} \nCoin piyasasi hakkinda sizin icin 3 tane de haber derledik, haberin"
       f" tüm icerigine web sitesinden ulasabilirsiniz.\n {news_tr}",
  to='+4917674580118')

print(message.sid)




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

