# %% [markdown]
# 잔재미코딩
# Xpath를 이용한 뉴스 크롤링
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 드라이버 생성
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('chromedriver', options=options)

# driver.get('http://127.0.0.1:5500/index.html')
driver.get(
    'https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html')

# %% [markdown]
# 최초 발견한 태그만 검색
# title = driver.find_element_by_tag_name('h3')
# print(title.text)
title = driver.find_element_by_xpath(
    '/html/body/div/div[1]/nav/ul/li[1]/ul')

# /html/body/div/div[1]/nav/ul/li[1]/ul/li[1]/a
# /html/body/div/div[1]/nav/ul/li[1]/ul/li[2]/a
# /html/body/div/div[1]/nav/ul/li[1]/ul/li[4]/a
# %% [markdown]
for p in title.find_elements_by_tag_name('a'):
    print(p.text)
# %%
# /html/body/p[2]
