import os
import sys
from json import loads
from urllib import parse
import urllib3
APIKEY = 'm4IfyspAlBF1y2aAumdC1Nj39oQHNX7v'
FWLV = 100

def deldupl(list):
    update_list = []
    for i, name in enumerate(list):
        if name not in update_list:
            update_list.append(name)
    return update_list

def urlDecoding(charlist):
    decoded_list = []
    for charname in charlist:
        decoded_list.append(parse.quote(charname))
    return decoded_list

if __name__ == "__main__":
    temp = []
    f = open("extract_character.txt", 'r')
    for line in f:
        temp.append(line.split(" ")[1][:-1])
    f.close()
    print(len(temp))
    decoded_list = urlDecoding(temp)
    print(len(decoded_list))

    char_list = []
    error_count = 0
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
    print(len(char_list))
    char_list = deldupl(char_list)
    print(len(char_list))
    f = open("season_player.txt",'w')
    for line in char_list:
        f.write(line['serverId']+" "+line['characterId']+" "+line['characterName']+'\n')
    f.close()
    print('Success! and Error count: {}'.format(error_count))