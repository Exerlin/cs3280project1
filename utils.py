#!/usr/bin/env python3

'''
    luhn_verified(credit_card_number) that returns the string
    “Authentic” if the card is real or “Fake” if the specified
    credit_card_number is not genuine.
'''
def luhn_verified(credit_card_number):
    sum_of_all_numbers = 0
    
    for index in range(len(credit_card_number) - 1):
        if(index % 2 == len(credit_card_number) % 2):
            credit_card_number[index] = credit_card_number[index] * 2
        if(credit_card_number[index] > 9):
            credit_card_number[index] = credit_card_number[index] - 9
        sum_of_all_numbers += credit_card_number[index]

    if(((sum_of_all_numbers % 10) + credit_card_number[len(credit_card_number) - 1]) == 10):
        return "Authentic"
    else:
        return "Fake"

'''
    is_valid(sequence) that returns true
    if the specified string sequence is in a valid credit card number format,
    and false otherwise.
'''
def is_valid(sequence):
    try:
        sequence = int(sequence)
        return True
    except:
        print('Please enter a valid credit card number.')
        return False
    
