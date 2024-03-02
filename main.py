list_of_odd_digits = []
list_of_even_digits = []
total = 0

def format_number(number):
    """
    Formats the credit card number
    :param number: is a string of the credit card number
    :return: the formatted credit card number
    """
    if '-' or ' ' in number:
        number = number.replace('-', '')
        number = number.replace(' ', '')

    return number


card_number = ''

while len(card_number) != 16 or not card_number.isdigit():
    card_number = input("Enter a credit card number: ")

    card_number = format_number(card_number)

    if len(card_number) != 16 or not card_number.isdigit():
        print("Card Number has to be 16 digits and must not contain a non-digit")

# Reverse card number
card_number = card_number[::-1]
# Store the even-position-digits in card number
for x in card_number[1::2]:
    list_of_even_digits.append(x)
# Double each even-position digit
list_of_even_digit_doubled = [int(x)*2 for x in list_of_even_digits]

# If number in even-position is two-digit, add the digits
new_list_of_even_digit_doubled = []
for x in list_of_even_digit_doubled:
    if x >= 10:
        li = list(str(x))
        sum1 = 0
        for i in li:
            sum1 += int(i)
        new_list_of_even_digit_doubled.append(sum1)
    else:
        new_list_of_even_digit_doubled.append(x)

# Sum of even-positioned-digits
sum_of_even_positioned = 0
for i in new_list_of_even_digit_doubled:
    sum_of_even_positioned += i

# Sum of odd-positioned-digits
list_of_odd_digits = [x for x in card_number[::2]]
sum_of_odd_positioned = sum([int(x) for x in list_of_odd_digits])

total = sum_of_even_positioned + sum_of_odd_positioned


def main(t):
    if t % 10 == 0:
        return {
            'valid': True,
            'numbers': card_number[::-1]
        }
    else:
        return {
            'valid': False,
            'numbers': card_number[::-1]
        }


if __name__ == "__main__":
    if main(total)['valid']:
        print(f"{main(total)['numbers']} is a valid Credit Card Number!")
    else:
        print(f"{main(total)['numbers']} is an invalid Credit Card Number!")


