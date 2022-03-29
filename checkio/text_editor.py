class Text:
    def __init__(self):
        self.text = ''
        self.font = None

    def write(self, text):
        self.text = f'{self.text}{text}'

    def set_font(self, font):
        self.font = font

    def show(self):
        return f'[{self.font}]{self.text}[{self.font}]' if self.font else self.text

    def restore(self, new_text):
        self.text = new_text.text
        self.font = new_text.font


class SavedText:
    def __init__(self):
        self.versions = []

    def get_version(self, i):
        return self.versions[i]

    def save_text(self, text: Text):
        new_text = Text()
        new_text.write(text.text)
        new_text.set_font(text.font)
        self.versions.append(new_text)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
