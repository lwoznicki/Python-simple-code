#https://www.hackerrank.com/challenges/valid_credit_card_numberating-credit-card-number/problem

import re

n = int(input())

for i in range(n):
    credit = input().strip()
    credit_removed_hiphen = credit.replace('-','')
    valid_credit_card_number = True
	
    credit_card_19_digits = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',credit))	
    credit_card_16_digits = bool(re.match(r'^[4-6]\d{15}$',credit))

    consecutive_repeated_numbers = bool(re.findall(r'(?=(\d)\1\1\1)',credit_removed_hiphen))
    if credit_card_16_digits == True or credit_card_19_digits == True:
        if consecutive_repeated_numbers == True:
            valid_credit_card_number = False
    else:
        valid_credit_card_number = False  
		
    if valid_credit_card_number == True:
        print('Valid')
    else:
        print('Invalid_credit_card_number')