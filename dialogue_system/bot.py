# -*- coding: utf-8 -*-
from dialogue_system.dialogue_management.manager import DialogueManager
from dialogue_system.language_generation.generator import LanguageGenerator
from dialogue_system.language_understanding.language_understanding import RuleBasedLanguageUnderstanding
from dialogue_system.search_item.searchitem import SearchItem


class Bot(object):

    def __init__(self):
        self.generator = LanguageGenerator()
        self.language_understanding = RuleBasedLanguageUnderstanding()
        self.manager = DialogueManager()


    def reply(self, sent):

        current_state = self.manager.get_state()

        if current_state['AGE'] != None and current_state['GENDER'] != None and current_state['MAXIMUM_AMOUNT'] != None:
            init_data = {}
            init_data['AGE'] = current_state['AGE']
            init_data['GENDER'] = current_state['GENDER']
            init_data['MAXIMUM_AMOUNT'] = current_state['MAXIMUM_AMOUNT']

            ins = SearchItem()
            ins.set_init(init_data)
            ins.watson_classify(sent)
            ins.search_item()
            item = ins.get_item()

            return item['Name']

        else:

            dialogue_act = self.language_understanding.execute(sent) # 一時的なユーザー状態
            # dialogue_act = {'user_act_type': act_type, 'utt': sent, + 情報が得られたキー}

            self.manager.update_dialogue_state(dialogue_act) # dialogue_actから状態を更新
            sys_act_type = self.manager.select_action(dialogue_act) # sialogue_actに{sys_act_type:'CHAT'|'REQUEST_AGE'|'REQUEST_GENDER'|'REQUEST_BUDGET'|'REQUEST_HOBBY'}を追加したもの

            print(dialogue_act)

            sent = self.generator.generate_sentence(sys_act_type)

        return sent