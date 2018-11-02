# 10.31.18
import math

BASE_DIGITS = '0123456789ABCDEF'
def basetodec(base, num):
    global BASE_DIGITS
    """
    Converts a number from a base that is less than 10 to a decimal base.
    Loops through each digit of the number and mutiplies it by the digit
    place and its corresponding "base power".

    :param: base -> int, the base of the number that is being converted.
    :param: num -> int, the number that is being converted to decimal.
    :return: dec_numer -> int, the final number
    """
    num = str(num)
    dec_number = 0
    for index, digit in enumerate(num[::-1]):  # backwards looping
        dec_number +=  BASE_DIGITS.index(digit) * (base ** index)  # add it to counter
    return dec_number


def dectobase(base, num):
    global BASE_DIGITS
    """
    Converts a decimal number to a number in a base representation of
    your choice.. It does this by finding
    out the number of digits the base number would have and then
    looping through each one of these digits to form the final
    number.

    :param: num -> int the decimal number that is being converted into
    binary.
    :return: finalnum -> str, a representation of the decimal
    number given.
    """
    finalnum = ''
    numofdigits = int(math.log(num) / math.log(base))
    for digit in range(numofdigits, -1, -1):
        if num - base ** digit >= 0:
            qty = int(num / base ** digit)
            finalnum += BASE_DIGITS[qty]
            num -= qty * base ** digit
        else:
            finalnum += '0'
    return finalnum


