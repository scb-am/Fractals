class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.__current_channel = 1

    def first_channel(self):
        self.__current_channel = 1
        return self.channels[0]

    def last_channel(self):
        self.__current_channel = len(self.channels)
        return self.channels[-1]

    def turn_channel(self, num):
        self.__current_channel = num
        return self.channels[num - 1]

    def next_channel(self):
        self.__current_channel = self.__current_channel + 1 if self.__current_channel<len(self.channels) else 1
        return self.channels[self.__current_channel - 1]

    def previous_channel(self):
        self.__current_channel -= 1
        return self.channels[self.__current_channel - 1]

    def current_channel(self):
        return self.channels[self.__current_channel - 1]

    def is_exist(self, channel):
        if type(channel) is int:
            return "Yes" if channel <= len(self.channels) else "No"
        return "Yes" if channel in self.channels else "No"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ['ZeeTV', 'Eurosport', 'TV1000', 'ABC News']

    controller = VoiceCommand(CHANNELS)

    print(controller.last_channel())
    print(controller.previous_channel())
    print(controller.current_channel())