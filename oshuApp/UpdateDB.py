import requests
import secret
from datetime import date, timedelta
from dateutil import relativedelta

# find the first and last date based on current date
today = date.today()

stDate = today.replace(day=1)
nextenDate = stDate + relativedelta.relativedelta(months=1)
edDate = nextenDate - timedelta(days=1)

stDate = stDate.strftime('%Y%m%d')
edDate = edDate.strftime('%Y%m%d')

# open api url
url = 'http://www.kopis.or.kr/openApi/restful/pblprfr'

# open api request parameters
params = {'service': secret.key, 'stdate': stDate, 'eddate': edDate, 'cpage': 1, 'rows': 50, 'prfstate': '01', 'signgucode' : 30}

# open api request
response = requests.get(url, params = params)

#print
contents = response.text
print(contents)
