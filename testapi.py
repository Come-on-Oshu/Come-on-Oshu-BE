# 라이브러리 import
import requests
import pprint
import json
import secret

# url 입력
url = 'http://apis.data.go.kr/6300000/festivalDaejeonService/festivalDaejeonList'

api_key = requests.utils.unquote(secret.key)
params = {'serviceKey': api_key, 'pageNo' : 1, 'numOfRows' : 10}

# url 불러오기
response = requests.get(url, params=params)

#데이터 값 출력해보기
contents = response.text

# 데이터 결과값 예쁘게 출력해주는 코드
pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))