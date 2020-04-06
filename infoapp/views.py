from django.shortcuts import render
import pandas
# Create your views here.
import requests
from sklearn import linear_model

import seaborn as sns;

sns.set()
import matplotlib.pyplot as plt

df = pandas.read_csv(
    "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo&datatype=csv")
print(df)
test = sns.lineplot(x='close', y='open', data=df)
test1 = sns.lineplot(x='close', y='low', data=df)
test2 = sns.lineplot(x='close', y='high', data=df)
# test = sns.lineplot(x='close', y='open',hue="event", style="event", data=df)
plt.ylabel('open high low')

plt.savefig('test.png')
X = df[['open', 'high', 'low']]
y = df['close']
print(X)
regr = linear_model.LinearRegression()
regr.fit(X, y)
close_price = regr.predict([[2300, 1300, 2562]])
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=2b6ff8726e6a4ab9b58670d54830bc34')
response = requests.get(url)


# print(response.json())


def index(request):
    template = 'infoapp/index.html'
    context = dict(response.json())
    return render(request, template, {'context': context})


def stockpredic(request):
    template = 'infoapp/stock.html'
    try:
        open = float(request.GET.get('open'))
        high = float(request.GET.get('high'))
        low = float(request.GET.get('low'))
        close_price = regr.predict([[open, high, low]])
    except:
        close_price = 0

    return render(request, template, {'close_price': close_price})
