from django.core.exceptions import ValidationError


def phone_number_validator_for_length(value):
    if len(value) != 10:
        raise ValidationError('The phone number should contain exactly 10 digits')


def is_digits_phone_validator(value):
    try:
        [int(d) for d in value]
    except ValueError:
        raise ValidationError('The phone number must contain only digits')


def first_letter_is_capital_validator(value):
    if value[0].capitalize() != value[0]:
        raise ValidationError('Your first name/last name must start with CAPITAL letter')
