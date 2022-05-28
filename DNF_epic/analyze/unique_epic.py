import os
import sys

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

class uniqueEpic:
    def __init__(self, epic):
        self.epic = epic
        self.count = 0

    def unique(self, name):
        count = 0
        unique_epic = []
        for epic in self.epic:
            if name in epic['itemName']:
                self.count += 1
                unique_epic.append(epic)
        return unique_epic

    def numChannel(self):
        channel_count = {}
        for data in self.epic:
            if data['channelName'] not in channel_count:
                channel_count.setdefault(data['channelName'], 1)
            else:
                channel_count[data['channelName']] += 1
        return channel_count

    def byChannel(self, channel_count, epic, epic_name):
        count_list = {}
        for data in epic:
            if data['channelName'] not in count_list:
                count_list.setdefault(data['channelName'], 1)
            else:
                count_list[data['channelName']] += 1

        for channel in count_list:
            percentage = (count_list[channel]/channel_count[channel])*100
            print("{} 은(는) {} 채널 내 드랍 에픽 {}개 중에서 {}개 출현, 재미로 보는 근본 없는 확률: {}%"\
                .format(epic_name, channel, channel_count[channel], count_list[channel], percentage))
        return 0

    def numDungeon(self):
        dungeon_count = {}
        for data in self.epic:
            if data['dungeonName'] not in dungeon_count:
                dungeon_count.setdefault(data['dungeonName'], 1)
            else:
                dungeon_count[data['dungeonName']] += 1
        return dungeon_count

    def byDungeon(self, dungeon_count, epic, epic_name):
        count_list = {}
        for data in epic:
            if data['dungeonName'] not in count_list:
                count_list.setdefault(data['dungeonName'], 1)
            else:
                count_list[data['dungeonName']] += 1

        for dungeon in count_list:
            percentage = (count_list[dungeon]/dungeon_count[dungeon])*100
            print("{} 은(는) {} 던전 내 드랍 에픽 {}개 중에서 {}개 출현, 재미로 보는 근본 없는 확률: {}%"\
                .format(epic_name, dungeon, dungeon_count[dungeon], count_list[dungeon], percentage))
        return 0

    def run(self):
        sys.stdout = open('stdout.txt', 'w')

        channel_count = self.numChannel()
        dungeon_count = self.numDungeon()
        
        for item in ITEMNAME: 
            print('\n')
            unique_epic = self.unique(item)
            self.byChannel(channel_count, unique_epic, item)
            self.byDungeon(dungeon_count, unique_epic, item)
        print("고유 에픽이 나온 경우 {}/{}".format(self.count, len(self.epic)))
        print('\n')
        
        sys.stdout.close()
        return 0