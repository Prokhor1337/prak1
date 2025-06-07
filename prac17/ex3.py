from collections import Counter

class TextStats:
    def __init__(self, text):
        self.text = text.lower()

    def count_words(self):
        return len(self.text.split())

    def most_common_letter(self):
        letters = [c for c in self.text if c.isalpha()]
        if not letters:
            return None
        return Counter(letters).most_common(1)[0]
