# -*- coding: utf-8 -*-

import requests

from source.generator_model import generate_mail, generate_password, generate_date



mail = generate_mail()
password = generate_password(12)
date = generate_date()
print (mail, password, date)

# r = requests.get('https://konto.gazeta.pl/konto/rejestracja,.html?', headers=headers, cookies=cookies)