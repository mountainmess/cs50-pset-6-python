import cs50

# prompt for CC number
while True:
    user_input = cs50.get_string("Number: ")
    if user_input > 0:
        break
sum1 = 0
sum2 = 0
total = 0
digit1 = 0
digit2 = 0
dcount = 0
check1 = user_input
check2 = user_input
count = user_input

# /*checksum validation Multiply every other digit by 2, starting with the number’s
# second-to-last digit, and then add those products’ digits together.*/


while check1 != 0:
    check1 = int(check1 / 10)
    digit1 = int(check1 % 10)
    digit1 = int(digit1 * 2)
    if digit1 > 9:
        sum1 += int(digit1 % 10)
        sum1 += int(digit1 / 10)
    else:
        sum1 += int(digit1)
    check1 = int(check1 / 10)

# /*the sum of the digits that weren’t multiplied by 2.*/


while check2 != 0:
    digit2 = int(check2 % 10)
    sum2 += int(digit2)
    check2 = int(check2 / 100)

# /*add the two numbers above together*/
total = int(sum1 + sum2)

# /*count digits*/
while count != 0:
    count = int(count / 10)
    dcount += 1

# /*check total ends in 0*/
if (total % 10) != 0:
    print("INVALID")

# /*check number is a valid length*/
# /* check if 13 digit visa*/
elif dcount == 13:
    user_input = int(user_input / 1000000000000)
    if user_input == 4:
        print("VISA")
    else:
        print("INVALID")

# /* check if 16 digit visa or mastercard*/
elif dcount == 16:
    user_input = int(user_input / 100000000000000)
    print("user_input: ", user_input)
    if user_input > 50 and user_input < 56:
        print("MASTERCARD")
    elif (int(user_input / 10)) == 4:
        print("VISA")
    else:
        print("INVALID")

    # check if AMEX*/
elif dcount == 15:
    user_input = int(user_input / 10000000000000)
    if user_input == 34 or user_input == 37:
        print("AMEX")
    else:
        print("INVALID")

else:
    print("INVALID")

