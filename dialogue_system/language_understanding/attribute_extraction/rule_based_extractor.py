# -*- coding: utf-8 -*-
import re


from dialogue_system.knowledge.reader import read_gender, read_age #, read_relationship
from dialogue_system.language_understanding.utils.utils import kansuji2arabic


class RuleBasedAttributeExtractor(object):

    def __init__(self):
        self.__ages = read_age()
        self.__genders = read_gender()
        #self.__relationships = read_relationship()

    #def extract(self, text):
        #attribute = {'AGE': self.__extract_age(text), 'GENDER': self.__extract_gender(text),
                     #'MAXIMUM_AMOUNT': self.__extract_budget(text), 'RELATIONSHIP': self.__extract_relationship(text)}

        #return attribute

    def extract(self, text):
        attribute = {'AGE': self.__extract_age(text), 'GENDER': self.__extract_gender(text),
                     'MAXIMUM_AMOUNT': self.__extract_budget(text)}

        return attribute

   #def __extract_age(self, text):
        #ages = [age for age in self.__ages if age in text]
        #ages.sort(key=len, reverse=True)
        #age = ages[0] if len(ages) > 0 else ''

        #return age

#上のageは数字でやった場合

    def __extract_age(self, text):
        for age, age_values in self.__ages.items():
            for age_value in age_values:
                if age_value in text:
                    return age
        return ''

    def __extract_gender(self, text):
        for gender, gender_values in self.__genders.items():
            for gender_value in gender_values:
                if gender_value in text:
                    return gender
        return ''

    def __extract_budget(self, text):
        pattern = r'\d+円|[一二三四五六七八九十壱弐参拾百千万萬億兆〇]+円'
        match_obj = re.findall(pattern, text)
        budget_str = match_obj[0][:-1] if len(match_obj) > 0 else ''
        budget_int = kansuji2arabic(budget_str)

        return budget_int

    #def __extract_relationship(self, text):
        #relationships = [rel for rel in self.__relationships if rel in text]
        #relationships.sort(key=len, reverse=True)
        #relationship = realtionships[0] if len(relationships) > 0 else ''

        #return relationship