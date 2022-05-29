# consts.py
```python
APIKEY = '당신의 API key를 입력하세요'
SERVER = 'all'
ALLSERVER = ['cain/', 'diregie/', 'siroco/', 'prey/', 'casillas/', 'hilder/', 'anton/', 'bakal/']
RAW_URL = 'https://dunfamoa.com'
FWLV = 100
```
>   
> http request와 로그 저장에 쓰일 const들을 모아놓은 파일.  
>   
# dfmoa.py
>   
> dunfamoa class는 loadAdv, loadChar, saveServer, saveCharinfo, run 메소드로 구성되어 있다.  
>     
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
from json import loads
from .consts import*

class dunfaMoa:
    def __init__(self, search_url, num):
        self.search_url = search_url
        self.filename = num
        
    def loadAdv(self):
        adv_url = []
        href_info = []
        sourcecode = urlopen(self.search_url, context=context, timeout = 600).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        for href in soup.find("div", class_="Wrapper-sc-1noqpd4-1 gfctoN").find_all("a"):
            href_info.append(href)
        for url in href_info:
            if 'href' in url.attrs and 'class' in url.attrs:
                if url.attrs['class'] == ['Row-sc-jrfk9d-1', 'hiKazl']:
                    adv_url.append(RAW_URL + url.attrs['href'])
```  
> HTTP client 역할을 수행할 수 있는 라이브러리 중 하나인 urllib를 사용한다.  
> client란 고객, 즉, 서비스(데이터)를 요청(Request)하는 역할을 하며  
> server가 이 요청(Request)을 받아들여 응답(Response)을 한다. (요청한 데이터를 보내준다.)  
> 'href'와 'a'를 찾아 원하는 것을 추출한다.  
> \<a\>는 anchor, 즉, 닻을 의미하고 \<href\>는 URL을 의미한다.  
> 그렇다면 \<a href = "주소"\>가 의미하는 것은  
> 우리가 웹(바다) 서핑(surfing:파도타기)을 할 때, 닻을 내려 해당 주소에 정박하겠다는 의미가 된다.  
> adv_url.append(RAW_URL + url.attrs['href']) 을 통해 모험단에 매칭되는 주소들을 리스트로 저장한다.  
> (RAW_URL은 consts.py에서 선언한 const.)  
>   
```python
    def loadChar(self, adv_url):
        adv_link = []
        char_info = []
        for url in adv_url:
            try:
                sourcecode = urlopen(url, context=context, timeout = 600).read()
                soup = BeautifulSoup(sourcecode, "html.parser")
                for href in soup.find("div", class_ = 'Outer-sc-1cu42wh-3 kCIUEG').find_all("a"):
                    adv_link.append(href)
                for data in adv_link:
                    if 'href' in data.attrs:
                        temp = data.attrs['href'].replace("/characters/", "")
                        temp = self.saveServer(temp)
                        char_info.append(temp)
            except:
                continue
        return char_info
```  
> 앞서 저장한 주소들로 던파모아의 모험단 페이지로 접속하여 서버와 캐릭터의 이름을 저장한다.  
>   
```python
    def saveCharinfo(self, char_name):
        f = open('/home/kkn/DNF_epic/crawling/dfmoa_list/{}.txt'.format(self.filename),'w')
        for name in char_name:
            f.write(str(name['characterName'])+'\n')
        f.close()
        return 0
```  
> 마지막으로 나중에 다시 요청할 수고를 덜기 위해 이를 txt파일로 저장한다.  
>    
```python
    def run(self):
        char_info = []
        adv_url = self.loadAdv()
        char_info.extend(self.loadChar(adv_url))
        self.saveCharinfo(char_info)
        return 0
```  
> run 메소드는 위의 메소드들을 차례로 실행하는 역할을 한다.  
>   
# filter.py
```python
class filtering:
    def __init__(self):
        pass
```  
>   
> filtering 클래스는 dataLoad, deldupl, getInfo, run 메소드로 구성되어 있다.
>   
```python
    def dataLoad(self):
        filelist = []
        rawlist = []
        filelist_ = os.listdir(path)
        for file in filelist_:
            if 'txt' in file:
                filelist.append(file)
        for txt in filelist:
            f = open(path + txt, 'r', encoding = 'UTF8')
            try:
                for index, raw in enumerate(f):
                    name = raw.replace("\n", "").strip()
                    rawlist.append(name)
                f.close()
            except:
                f.close()
                f = open(path + txt, 'r', encoding = 'cp949')
                for index, raw in enumerate(f):
                    name = raw.replace("\n", "").strip()
                    rawlist.append(name)
                f.close()
        charlist = self.deldupl(rawlist)
        return charlist
```  
>   
> dfmoa.py에서 저장한 캐릭터 이름들을 불러온다.  
>   
```python
    def deldupl(self, list):
        update_list = []
        for i, name in enumerate(list):
            if name not in update_list:
                update_list.append(name)
        return update_list
```  
>   
> 중복된 데이터를 걸러내주는 작업을 수행한다.  
>   

```python

    def getInfo(self):
        char_list = []
        error_count = 0
        decoded_list = self.dataLoad()
        http = urllib3.PoolManager()
        for time, hash in enumerate(decoded_list):
            try:
                url = 'https://api.neople.co.kr/df/servers/{}/characters?characterName={}&limit={}&wordType={}&apikey={}'\
                        .format('all', hash, '200', 'match', APIKEY)
                req = http.request('GET', url)
                search_info = loads(req.data.decode('utf-8'))
                if len(search_info['rows']) >= 1:
                    for individual_info in search_info['rows']:
                        if individual_info['level'] > FWLV:
                            char_list.append({"serverId":individual_info['serverId'], "characterId":individual_info['characterId'], "characterName":individual_info['characterName']})
                            print(time, individual_info['characterName'])
            except:
                error_count += 1
                print("API server down or Freak character. [Error Count : {}]".format(error_count))
        char_list = self.deldupl(char_list)
        filename = whatTime()
        f = open("/home/kkn/DNF_epic/data/{}_3.txt".format(filename),'w')
        for line in char_list:
            f.write(line['serverId']+" "+line['characterId']+" "+line['characterName']+'\n')
        f.close()
        print('Success! and Error count: {}'.format(error_count))
        return 0
```  
>   
