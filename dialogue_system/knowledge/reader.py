# -*- coding: utf-8 -*-
import os
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


#def read_age():
    #file_path = os.path.join(BASE_DIR, 'age.txt')
    #with open(file_path, 'rb') as f:
        #ages = [age.decode('utf-8').strip() for age in f]

    #return ages
#上のageは数字でやった場合

def read_age():
    file_path = os.path.join(BASE_DIR, 'age.yaml')
    with open(file_path, 'rb') as f:
        age = yaml.load(f)

    return age


def read_gender():
    file_path = os.path.join(BASE_DIR, 'gender.yaml')
    with open(file_path, 'rb') as f:
        gender = yaml.load(f)

    return gender

#def read_relationship():
    #file_path = os.path.join(BASE_DIR, 'relationship.yaml')
    #with open(file_path, 'rb') as f:
        #relationships = yaml.load(f)

    #return relationships