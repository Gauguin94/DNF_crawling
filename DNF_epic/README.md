# run.py

> 우리는 최대한 많은 모험단을 찾아 로그를 수집해야 한다.  
```python
ADV_LETTER = [
    '%ec%82%ac%eb%9e%91', '%ea%b8%b0%ec%96%b5', '%ec%b6%94%ec%96%b5', '%ec%9d%b4%eb%b3%84', '%ec%a7%80%ec%a1%b4', '%ec%a0%84%ec%82%ac',\
    '%eb%a1%9c%ea%b7%b8', '%ec%8a%a4%ed%95%8f', '%ec%9d%b8%ed%8c%8c', '%ec%8a%a4%ec%bb%a4', '%ec%8a%a4%ed%8c%8c', '%eb%84%a8%eb%a7%88',\
    '%ea%b7%b8%ed%94%8c', '%ed%86%a0%eb%84%a4', '%ea%b8%b0%eb%a6%b0', '%ed%87%b4%eb%a7%88', '%ed%81%ac%eb%a3%a8', '%ec%96%b4%eb%b2%b5',\
    '%ed%99%80%eb%a6%ac', '%eb%b2%84%ed%94%84', '%eb%b2%84%ed%8d%bc', '%ed%8e%b8%ec%95%a0', '%eb%9d%bc%ed%95%8c', '%ec%9d%b4%eb%a6%84',\
    '%eb%8d%98%ed%8c%8c', '%eb%a7%88%ed%87%b4', '%eb%ac%bc%ed%87%b4', '%eb%ac%bc%ea%b3%b5', '%eb%a7%88%ea%b3%b5', '%ec%98%a4%ea%b3%b5',\
    '%ec%9e%a5%ea%b5%b0', '%ec%9e%a5%ea%b5%90', '%ec%82%ac%eb%a0%b9', '%ed%99%94%eb%a0%a5', '%eb%a7%88%eb%a0%a5', '%eb%a7%88%eb%b2%95',\
    '%ec%9a%b0%eb%9f%ad', '%eb%aa%a8%ea%b8%b0', '%eb%b0%94%eb%9e%8c', '%ec%82%ac%eb%9e%8c', '%eb%8b%88%ec%95%8c', '%eb%b0%94%ec%95%8c',\
    '%eb%94%94%ec%95%84', '%eb%a9%94%ed%94%bc', '%eb%af%b8%ec%b9%b4', '%ed%8b%b0%eb%a6%ac', '%ec%9e%84%ed%8e%98', '%eb%a7%90%ed%8b%b0',\
    '%ed%83%80%eb%9d%bd', '%ec%9e%90%eb%9e%91', '%ec%8b%a0%ed%99%94', '%ed%8c%8c%ec%9b%8c', '%eb%82%98%eb%9d%bd', '%eb%9d%b5%ec%a7%84',\
    '%eb%aa%85%ec%a7%84', '%ec%9c%a4%eb%aa%85', '%ec%9c%a4%eb%9d%b5', '%ed%8c%a8%ed%99%a9', '%ed%8c%a8%ec%99%95', '%ed%88%ac%ec%8b%a0',\
    '%eb%b2%9a%ea%bd%83', '%eb%82%98%ec%84%a0', '%eb%87%8c%ec%a0%88', '%eb%8b%8c%ec%9e%90', '%ed%83%88%ec%a3%bc', '%ea%b3%b5%ea%b2%a9',\
    '%ea%b7%80%ec%8b%a0', '%ea%b2%80%ec%8b%a0', '%eb%87%8c%ec%8b%a0', '%eb%a7%88%ec%8b%a0', '%eb%a7%88%ec%99%95', '%ec%a0%9c%ec%99%95',\
    '%ed%99%a9%ec%a0%9c', '%eb%8c%80%ec%99%95', '%eb%b8%9c%eb%af%b8', '%eb%b8%9d%eb%af%b8', '%ec%8a%a4%ed%83%80', '%ed%99%94%ec%8b%a0',\
    'god', 'black', 'dark', 'love', 'blue', 'red', 'yellow', 'green', 'sky', 'wind', 'water', 'fire', 'flame', 'bomb', 'air', 'hi', 'bye', 'iu', 'a'
]
# 사랑, 기억, 추억, 이별, 지존, 전사
# 로그, 스핏, 인파, 스커, 스파, 넨마
# 그플, 토네, 기린, 퇴마, 크루, 어벵
# 홀리, 버프, 버퍼, 편애, 라핌, 이름
# 던파, 마퇴, 물퇴, 물공, 마공, 오공
# 장군, 장교, 사령, 화력, 마력, 마법
# 우럭, 모기, 바람, 사람, 니알, 바알
# 디아, 메피, 미카, 티리, 임페, 말티
# 타락, 자랑, 신화, 파워, 나락, 띵진
# 벚꽃, 나선, 뇌절, 닌자, 탈주, 공격
# 명진, 윤명, 윤띵, 패황, 패왕, 투신
# 귀신, 검신, 뇌신, 마신, 마왕, 제왕
# 황제, 대왕, 븜미, 븝미, 스타, 화신
```  
> 생각나는 두글자 단어들과 영단어의 리스트를 만들었다.  
> 던파모아에서 '사랑'이라는 키워드로 검색을 진행하면,  
> '사랑', '사랑해', '사랑한다' 등의 '사랑'이라는 키워드가 들어가는 모험단 이름이  
> 최대 20개까지 출력된다.  
> 그리고 영단어의 경우도 아주 기초적이고 접근성이,  
> 모험단 계정을 만들 때 자주 사용할만한 영단어로 구성하였다.  
> 각 단어들은 URL 인코딩을 사용하여 변환하였다.  
> [URL 인코딩 변환 사이트](https://www.convertstring.com/ko/EncodeDecode/UrlEncode) <- click  
>  
# 대략적인 흐름  
> **세부적인 것은 글 마지막에 존재하는 링크들로 들어가면 확인 가능.**  
```python
    for num, letter in enumerate(ADV_LETTER):
        dunfaMoa(SEARCH_URL + letter, num).run()
```  
>  
> 먼저, 앞서 만들었던 리스트 내 단어들로 dunfamoa 홈페이지에서 검색을 실시합니다.  
> 모험단 검색을 통해, 모험단 내 계정 캐릭터의 이름들을 전부 가져옵니다.    
>  
```python
    do = filtering()
    do.run()
```  
>   
> 목표는 105제 고유 에픽이기 때문에, 파밍을 하지 못한, 110 레벨 이하 분들은 제외시킵니다.  
> 가져온 캐릭터의 이름들을 txt로 저장합니다.  
>   
```python
    char_list = preprocessData().run()
```  
>   
> 혹시나 겹치는 캐릭터가 있을 수 있기 때문에 한 번 걸러줍니다.  
> (preprocess는 아니지만, 작성 당시 떠오르는 이름이 없어서...)  
>   
```python
    getLog(char_list).run()
```  
>   
> 저장한 캐릭터의 이름들의 로그를 NEOPLE Open API 서버에 요청합니다.  
>   
```python
    extract_func = extractEpic()
    epic = extract_func.run()
```  
>   
> 반환받은 로그들 중 에픽 획득 로그와 에픽 획득처 로그만을 가져옵니다.  
> 또한 다루기 쉽도록 내가 원하는 형태의 데이터로 가공합니다.  
>    
```python
    custom = customEpic(epic).run()
    unique = uniqueEpic(epic).run()
```  
>   
> 커스텀 에픽과 고유 에픽의 로그를 확인하는 작업입니다.  
> 통계적인 방법을 사용하지 않아 의미없는 기록이긴 하지만,  
> 재미로 전체 에픽 획득 대비 커스텀 에픽과 고유 에픽의 획득 수를 확인해봤습니다.  
>   
# Go to directory  
  
> **1. Dunfamoa 크롤링**  
> [WARP](https://github.com/Gauguin94/DNF_crawling/tree/main/DNF_epic/crawling) <- click
>     
> **2. NEOPLE 오픈 API 호출**  
> [WARP](https://github.com/Gauguin94/DNF_crawling/tree/main/DNF_epic/getAPI) <- click  
>   
> **3. 데이터 관련 사전 작업**  
> [WARP](https://github.com/Gauguin94/DNF_crawling/tree/main/DNF_epic/data) <- click  
>   
> **4. 재미로 해본 근본없는 분석?**  
> [WARP](https://github.com/Gauguin94/DNF_crawling/tree/main/DNF_epic/analyze) <- click  
