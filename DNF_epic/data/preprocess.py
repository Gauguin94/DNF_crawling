import os
from datetime import datetime

def whatTime():
    time = datetime.now()
    time = time.strftime("%y%m%d%H%M")
    date = time[:6]
    return date

class preprocessData:
    def __init__(self):
        pass

    def loadData(self):
        path = '/home/kkn/DNF_epic/data/'
        charlist = []
        filelist = []
        filelist_ = os.listdir(path)
        for file in filelist_:
            if 'txt' in file:
                filelist.append(file)
        for txt in filelist:
            f = open(path + txt, 'r', encoding = 'UTF8')
            try:
                for index, raw in enumerate(f):
                    name = raw.replace("\n", "").strip()
                    charlist.append(name)
                f.close()
            except:
                f.close()
                f = open(path + txt, 'r', encoding = 'cp949')
                for index, raw in enumerate(f):
                    name = raw.replace("\n", "").strip()
                    charlist.append(name)
                f.close()
        charlist = self.deldupl(charlist)
        return charlist

    def deldupl(self, list):
        update_list = []
        for i, name in enumerate(list):
            if name not in update_list:
                update_list.append(name)
        return update_list

    def saveData(self, charlist):
        filename = whatTime()
        f = open('/home/kkn/DNF_epic/output/character_list/name_list_{}.txt'.format(filename), 'w')
        for line in charlist:
            f.write(line+'\n')
        f.close()
        return 0

    def run(self):
        char_list = []
        char_list = self.loadData()
        self.saveData(char_list)
        return char_list