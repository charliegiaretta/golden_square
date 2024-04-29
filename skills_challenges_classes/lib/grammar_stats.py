class GrammarStats:
    def __init__(self):
        self.texts = 0
        self.passed_texts = 0

    def check(self, text):
        if text[0].isupper() and text[-1] == '.':
            self.texts += 1
            self.passed_texts += 1
            return True
        else:
            self.texts += 1
            return False

    def percentage_good(self):
        percent = (self.passed_texts / self.texts) * 100
        return round(percent)