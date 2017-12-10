from django.core.validators import RegexValidator

all_numbers_validator = RegexValidator('^\d+$',
                                       'Number entered was not all digits(no whitespaces), '
                                       'please try again')
min_length_validator = RegexValidator('^.{10,14}$',
                                      'Number entered was not a minimum of 10 characters, max of 14, '
                                      'please try again')
not_start_with_zero_validator = RegexValidator('^[1-9]{1}',
                                               'Number is not in international format, '
                                               'please try again')