# -*- coding: utf-8 -*-
from dialogue_system.dialogue_management.manager import DialogueManager

from dialogue_system.language_understanding.language_understanding import RuleBasedLanguageUnderstanding


class Bot(object):

    def __init__(self):

        self.language_understanding = RuleBasedLanguageUnderstanding()
        self.manager = DialogueManager()

    def reply(self, sent):
        dialogue_act = self.language_understanding.execute(sent)

        self.manager.update_dialogue_state(dialogue_act)
        sys_act_type = self.manager.select_action(dialogue_act)
        print(dialogue_act)
        

        return sent