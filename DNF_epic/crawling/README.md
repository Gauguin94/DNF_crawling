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
>  dunfamoa class는 loadAdv, loadChar, saveServer, saveCharinfo, run 메소드로 구성되어 있다.  
>     
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
from json import loads
from .consts import*

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
