import requests
from bs4 import BeautifulSoup
from time import sleep
from requests_html import HTMLSession

URL = "https://ads.tiktok.com/business/creativecenter/inspiration/topads/pad/en?region=LB"
s = HTMLSession()
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

response = s.get(URL, headers=headers)
response.html.render(sleep=3)

vids = response.html.xpath('//*[@id="ccContentContainer"]/div[2]/div/div[2]/div[1]/div[1]',first=True)

for items in vids.absolute_links:
    print(items)