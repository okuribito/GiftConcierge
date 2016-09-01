# -*- coding: utf-8 -*-


class DialogueState(object):

    def __init__(self):
        #self.__state = {'GENDER': None, 'AGE': None, 'MAXIMUM_AMOUNT': None, 'RELSTIONSHIP': None }
        self.__state = {'GENDER': None, 'AGE': None, 'MAXIMUM_AMOUNT': None, }

    def update(self, dialogue_act):
        self.__state['GENDER'] = dialogue_act.get('GENDER', self.__state['GENDER'])
        self.__state['AGE'] = dialogue_act.get('AGE', self.__state['AGE'])
        self.__state['MAXIMUM_AMOUNT'] = dialogue_act.get('MAXIMUM_AMOUNT', self.__state['MAXIMUM_AMOUNT'])
        #self.__state['RELATIONSIP'] = dialogue_act.get('RELATIONSHIP', self.__state['RELATIONSHIP'])

    def has(self, name):
        return self.__state.get(name, None) != None

    def get_age(self):
        return self.__state['AGE']

    def get_gender(self):
        return self.__state['GENDER']

    def get_budget(self):
        return self.__state['MAXIMUM_AMOUNT']

    #def get_relationship(self):
        #return self.__state['RELATIONSHIP']    

    def clear(self):
        self.__init__()

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)