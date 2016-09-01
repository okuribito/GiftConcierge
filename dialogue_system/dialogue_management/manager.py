# -*- coding: utf-8 -*-
from copy import deepcopy

from dialogue_system.dialogue_management.state import DialogueState

#from dialogue_system.backend.apis.docomo_dialogue import DocomoDialogAPI


class DialogueManager(object):

    def __init__(self):
        self.dialogue_state = DialogueState()

    def update_dialogue_state(self, dialogue_act):
        self.dialogue_state.update(dialogue_act)

    def select_action(self, dialogue_act):
        sys_act = deepcopy(dialogue_act)
        if dialogue_act['user_act_type'] == 'OTHER':
            #api = DocomoDialogAPI()
            #reply = api.reply(dialogue_act['utt'])
            reply ="こんにちは"
            sys_act['sys_act_type'] = 'CHAT'
            sys_act['utt'] = reply
        elif not self.dialogue_state.has('AGE'):
            sys_act['sys_act_type'] = 'REQUEST_AGE'
        elif not self.dialogue_state.has('GENDER'):
            sys_act['sys_act_type'] = 'REQUEST_GENDER'
        #elif not self.dialogue_state.has('MAXIMUM_AMOUNT'):
            #sys_act['sys_act_type'] = 'REQUEST_BUDGET'
        #elif not self.dialogue_state.has('RELATIONSHIP'):
            #sys_act['sys_act_type'] = 'REQUEST_RELATIONSHIP'  
        elif not self.dialogue_state.has('MAXIMUM_AMOUNT')
        	sys_act['sys_act_type'] = 'REQUEST_BUDGET'
        # else:
        #     api = HotPepperGourmetAPI()
        #     area = self.dialogue_state.get_area()
        #     food = self.dialogue_state.get_food()
        #     budget = self.dialogue_state.get_budget()
        #     restaurant = api.search_restaurant(area=area, food=food,budget=budget)
        #     sys_act['sys_act_type'] = 'INFORM_RESTAURANT'
        #     sys_act['restaurant'] = restaurant
        #     self.dialogue_state.clear()

        # 初期情報がそろったあと趣味を聞く状態
        else:
            sys_act['sys_act_type'] = 'REQUEST_HOBBY'
            sys_act['AGE'] = self.dialogue_state.get_age()
            sys_act['GENDER'] = self.dialogue_state.get_gender()
            sys_act['MAXIMUM_AMOUNT'] = self.dialogue_state.get_budget()
            return sys_act

        return sys_act 