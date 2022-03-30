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




# class Text:
#     text = font = ''
#
#     def write(self, text):
#         self.text += text
#
#     def restore(self, old):
#         self.text, self.font = old
#
#     def set_font(self, font):
#         self.font = f'[{font}]'
#
#     def show(self):
#         return f'{self.font}{self.text}{self.font}'
#
#
# class SavedText(list):
#     get_version = list.__getitem__
#
#     def save_text(self, text):
#         self.append((text.text, text.font))




# class Text:
#     def __init__(self): self.restore(dict(contents='', font=None))
#     def restore(self, version): vars(self).update(version)
#     def write(self, text): self.contents += text
#     def set_font(self, font): self.font = font
#     def show(self):
#         fontrep = '' if self.font is None else self.font.join('[]')
#         return fontrep + self.contents + fontrep
#
# class SavedText(list):
#     def save_text(self, text): self.append(vars(text).copy())
#     get_version = list.__getitem__




# from copy import copy
#
#
# class Text:
#
#     def __init__(self):
#         self.font = None
#         self.text = []
#
#     def write(self, text):
#         self.text.append(text)
#
#     def set_font(self, font):
#         self.font = font
#
#     def show(self):
#         text = ''.join(self.text)
#         if self.font is not None:
#             return '[{0}]{1}[{0}]'.format(self.font, text)
#         return text
#
#     def restore(self, version):
#         self.text = version[0]
#         self.font = version[1]
#
#
# class SavedText:
#
#     def __init__(self):
#         self.versions = []
#
#     def save_text(self, text):
#         version = (copy(text.text), text.font)
#         self.versions.append(version)
#
#     def get_version(self, number):
#         return self.versions[number]


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
