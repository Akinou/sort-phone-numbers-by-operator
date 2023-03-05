for phone_number in phone_numbers:
    for operator, codes in operators.items():
        if phone_number[:3] in codes:
            print(f"{phone_number}: {operator}")
            break
