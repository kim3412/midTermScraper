# import modules
# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import re # for regular expression
import urllib.parse # for decode url to korean
import csv
import codecs


# hashtag url
url = "https://www.instagram.com/explore/tags/%EB%A7%9B%EC%8A%A4%ED%83%80%EA%B7%B8%EB%9E%A8/?hl=ko"

# browser
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\selenium\\geckodriver.exe")
driver.implicitly_wait(3)
driver.get(url)

# get total number of posts for the hashtag
totalCount = driver.find_element_by_class_name('g47SY').text
print("총 게시물: ", totalCount)


# get urls on 9 popular posts
elem = driver.find_element_by_tag_name("body")

url_list = []
cnt = 0
pagedowns = 1
while pagedowns < 5:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    link = driver.find_elements_by_xpath('.//a')

    for i in link:
        tmp = i.get_attribute('href')
        cnt += 1
        url_list.append(tmp)
        if cnt >= 9:
            break
    if cnt >= 9:
        break
    pagedowns += 1


# get number of liked and hashtag list on above posts
dict_tag = {}
sumLike = 0
cnt = 0
for u in url_list:
    driver.get(u)
    sumLike += int(re.sub('[좋아요, 개]', '', driver.find_element_by_class_name('zV_Nj').text)) # delete not number letters
    print(sumLike)
    cnt += 1
    tag = driver.find_elements_by_xpath('.//a')

    # gather tags
    for t in tag:
        try:
            tagTmp = t.get_attribute('href')
        except StaleElementReferenceException:
            continue
        if tagTmp.find("https://www.instagram.com/explore/tags/") == -1:
            continue
        tagA = tagTmp.replace("https://www.instagram.com/explore/tags/", "")
        tagA = tagA.replace("/", "")
        tagA = urllib.parse.unquote(tagA)
        if tagA not in dict_tag:
            dict_tag[tagA] = 0
        dict_tag[tagA] += 1

print("인기 게시물 좋아요 수 평균: ", sumLike/cnt)



# 한글 인코딩 
# UnicodeEncodeError: 'euc_kr' codec can't encode character '\xfc' in position 2: illegal multibyte sequence

# w = csv.writer(codecs.open("D:\\BigData\\midTerm\\hashtag.csv", 'w', encoding='euc_kr'))
# for k, v in dict_tag.items():
#     w.writerow([k, v])
### save
"""
keys = sorted(dict_data.items(), key=lambda x:x[1], reverse=True)

for k, v in keys[:15]:
    print("{}(){}".format(k, v))
"""
driver.close()
