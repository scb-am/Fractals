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




# from dataclasses import dataclass, field
# from functools import singledispatchmethod, wraps
# from typing import List
# Channel = str
#
#
# def _channel(method):
#     @wraps(method)
#     def _method(self, *args, **kwargs):
#         method(self, *args, **kwargs)
#         return self.channels[self.n % len(self.channels)]
#     return _method
#
#
# def _bool2text(method):
#     @wraps(method)  # Necessary to keep annotations for singledispatchmethod.
#     def _method(self, *args, **kwargs):
#         return 'Yes' if method(self, *args, **kwargs) else 'No'
#     return _method
#
#
# @dataclass
# class VoiceCommand:
#     channels: List[Channel] = field(default_factory=list)
#     n: int = 0
#
#     @_channel
#     def first_channel(self) -> Channel:
#         self.n = 0
#
#     @_channel
#     def last_channel(self) -> Channel:
#         self.n = -1
#
#     @_channel
#     def turn_channel(self, n: int) -> Channel:
#         self.n = n - 1
#
#     @_channel
#     def next_channel(self) -> Channel:
#         self.n += 1
#
#     @_channel
#     def previous_channel(self) -> Channel:
#         self.n -= 1
#
#     @_channel
#     def current_channel(self) -> Channel:
#         pass
#
#     @singledispatchmethod
#     @_bool2text
#     def is_exist(self, *args, **kwargs):
#         return False
#
#     @is_exist.register
#     @_bool2text
#     def _(self, n: int) -> str:
#         return 0 <= n - 1 < len(self.channels)
#
#     @is_exist.register
#     @_bool2text
#     def _(self, channel: Channel) -> str:
#         return channel in self.channels


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ['ZeeTV', 'Eurosport', 'TV1000', 'ABC News']

    controller = VoiceCommand(CHANNELS)

    print(controller.last_channel())
    print(controller.previous_channel())
    print(controller.current_channel())