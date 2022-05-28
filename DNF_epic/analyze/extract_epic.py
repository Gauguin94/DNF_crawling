import os

CHANNEL_NAME = ['벨마이어 공국 북부', '벨마이어 공국 남부', '흑요정 왕국', '미러 아라드', '황도', '수쥬', '이튼 공업지대', '센트럴파크', '할렘', '데 로스 제국',\
                '비공정', '바하이트', '노블레스 코드']

DUNGEON_NAME = ['성역의 바깥', '베리콜리스', '백색의 땅', '속죄의 다리', '왜곡된 차원의 폭풍',\
                '로케런 힐즈', '치안 유지국', '퀸 팔트', '화이트 플루어', '할트산 결전', '젤레 협곡', '캐니언 힐',\
                '과거의 죽은 자의 성', '베키의 공간', '왕의 요람', '헤블론의 예언소', '어둠의 공방', '빛의 쉼터', '파괴된 죽은 자의 성',\
                '옛 겐트 외곽', '라이스툰', '레츠테 호픈', '레츠테 호픈 지하수로', '이터널 플레임 연구소', '나사우 삼림', '펠슈테크']

class extractEpic:
    def __init__(self):
        pass

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
        #epiclist = self.deldupl(epiclist)
        return epiclist

    def deldupl(self, list):
        update_list = []
        for i, name in enumerate(list):
            print("{}/{}".format(i, len(list)))
            if name not in update_list:
                update_list.append(name)
        return update_list

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

    def run(self):
        epic_list = self.logLoad()
        epiclog = self.combWord(epic_list)
        return epiclog