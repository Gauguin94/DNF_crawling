import ssl
import urllib3
from json import loads
from urllib.request import urlopen
from datetime import datetime
from .consts import*
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
context = ssl._create_unverified_context()

def whatTime():
    time = datetime.now()
    time = time.strftime("%y%m%d%H%M")
    date = time[:6]
    return date

class neopleWeb:
    def __init__(self, keyword):
        self.keyword = keyword
        self.error_count = 0
        self.char_count = 0

    def loadChar(self):
        char_list = []
        http = urllib3.PoolManager()
        for word in self.keyword:
            try:
                url = 'https://api.neople.co.kr/df/servers/{}/characters?characterName={}&limit={}&wordType={}&apikey={}'\
                    .format('all', word, '200', 'full', APIKEY)
                req = http.request('GET', url)
                search_info = loads(req.data.decode('utf-8'))
                for character in search_info['rows']:
                    if character['level'] > FWLV:
                        self.char_count += 1
                        char_list.append({'serverId':character['serverId'], 'characterId':character['characterId'], 'characterName':character['characterName']})
                        print('{} {} {}'.format(self.char_count, character['serverId'], character['characterName']))
            except:
                self.error_count += 1
                print('Neople API server down or freak character. Error count: {}'.format(self.error_count))
        return char_list

    def deldupl(self, list):
        update_list = []
        for i, name in enumerate(list):
            if name not in update_list:
                update_list.append(name)
        return update_list

    def saveCharinfo(self, char_list):
        filename = whatTime()
        f = open('/home/kkn/DNF_epic/data/{}.txt'.format(filename), 'w')
        for character in char_list:
            f.write(character['serverId']+" "+character['characterId']+" "+character['characterName']+'\n')
        f.close()
        print('{} successd! and Error count: {}'.format(self.char_count, self.error_count))
        return 0

    def run(self):
        charlist = self.loadChar()
        charlist = self.deldupl(charlist)
        self.saveCharinfo(charlist)
        return 0