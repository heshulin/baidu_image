import requests
import re
import os
from urllib import parse

class your_name_filter:
    __photo_url=""
    def pull_photo(self,photoname):
        photoname = photoname.encode('utf-8')
        photoname = parse.quote(photoname)
        url = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&' \
              r'fm=detail&fr=&sf=1&fmq=1447473655189_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&' \
              r'face=0&istype=2&ie=utf-8&word='+photoname
        html = requests.get(url).text
        urls = re.findall(r'"objURL":"(.*?)"', html)
        flag=1
        for url in urls:
            try:
                res = requests.get(url)
                if str(res.status_code)[0] == "4":
                    print("未成功：", url)
                    flag=0
                    continue
            except Exception as e:
                flag = 0
                print("未成功：", url)

            if(flag==1):
                self.__photo_url = url
                break

  #得到处理完图片的URL
    def get_yourname_url(self):
        return self.__photo_url

your_name_filter.pull_photo(your_name_filter,"内蒙古大学")
print(your_name_filter.get_yourname_url(your_name_filter))
