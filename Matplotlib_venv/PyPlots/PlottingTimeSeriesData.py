from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd
from datetime import datetime, timedelta

plt.style.use('seaborn')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

# Time Series Plot 1
# plt.plot_date(dates, y, linestyle='solid', linewidth=1, marker=None)
# plt.gcf().autofmt_xdate()
#
# date_format = mpl_dates.DateFormatter('%b, %d, %Y')
# plt.gca().xaxis.set_major_formatter(date_format)

# Time Series Plot 2
df = pd.read_csv('../DataFiles/bitcoin_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

price_date = df['Date']
price_close = df['Close']

plt.plot_date(price_date, price_close, linestyle='solid',
              linewidth=1, marker=None)
plt.gcf().autofmt_xdate()

plt.legend()
plt.title('BitCoin Price Trend')
plt.xlabel('Dates')
plt.ylabel('Closing Price')
plt.tight_layout()
plt.show()
