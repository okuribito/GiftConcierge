# -*- coding: utf-8 -*-
import sys


class LanguageGenerator(object):

    def __init__(self):
        pass

    def generate_sentence(self, dialogue_act):
        sent = ''
        if 'AGE' in dialogue_act:
            sent += '年齢は{0}才ですね。'.format(dialogue_act['AGE'])
        if 'GENDER' in dialogue_act:
            sent += '{0}ですね。'.format(dialogue_act['GENDER'])
        if 'MAXIMUM_AMOUNT' in dialogue_act:
            sent += '予算は{0}円ですね。'.format(dialogue_act['MAXIMUM_AMOUNT'])

        sys_act_type = dialogue_act['sys_act_type']
        if sys_act_type == 'REQUEST_AGE':
            sent += '年齢は何歳ですか？'
        elif sys_act_type == 'REQUEST_GENDER':
            sent += '男の子ですか？女の子ですか？'
        elif sys_act_type == 'REQUEST_BUDGET':
            sent += '予算の上限はどのくらいですか？'
        #elif sys_act_type == 'CHAT':
            #sent += dialogue_act['utt']
        #elif sys_act_type == 'INFORM_RESTAURANT':
            #restaurant = dialogue_act['restaurant']
            #if restaurant:
                #name, address, access = restaurant['name'], restaurant['address'], restaurant['access']
                #lat, lng = restaurant['lat'], restaurant['lng']
                #sent += 'では、{0}がおすすめです。\n場所は{1}で{2}です。\n'.format(name, address, access)
                #url = 'https://maps.googleapis.com/maps/api/staticmap?center={0},{1}&size=640x480&zoom=14&markers={0},{1}'
                #sent += url.format(lat, lng)
            #else:
                #sent += '申し訳ありません。条件に一致するお店が見つかりませんでした。'
        else:
            print('Error')
            sys.exit(-1)

        return sent