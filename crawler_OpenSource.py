import requests
import bs4
import time
import random
import pandas as pd

str = ['daily','weekly','monthly']
#按日、月、年不同排行榜爬取三个网页
for str1 in str:
    #根网页请求头
    headers = {
        'authority': 'github.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://github.com/',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '_gh_sess=VtMzgCqb8bpPln9z9HwK41decARAVRZ6fgJZ7EobUXfT4rD4GNTSh6Hbp2W5mESG7PlrxXc2dJqmpiPFSE25OuP8DoI07ADM9OVEnM0RJ1030pAq9YxJyxY0S8jGipOSJgSyJUrBkK1glrMCFMMblfklQvZWZBkkk8gNBJhSBpEeuPZ^%^2F8aKXvMQqcyDAVN3knG^%^2FOMc74W^%^2BfZ^%^2FAfwBj2rwVyxI^%^2BLqCnxSJsmo8l53x6HVxNAkeTdlWBeyzBfcemQeN5NoqF6bFa8Of^%^2BjkAWbZQA^%^3D^%^3D--D^%^2F5GtG7rlSh0kJ69--eDremcxpaWkXnc94dl9U^%^2FA^%^3D^%^3D; _octo=GH1.1.2086256431.1640709908; logged_in=no; tz=Asia^%^2FShanghai',
        'if-none-match': 'W/^\\^31a7eed40bdd84984ae3b0512357ccfc^\\^',
    }
    #请求根网页
    response = requests.get('https://github.com/trending?since='+ str1, headers=headers, verify=False, proxies={'http':'http://127.0.0.1:1086'})
    #设置最大retries数
    requests.DEFAULT_RETRIES = 5

    #生成bs4对象
    bsoup=bs4.BeautifulSoup(response.text,'lxml')

    if(response.status_code == 200):
        print("父网页请求成功!")

    #防止过多https链接导致爬虫失败
    s = requests.session()
    s.keep_alive = False

    #访问子网页
    title = bsoup.find_all('h1',class_='h3 lh-condensed')
    for ti in title:
        #拼接子网页URL
        a = ti.find('a').text.strip().replace("\n", "")
        b = "https://github.com/" + a.replace(" ","")
        #请求子网页
        headers1 = {
            'authority': 'github.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '^\\^',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '^\\^Windows^\\^',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://github.com/trending',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '_gh_sess=VtMzgCqb8bpPln9z9HwK41decARAVRZ6fgJZ7EobUXfT4rD4GNTSh6Hbp2W5mESG7PlrxXc2dJqmpiPFSE25OuP8DoI07ADM9OVEnM0RJ1030pAq9YxJyxY0S8jGipOSJgSyJUrBkK1glrMCFMMblfklQvZWZBkkk8gNBJhSBpEeuPZ^%^2F8aKXvMQqcyDAVN3knG^%^2FOMc74W^%^2BfZ^%^2FAfwBj2rwVyxI^%^2BLqCnxSJsmo8l53x6HVxNAkeTdlWBeyzBfcemQeN5NoqF6bFa8Of^%^2BjkAWbZQA^%^3D^%^3D--D^%^2F5GtG7rlSh0kJ69--eDremcxpaWkXnc94dl9U^%^2FA^%^3D^%^3D; _octo=GH1.1.2086256431.1640709908; logged_in=no; tz=Asia^%^2FShanghai',
        }
        response = requests.get(str(b), headers=headers1, verify=False, proxies={'http':'http://127.0.0.1:1086'})

        if(response.status_code == 200): #子网页请求成功!
            print("request successfully!")
            c = str(a.replace(" ","").replace('/','_'))
            #保存子网页
            with open(c +".html",'w',encoding = 'utf-8') as f:
                f.write(response.text)

            #保存项目的相关信息
            project_info= []

            soup=bs4.BeautifulSoup(response.text,'lxml')

            texts = soup.find_all('div', class_='BorderGrid-row hide-sm hide-md')
            for a_text in texts:
                #保存项目的描述信息
                title = a_text.find('p',class_="f4 my-3")
                if(title == None):
                    print(1)
                else:
                    title = title.text.strip().replace("\n", "")
                    print(title)

                #保存项目基本信息
                info_list=[]

                info = a_text.find_all('div',class_="mt-2")

                for info1 in info:
                    info2 = info1.text.strip().replace("\n", "").replace(" ", "")
                    info_list.append(info2)
            
                #防止项目信息不全意外报错
                i = 0
        
                if(info_list[i][-4:]=='adme'):
                    readme = info_list[i]
                    i = i + 1
                else:
                    readme = 'null'
                if(info_list[i][-4:]=='ense'):
                    license = info_list[i]
                    i = i + 1
                else:
                    license = 'null'
                if(info_list[i][-4:]=="duct"):
                    conduct = info_list[i]
                    i = i + 1
                else:
                    conduct = 'null'

                if(info_list[i][-4:]=='tars'):
                    stars = info_list[i]
                    i = i + 1
                else:
                    stars = 'null'
                if(info_list[i][-4:]=='hing'):
                    watch = info_list[i]
                    i = i + 1
                else:
                    watch = 'null'
                if(info_list[i][-4:]=='orks'):
                    share = info_list[i]
                    i = i + 1
                else:
                    share = 'null'

                languages = soup.find_all('ul', class_='list-style-none')
                #保存项目所使用语言信息
                language_info = []
                for language in languages:
                    language1 = language.find_all('li',class_='d-inline')
                    for language2 in language1:
                        #存在项目所使用语言信息则加入language_info中
                        if(language2 != None):
                            language_info.append(language2.text.strip().replace("\n", ""))

                #按需构建DataFrame
                if(len(language_info)==0):
                    pd1= pd.DataFrame({'title': title, 'readme': readme, 'license': license, 'conduct': conduct,
                    'stars': stars, 'watch': watch, 'share': share, },index=[0])
                elif(len(language_info)==1):
                    pd1= pd.DataFrame({'title': title, 'readme': readme, 'license': license, 'conduct': conduct,
                    'stars': stars, 'watch': watch, 'share': share, 'language1': language_info[0], },index=[0])
                elif(len(language_info)==2):
                    pd1= pd.DataFrame({'title': title, 'readme': readme, 'license': license, 'conduct': conduct,
                    'stars': stars, 'watch': watch, 'share': share, 'language1': language_info[0],  'language2': language_info[1], },index=[0])
                elif(len(language_info)==3):
                    pd1= pd.DataFrame({'title': title, 'readme': readme, 'license': license, 'conduct': conduct,
                    'stars': stars, 'watch': watch, 'share': share, 'language1': language_info[0],  'language2': language_info[1], 'language3': language_info[2]
                    },index=[0])
                elif(len(language_info)==4):
                    pd1= pd.DataFrame({'title': title, 'readme': readme, 'license': license, 'conduct': conduct,
                    'stars': stars, 'watch': watch, 'share': share, 'language1': language_info[0],  'language2': language_info[1], 'language3': language_info[2]
                    , 'language4': language_info[3]},index=[0])
                elif(len(language_info)==5):
                    pd1= pd.DataFrame({'title': title, 'readme': readme, 'license': license, 'conduct': conduct,
                    'stars': stars, 'watch': watch, 'share': share, 'language1': language_info[0],  'language2': language_info[1], 'language3': language_info[2]
                    , 'language4': language_info[3], 'language5': language_info[4]},index=[0])

                project_info.append(pd1)

            #设置爬取休眠时间
            second=random.randrange(3,5)
            time.sleep(second)
        else: #请求子网页失败！
            print("error!")


    #数据持久化处理
    project_info2=pd.concat(project_info)
    project_info2.to_excel('project_info_'+str1+'.xlsx',index=False)