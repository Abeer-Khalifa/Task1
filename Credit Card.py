def luhn_algorithm(card_number):
    card_number = card_number.replace(" ", "")  # Remove spaces if present
    digits = [int(digit) for digit in card_number]
    doubled_digits = []

    for i in range(len(digits) - 2, -1, -2):
        doubled_digits.append(digits[i] * 2)
        total = sum([sum(divmod(digit, 10)) for digit in doubled_digits]) + sum(digits[-1::-2])

    return total % 10 == 0


credit_card_number =(input("Input card number: "))
is_valid = luhn_algorithm(credit_card_number)

if is_valid:
    if credit_card_number[0] == '3':
        print("American Express")
    elif credit_card_number[0] == '4':
        print("Visa")
    if credit_card_number[0] == '5':
        print("MasterCard")
else:
    print("This credit card is not valid.")
