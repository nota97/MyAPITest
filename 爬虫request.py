import requests
from lxml import etree
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

temp_url = 'https://www.qiushibaike.com/8hr/page/'
for i in range(1, 2):
    url = temp_url + str(i)
    response = requests.get(url, headers=headers)
    html = response.content
    element = etree.HTML(html)
    lst = element.xpath('//div[@class="recmd-right"]/a/text()')
    lst1=element.xpath('//div[@class="recmd-num"]/span/text()')
    lst2=element.xpath('//div[@class="recmd-detail clearfix"]/a/span/text()')
    img=element.xpath('//div[@class="recmd-detail clearfix"]/a/img/@src')
    for j in range(len(lst2)):
        print("第" + str(i) + "页第" + str(j + 1) + "个段子，标题是：")
        content = lst[j]
        content = content.replace('\n', '')
        content = content.replace('<br/>', '\n')

        author = lst2[j]
        author = author.replace('\n', '')
        author = author.replace('<br/>', '\n')

        image = img[j]
        image = image.replace('\n', '')
        image = image.replace('<br/>', '\n')

        items = {
            'author': author,
            'image': str(image),
            'text': content,
            'zan': str(lst1[j*5]),
            'comments': str(lst1[j*5+3]),
        }
        print(items)
        with open("qiushi.json", 'a',encoding='utf-8') as f:
            f.write(json.dumps(items, ensure_ascii=False) + '\n')


# import requests
# from lxml import etree

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

# url="https://movie.douban.com/chart"

# response=requests.get(url,headers=headers)
# html=response.content.decode()
# element = etree.HTML(html)
# lst=element.xpath('//tr[@class="item"]')
# for i in lst:
#     name=i.xpath('td/div/a/text()')[0]
#     name=name.replace(" ","")
#     name=name.replace("\n","")
#     name=name.replace("/","")
#     print(name)

#     url=i.xpath('td/div/a/@href')[0]
#     print(url)
#     img=i.xpath('td/a/img/@src')[0]
#     print(img)
#     rating=i.xpath('td/div/div/span[@class="rating_nums"]/text()')[0]
#     print(rating)
#     pl=i.xpath('td/div/div/span[@class="pl"]/text()')[0]
#     print(pl)

