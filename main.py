import phonenumbers

# pip3 install phonenumbers

from test import number
from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "NG")
print(phonenumbers.format_number(ch_number, phonenumbers.PhoneNumberFormat.E164))
print(phonenumbers.format_number(ch_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print(phonenumbers.format_number(ch_number, phonenumbers.PhoneNumberFormat.NATIONAL))
print(phonenumbers.format_number(ch_number, phonenumbers.PhoneNumberFormat.RFC3966))
print(geocoder.description_for_number(ch_number, "en"))