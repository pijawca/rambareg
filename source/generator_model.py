# -*- coding: utf-8 -*-

import string
from russian_names import RussianNames
from random import choice, randint


def generate_mail():
    get_name = RussianNames(count=1, transliterate=True, output_type='dict').get_batch()
    get_name = get_name[0]
    mail = f'{get_name["surname"]}.{get_name["name"]}'.lower()
    
    return mail

def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(choice(characters) for _ in range(length))
    
    return password

def generate_date():
    day = randint(1, 31)
    month = randint(1, 12)
    year = randint(1950, 2004)
    
    return [day, month, year]
