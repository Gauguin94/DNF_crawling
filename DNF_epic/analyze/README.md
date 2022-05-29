# extract_epic.py  
```python
CHANNEL_NAME = ['벨마이어 공국 북부', '벨마이어 공국 남부', '흑요정 왕국', '미러 아라드', '황도', '수쥬', '이튼 공업지대', '센트럴파크', '할렘', '데 로스 제국',\
                '비공정', '바하이트', '노블레스 코드']

DUNGEON_NAME = ['성역의 바깥', '베리콜리스', '백색의 땅', '속죄의 다리', '왜곡된 차원의 폭풍',\
                '로케런 힐즈', '치안 유지국', '퀸 팔트', '화이트 플루어', '할트산 결전', '젤레 협곡', '캐니언 힐',\
                '과거의 죽은 자의 성', '베키의 공간', '왕의 요람', '헤블론의 예언소', '어둠의 공방', '빛의 쉼터', '파괴된 죽은 자의 성',\
                '옛 겐트 외곽', '라이스툰', '레츠테 호픈', '레츠테 호픈 지하수로', '이터널 플레임 연구소', '나사우 삼림', '펠슈테크']
```
>   
> 원하는 형태의 데이터로 가공할 때 필요한 채널 이름과 던전 이름을 리스트로 만들었다.  
>   
```python
class extractEpic:
    def __init__(self):
        pass
```  
>   
> extractEpic 클래스는 logLoad, combWord, run 메소드로 구성되어 있다.   
> 앞서 획득한 로그들을 원하는 형태의 데이터로 가공한다.  
>   
```python
    def logLoad(self):
        filelist = []
        epiclist = []
        path = '/home/kkn/DNF_epic/output/'
        filelist_ = os.listdir(path)
        for file in filelist_:
            if 'txt' in file:
                filelist.append(file)
        for txt in filelist:
            f = open(path + txt, 'r', encoding = 'UTF8')
            try:
                for line in f:
                    log = line.replace("\n", "")
                    epiclist.append(log)
                f.close()
            except:
                f.close()
                f = open(path + txt, 'r', encoding = 'cp949')
                for line in f:
                    log = line.replace("\n", "")
                    epiclist.append(log)
                f.close()
        return epiclist
```
>   
> txt 파일에 저장한 로그들을 불러들인다.  
>   
```python
    def combWord(self, epiclist):
        standard = []
        for line in epiclist:
            wasted_count = 0
            div = line.split(" ")
            server = div[0]
            adv = div[1]
            char = div[2]
            date = div[-2]+" "+div[-1]
            channelNo = div[-3]
            for name in DUNGEON_NAME:
                if name in line:
                    dungeon = name
            for name in CHANNEL_NAME:
                if name in line:
                    channel = name
                else:
                    wasted_count += 1
            if wasted_count >= len(CHANNEL_NAME):
                continue
            else:
                item = line.replace(div[0], "")
                item = item.replace(div[1], "")
                item = item.replace(div[2], "")
                item = item.replace(date, "")
                item = item.replace(channelNo, "")
                item = item.replace(channel, "")
                item = item.replace(dungeon, "").strip()

                standard.append({'itemName':item, 'dungeonName':dungeon, 'channelName':channel})
        
        return standard
```
>   
> {아이템 이름, 아이템이 출현한 던전 이름, 아이템이 출현한 채널 이름} 형태의 딕셔너리 타입으로 저장한다.  

# unique_epic.py  

```python
ITEMNAME = [
    '임펄스 트리거', '여명의 성배', '전술 드론 콘트롤러 암릿', '지상형 : 전술 차륜 드론', '하늘을 수호하는 윙 부츠', '부스팅 펄스 튜브', '파워 플랜트', '골드 윙 반지',\
    '언리밋 사이버네틱', '고귀한 신의', '매니퓰레이션', '황혼의 성단', '미지의 황금비석', '공중형 : 전술 프롭 드론', '전술 레이더망 링', '잔잔한 선율', '이온화조정 팔찌',\
    '대지를 딛는 부츠', '별을 담는 벨트', '주체할 수 없는 낡은 규칙', '하이테크 전술보조 각반', '천상을 수호하는 윙 아머', '폭풍을 삼킨 에너지', '선회하는 흐려진 혜안',\
    '고양된 분노의 목걸이', '터치 컨트롤 패널', '자기장 탐지링', '억제된 마력의 팔찌', '하이테크 전술지휘 아머', '천재 기술자의 두터운 보호부츠', '천재 기술자의 멀티툴 벨트',\
    '천재 기술자의 보호 마스크', '스톰라이더', '홀로그램 콜', '하늘에 휘날리는 깃털', '어댑터블 투톤 링', '자정의 성역', '수확하는 옥수', '디젯 퓨즈 초크', '데저트 테크놀로지 팬츠',\
    '마땅한 본분', '죽음에 잠식된 갑주', '화려한 청색의 음율', '소망을 전하는 편지', '작은 풀잎의 순수함', '정의의 기사 가면', '피어오르는 광기', '아크로매틱 룸버스',\
    '원터치 스마트 리모콘', '어비스 리액터', '블랙 캣 헬멧', '얼터레이션 다이얼 벨트', '평화를 수호하는 윙 레깅스', '하이테크 고기동 강화 부츠', '고통의 상처',\
    '용살자의 증표 - 용린 귀걸이', '기품의 금빛 장신구', '화음하는 음색', '죽음을 부르는 관', '저주받은 마음', '리버시블 레더 코트', '음율에 담은 소망', '절망의 발소리',\
    '천재 기술자의 멀티박스 팬츠', '하이테크 바디 프로텍트 숄더'
]
```  
>   
> 105제 고유 에픽을 모아 리스트로 저장하였다.  
>   
```python
```
```python
```
```python
```
```python
```
```python
```
```python
```
