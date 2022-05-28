import os

ITEMNAME_0 = '숲속의'
ITEMNAME_1 = '블루 베릴'
ITEMNAME_2 = '엔트 정령의'

class customEpic:
    def __init__(self, epic):
        self.epic = epic

    def forest(self):
        count = 0
        forest_custom = []
        for epic in self.epic:
            if ITEMNAME_0 in epic['itemName']:
                count += 1
                forest_custom.append(epic)
        print("숲속 커스텀 에픽이 나온 경우 {}/{}".format(count, len(self.epic)))
        return forest_custom

    def beryl(self):
        count = 0
        beryl_custom = []
        for epic in self.epic:
            if ITEMNAME_1 in epic['itemName']:
                count += 1
                beryl_custom.append(epic)
        print("블루 베릴 커스텀 에픽이 나온 경우 {}/{}".format(count, len(self.epic)))
        return beryl_custom

    def spirit(self):
        count = 0
        spirit_custom = []
        for epic in self.epic:
            if ITEMNAME_2 in epic['itemName']:
                count += 1
                spirit_custom.append(epic)
        print("엔트 정령 커스텀 에픽이 나온 경우 {}/{}".format(count, len(self.epic)))
        return spirit_custom

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
            print("{} 커스텀은 {} 채널 내 드랍 에픽 {}개 중에서 {}개 출현, 재미로 보는 근본 없는 확률: {}%"\
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
            print("{} 커스텀은 {} 던전 내 드랍 에픽 {}개 중에서 {}개 출현, 재미로 보는 근본 없는 확률: {}%"\
                .format(epic_name, dungeon, dungeon_count[dungeon], count_list[dungeon], percentage))
        return 0

    def run(self):
        print('\n')
        channel_count = self.numChannel()
        dungeon_count = self.numDungeon()

        forest_epic = self.forest()
        beryl_epic = self.beryl()
        spirit_epic = self.spirit()
        print('\n')

        self.byChannel(channel_count, forest_epic, ITEMNAME_0)
        self.byChannel(channel_count, beryl_epic, ITEMNAME_1)
        self.byChannel(channel_count, spirit_epic, ITEMNAME_2)
        print('\n')

        #self.byDungeon(dungeon_count, forest_epic, ITEMNAME_0)
        self.byDungeon(dungeon_count, beryl_epic, ITEMNAME_1)
        self.byDungeon(dungeon_count, spirit_epic, ITEMNAME_2)
        
        return 0