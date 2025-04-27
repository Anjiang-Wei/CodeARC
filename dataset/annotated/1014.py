def check_HK_phone_number(number: str) -> tuple[bool, bool]:
    import re

    HK_PHONE_NUMBER = r'\d{4} \d{4}'

    def is_valid_HK_phone_number(number):
        # Check if the entire string is a valid HK phone number
        return bool(re.match(HK_PHONE_NUMBER + r'\Z', number))

    def has_valid_HK_phone_number(number):
        # Check if the string contains a valid HK phone number
        return bool(re.search(HK_PHONE_NUMBER, number))

    return is_valid_HK_phone_number(number), has_valid_HK_phone_number(number)

