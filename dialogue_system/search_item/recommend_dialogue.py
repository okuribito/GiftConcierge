# -*- coding: utf-8 -*-
from dialogue_system.search_item.searchitem import SearchItem
from dialogue_system.morpheme import morpheme


class RecommendItem():

    def __init__(self):
        self.__search_item = SearchItem()
        self.__recommend_state = ['cnt':0, 'category':0, 'state':'WAITING_QUERY']


    def recommend(self, init_data, text):

        if len(text) < 2:
            print(text)
            return 'よく聞き取れませんでした。もう一度お願いします。'

        else:
            self.__search_item.set_init(init_data)
            self.__search_item.watson_classify(text)
            self.__search_item.search_item()
            wakati_sent = morpheme(sent)
            self.__search_item.search_description(wakati_sent)
            item = self.__search_item.get_item()

            sent = 'あなたにおすすめの商品は' + item['Name'] + 'です。'
            sent += 'どうでしょうか？気に入ったら「はい」と、違う商品が良いときは「いいえ」と言ってください。'

            self.__recommend_state['cnt'] += 1
            self.__recommend_state['category'] += 1
            self.__recommend_state['state'] = 'WAITING_ANSWER'

            return sent

        # elif self.__recommend_state['cnt'] > 0:
        #     if self.__recommend_state['category'] > 0:
        #         item = self.__search_item.get_item(self.__recommend_state['category'], 0)

        #         sent = 'うーん、それではこの商品ならどうですか？' + item['Name'] + 'です。'
        #         sent += 'どうでしょうか？気に入ったら「はい」と、違う商品が良いときは「いいえ」と言ってください。'

        #         self.__recommend_state['cnt'] += 1
        #         self.__recommend_state['category'] = 0
        #         self.__recommend_state['state'] = 'WAITING_ANSWER'

        #         return sent

        #     elif self.__recommend_state['category'] == 0:
        #         sent == 'その子の好きなものを教えて！'
        #         self.__recommend_state['state'] == 'WAITING_QUERY'

        def recommend_next(self):
            if self.__recommend_state['category'] > 0:
                item = self.__search_item.get_item(self.__recommend_state['category'], 0)

                sent = 'それではこの商品ならどうですか？' + item['Name'] + 'です。'
                sent += 'どうでしょうか？気に入ったら「はい」と、違う商品が良いときは「いいえ」と言ってください。'

                self.__recommend_state['cnt'] += 1
                self.__recommend_state['category'] += 1
                if self.__recommend_state['category'] == 3: # ここで何番目カテゴリまでをお勧めするかきめられる. 
                    self.__recommend_state['category'] = 0:
                self.__recommend_state['state'] = 'WAITING_ANSWER'

                return sent

            elif self.__recommend_state['category'] == 0:
                sent == 'うーん、もっと情報がほしいなあ。その子の好きなものを教えてください。'
                self.__recommend_state['state'] = 'WAITING_QUERY'

                return sent

        def answer_type(self, text):
            if 'はい' in text:
                sent == '気に入ってくれてうれしい。きっとすてきなプレゼントになりますよ。'
                self.__recommend_state['state'] = 'END'
            elif 'いいえ' in text:
                if self.__recommend_state['cnt'] => 10:
                    return 'お手上げ！わかりません。'
                    self.__recommend_state['state'] = 'END'
                else:
                    return self.recommend_next()


    def get_state(self):
        return self.__recommend_state
