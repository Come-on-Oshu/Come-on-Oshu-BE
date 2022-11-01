from bs4 import BeautifulSoup
from urllib.request import urlopen

# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response: #아래와 같은 의미
# response = urlopen('https://dpo.artdj.kr/dpo/?a_idx=01_01')
# soup = BeautifulSoup(response, 'html.parser')
# for anchor in soup.find_all(attrs={'id':'txt_box'}):
#     print(anchor.get('table'))

#select('div.contt div')

# selenium 불러오기
from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# chrome창(웹드라이버) 열기
driver = set_chrome_driver()

# 실행할 웹페이지 불러오기(구글 지도 예시)
driver.get("https://dpo.artdj.kr/dpo/?a_idx=01_01")

driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.sub_calendar_month_box > ul > li > a')

for n in notices:
    print(n)