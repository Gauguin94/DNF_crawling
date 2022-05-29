# getlog.py  
```python
class getLog:
    def __init__(self, list):
        self.charlist = list
```  
>   
> getLog 클래스는 getInfo, logSearch, saveLog, run 메소드로 구성되어 있다.  
> getLog는 캐릭터별 에픽과 관련된 모든 로그를 가져온다.  
>   
```python
    def getInfo(self):
        info_dict = []
        for character in self.charlist:
            info = character.split(" ")
            info_dict.append({'serverId':info[0], 'characterId':info[1], 'characterName':info[2]})
        return info_dict
```  
>   
> 이전에 불러온 캐릭터 정보를 딕셔너리 형태로 저장한다. {서버 이름, 캐릭터 고유 ID, 캐릭터 이름}  
>   
```python
    def logSearch(self, char_info):
        temp = []
        error_char = []
        for num, char in enumerate(char_info):
            error_count = 0
            normal = 0
            start = datetime(2022, 3, 17, 6, 0)
            deadline = datetime.now()
            day = (deadline-start).days + 1
            for i in range(1, day):
                if i == 1:
                    origin = start
                start_time = transform(start)
                end = origin + timedelta(days = i)
                end_time = transform(end)
                try:
                    http = urllib3.PoolManager()
                    url = 'https://api.neople.co.kr/df/servers/{}/characters/{}/timeline?limit={}&code={}&startDate={}&endDate={}&apikey={}'\
                        .format(char['serverId'], char['characterId'], LIMIT, GETEPIC, start_time, end_time, APIKEY)
                    req = http.request('GET', url)
                    info = loads(req.data.decode('utf-8'))
                    start = end
                    for log in info['timeline']['rows']:
                        temp.append({
                            'serverId':char['serverId'], 'adventureName':info['adventureName'], 'characterName':char['characterName'],\
                            'itemName':log['data']['itemName'], 'dungeonName':log['data']['dungeonName'],'channelName':log['data']['channelName'],\
                            'channelNo':log['data']['channelNo'], 'date':log['date']
                            })
                    normal += 1
                except:
                    error_count += 1
                    error_char.append({'serverId':char['serverId'], 'characterName':char['characterName']})
                    if error_count == 1:
                        print('{}/23651 API server down or Freak character: {}(in logSearch step)'.format(num + 1, char['serverId']+" "+char['characterName']))
            if normal:
                print(str(num+1)+"/23651", char['serverId'], char['characterName'])
        return temp, error_char
```  
>   
> 105 레벨 아이템을 얻을 수 있는 시즌은 2022년 3월 17일에 오픈되었기 때문에  
> 3월 17일부터의 에픽 관련 로그만을 가져오도록 한다.  
> NEOPLE Open API 서버에 요청을 보내 응답을 받는 것인데,  
> 응답받는 과정에서 오류가 있는 캐릭터는 예외 처리를 하여 따로 기록을 저장하도록 한다.  
>   
```python
    def saveLog(self, log_list, error_list):
        filename = whatTime()
        f = open('/home/kkn/DNF_epic/output/{}_log.txt'.format(filename),'w')
        for line in log_list:
            f.write(line['serverId']+" "+line['adventureName']+" "+line['characterName']+" "+line['itemName']+" "+line['dungeonName']+" "\
                +line['channelName']+" "+str(line['channelNo'])+" "+line['date']+'\n')
        f.close()
        f = open('/home/kkn/DNF_epic/output/character_list/error_log.txt','w')
        try:
            for line in error_list:
                f.write(line['serverId']+" "+line['characterName'])
            f.close()
        except:
            f.close()
        print('Finish!')
        return 0
```  
>   
> 앞서 응답받은 캐릭터별 에픽 관련 로그와 오류가 난 캐릭터들을 저장하는 작업을 수행한다.  
>   
