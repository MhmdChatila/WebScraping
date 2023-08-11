import requests
from bs4 import BeautifulSoup

URL = "https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en?region=LB"
headers= {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}
respones = requests.get(URL,headers=headers)
soup = BeautifulSoup(respones.text,'lxml')

# Find elements that have any of the specified classes
data = soup.find('div',class_=[
    'CommonGridLayoutDataList_listWrap__aDyjD',
    'index-mobile_listWrap__lcrSL',
    'TopadsList_topadsDataContentWrap__bZ3dt',
    'index-mobile_topadsDataContentWrap__4uruH',
])

print(data)

target_classes2 = [
    'CommonGridLayoutDataList_cardWrapper__jkA9g',
    'TopadsList_cardWrapper__9A7Uf',
    'index-mobile_cardWrapper__TEjKX',
]
if data:
    nested_divs = data.find_all('div',class_=target_classes2)
    for nested_div in nested_divs:
        a_tags = nested_div.find_all('a')
        for a_tag in a_tags:
            href = a_tag.get("href")
            if href:
                print(href)
else:
    print("Parent div not found.")