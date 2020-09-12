# 잔재미코딩
# Xpath를 이용한 뉴스 크롤링
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
# chromedriver = 'C:/dev_python/Webdriver/chromedriver.exe' # 윈도우
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('window-size=1920x1080')
option.add_argument('disable-gpu')
driver = webdriver.Chrome('chromedriver', chrome_options=option)

driver.get('http://v.media.daum.net/v/20170922175202762')

# 최초 발견한 태그만 검색
# title = driver.find_element_by_tag_name('h3')
# print(title.text)
title = driver.find_element_by_xpath(
    '//*[@id="harmonyContainer"]')

for p in title.find_elements_by_tag_name('p'):
    print(p.text)

driver.quit()
