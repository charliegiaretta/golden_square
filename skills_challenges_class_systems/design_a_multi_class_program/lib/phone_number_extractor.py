import re

class PhoneNumberExtractor():
    def __init__(self, diary):
        self._diary = diary

    def extract(self):
        phone_numbers = set()
        for entry in self._diary.all():
            contents = entry.contents
            found_numbers = re.findall(r"\b0[0-9]{10}\b", contents)
            phone_numbers.update(found_numbers)
        return phone_numbers
