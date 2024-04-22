import requests
from bs4 import BeautifulSoup
import re
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
key=input("请输入你想爬的小说:")
url="https://www.readnovel.com/so/"+key
strhtml=requests.get(url,headers=headers).text
bs=BeautifulSoup(strhtml,"html.parser")
names=bs.select("h4")
authors=bs.find_all(attrs={"class":"name default"})
# for i in authors:
#     print(i.text)
updates=bs.find_all(attrs={"class":"update"})
# for i in updates:
#     print(i.text)
# names=re.findall('target="_blank">(.*?)<',str(names))
i=0
for name in names:
    if i>=7:
        break
    name=str(name)
    name=name.replace('<cite class="red-kw">','')
    name=name.replace('</cite>', '')
    name=re.findall('target="_blank">(.*?)<',name)
    print(str(i)+str(name),end="   ")
    print(authors[i].text,end="   ")
    print(updates[i].text)
    i+=1
key = int(input("请从0-6选择你要下载的小说:"))
while key<0 or key>6:
    key = input("输入错误,请重新输入:")
# print(names)
namess=re.findall('<a href="(.*?)" tar',str(names))
# i=0
# for name in names:
#     if i==key:
#         key=re.findall('<a href="(.*?)" tar',str(name))
#         break
#     i+=1
# print(key)
url="https://www.readnovel.com"+namess[key]+"#Catalog"
# print(url)
strhtml=requests.get(url,headers=headers).text
bs=BeautifulSoup(strhtml,"html.parser")
zj=bs.find_all(attrs={"class":"volume"})
zjnames=re.findall('target="_blank">(.*?)<',str(zj))
zjdzs=re.findall('href="(.*?)" tar',str(zj))
# print(zjnames)
# print(zjdzs)

with open('xiaoshuo.txt',mode='w',encoding='utf-8') as file:
    i=0
    for zjname in zjnames:
        file.write(str(zjname)+"\n\n")
        print(zjname)
        url="https://www.readnovel.com"+zjdzs[i]
        strhtml = requests.get(url, headers=headers).text
        bs = BeautifulSoup(strhtml, "html.parser")
        content = bs.find_all(attrs={"class": "ywskythunderfont"})
        content=str(content)
        content=content.replace("<p>","")
        content = content.replace("</p>", "")
        content=content[34:-338]
        # print(content)
        file.write(content+"\n\n")
        # print(content)
        # content=str(content)
        # print(content)
        # content=content[:-700]
        # print(content)
        # con=re.findall('"ywskythunderfont">(.*?)</p>',content)
        # con=str(con)
        # print(con)
        # con=con.replace("<p>","")
        # file.write(con)
        # print(con)
        i+=1


# url="https://www.readnovel.com"+



# class="ywskythunderfont"