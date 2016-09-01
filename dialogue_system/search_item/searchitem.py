# -*- coding: utf-8 -*-
import json
import csv
import os
from watson_developer_cloud import NaturalLanguageClassifierV1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class SearchItem(object):

    def __init__(self):
        
        self.__init_data = {'GENDER':'', 'AGE':'', 'MAXIMUM_AMOUNT':''}
        self.__all_item_data = self.open_file()
        self.__watson_category_list = []
        self.__item_candidate = [[] for i in range(6)]


    def set_init(self, init_data):
        if not init_data['GENDER']:
            self.__init_data['GENDER'] = '女の子'
        else:
            self.__init_data['GENDER'] = init_data['GENDER']
        if not init_data['AGE']:
            self.__init_data['AGE'] = '10'
        else:
            self.__init_data['AGE'] = init_data['AGE']
        if not init_data['MAXIMUM_AMOUNT']:
            self.__init_data['MAXIMUM_AMOUNT'] = '3000'
        else:
            self.__init_data['MAXIMUM_AMOUNT'] = init_data['MAXIMUM_AMOUNT']



    def open_file(self):
        file_path = os.path.join(BASE_DIR, 'data.json')
#        file_path= 'data.json'
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return data


    def watson_classify(self, text):

        if self.__init_data['GENDER'] == '男の子':
            self.watson_boy(text)

        if self.__init_data['GENDER'] == '女の子':
            self.watson_girl(text)


    def watson_girl(self, text):
        USERNAME = ''
        PASSWORD = ''
        CLASSIFIER_ID = ''

        natural_language_classifier = NaturalLanguageClassifierV1(
            username=USERNAME, 
            password=PASSWORD)
        classes = natural_language_classifier.classify(CLASSIFIER_ID, text)

        for i_class in classes['classes']:
            self.__watson_category_list.append(i_class['class_name'])


    def watson_boy(self, text):
        USERNAME = ''
        PASSWORD = ''
        CLASSIFIER_ID = ''

        natural_language_classifier = NaturalLanguageClassifierV1(
            username=USERNAME, 
            password=PASSWORD)
        classes = natural_language_classifier.classify(CLASSIFIER_ID, text)

        for i_class in classes['classes']:
            self.__watson_category_list.append(i_class['class_name'])


    def search_item(self):

        tmp_item_list = self.apply_badget(self.__all_item_data, int(self.__init_data['MAXIMUM_AMOUNT']))

        for cnt, category in enumerate(self.__watson_category_list):
            self.__item_candidate[cnt] = self.select_category(tmp_item_list, category)

    def apply_badget(self, item_list, badget):
        """
        item_listから予算+a以下の金額の商品を選んで返す
        args:
            data: list, 商品のリスト
            badget: int, 予算
        return:
            new_item_list:, list, 商品のリスト
        """
        badget = badget * 1.1
        new_item_list = []

        for item in item_list:
            try:
                if int(item['Price']) < badget:
                    new_item_list.append(item)
            except IndexError:
                print('IndexError')
                pass

        return new_item_list


    def select_category(self, item_list, category):
        """
        args:
            data: list, 商品のリスト
            category: str, カテゴリー名
        return:
            new_item_list:, list, 商品のリスト
        """
        new_item_list = []

        for item in item_list:
            try:
                if item['Add_Categories'] == category:
                    new_item_list.append(item)
            except IndexError:
                print('IndexError')
                pass

        return new_item_list


    def key_word_selct(self, word_list):
        """
        全商品の説明文中の単語頻度情報のcsvファイルを参照し、
        与えられた単語リストからもっとも頻度の低いものを返す
        """

        file_path = os.path.join(BASE_DIR, 'bow.csv')
#        file_path = 'bow.csv'
        f = open(file_path, 'r', encoding='utf-8')
        csv_data = csv.reader(f)
        bow_list_data = [v for v in csv_data]

        most_word = 'かわいい'
        min_freq = 1000

        for word in word_list:
            for word_bow in bow_list_data:
                if word == word_bow[0]:
                    if int(word_bow[1]) < 1000:
                        min_freq = int(word_bow[1])
                        most_word = word
        # TODO ヒットしなかったときに何を返すか考える
        return most_word


    def search_description(self, word_list):
        """
        重要単語と商品説明が部分一致した商品を候補の一番上に並び替える
        """
        key_word = self.key_word_selct(word_list)

        for category_item in self.__item_candidate:
            for cnt, item in enumerate(category_item):
                if key_word in item['Description']:
                    tmp = item
                    del category_item[cnt]
                    category_item.insert(0, tmp)


    def get_item(self, category_num=0, item_num=0):
        """
        引数のカテゴリと商品のインデックスで指定された、商品オブジェクトを返す
        arg:
            category_num: int, カテゴリの番号
            item_num: int, 商品の番号
        return:
            商品オブジェクト
        """
        try:
            return self.__item_candidate[category_num][item_num]
        except IndexError:
            print('該当する商品がありません')
            return self.__item_candidate[0][0]

if __name__ == '__main__':
    init_data = {'GENDER':'女の子', 'AGE':'10', 'MAXIMUM_AMOUNT':''}
    text = 'お誕生日パーティをします'
    word_list = ['地図']

    ins = SearchItem()
    ins.set_init(init_data)
    ins.watson_classify(text)
    ins.search_item()
    item = ins.get_item()
    item2 = ins.get_item(0, 1)
    print('item1:   Name: {}, Price: {}円'.format(item['Name'], item['Price']))
    print('item2:   Name: {}, Price: {}円'.format(item2['Name'], item2['Price']))
    ins.search_description(word_list)
    item = ins.get_item()
    item2 = ins.get_item(0, 1)
    print('item1:   Name: {}, Price: {}円'.format(item['Name'], item['Price']))
    print('item2:   Name: {}, Price: {}円'.format(item2['Name'], item2['Price']))

