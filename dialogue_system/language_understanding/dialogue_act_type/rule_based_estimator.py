
# -*- coding: utf-8 -*-


class RuleBasedDialogueActTypeEstimator(object):

    def __init__(self):
        pass

    def estimate(self, attribute):
        if attribute['GENDER'] != '':
            return 'INFORM_GENDER'
        elif attribute['AGE'] != '':
            return 'INFORM_AGE'
        elif attribute['MAXIMUM_AMOUNT'] != '':
            return 'INFORM_MONEY'
        #elif attribute['RELATIONSHIP'] != '':
            #return 'RELATIONSHIP'    
        else:
            return 'OTHER'