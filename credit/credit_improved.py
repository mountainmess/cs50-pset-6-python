# After writing the messy translation, I decided to start from scratch and learn a bit
# about  how python works, including creating lists for easy access to digits, and 
# streamling the code all round (this is 30 lines shorter than my other code)

import cs50


def main():
    # prompt for CC number
    while True:
        cc_number = cs50.get_string("Number: ")
        if cc_number.isdigit():
            break
    cc_digits = digits_list(cc_number)

    # key numbers to ID credit cards
    AMEX = [4, 7]
    MASTERCARD = [1, 2, 3, 4, 5]
    VISA = [4]

    # send number through checksum
    # VISA starts with a 4 and is 13 or 16 in length
    # MASTERCARD starts with a 5, variable 2nd digit, 16 in length
    # AMEX starts with a 3, variable second digit and 15 in length
    if luhn(cc_number, cc_digits) == True:
        if cc_digits[0] in VISA and (len(cc_digits) == 13 or len(cc_digits) == 16):
            print("VISA")
        if cc_digits[0] == 5 and cc_digits[1] in MASTERCARD and len(cc_digits) == 16:
            print("MASTERCARD")
        if cc_digits[0] == 3 and cc_digits[1] in AMEX and len(cc_digits) == 15:
            print("AMEX")
    else:
        print("INVALID")


def luhn(cc, cc_list):
    # create a list of the odds and evens
    odd_digits = cc_list[-1::-2]
    even_digits = cc_list[-2::-2]
    total = 0
    total += sum(odd_digits) # add the odd digits together
    for d in even_digits:
        total += sum(digits_list(d*2)) # double the even digits and add them to the total
    if total % 10 == 0: # if the total ends in a 0 (is a factor of 10)
        return True
    else:
        return False


def digits_list(number):
    return[int(d) for d in str(number)] # converts a string to a list of integers


main()
