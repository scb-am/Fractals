import getopt
import os
import sys
import subprocess

from colorama import Fore
from colorama import Style
from programming_types.FP_application import find_treasure
from programming_types.OOP_application import Treasure_map, Treasure_road


class Main():
    def __init__(self, text_command):
        self.text_command = text_command
        self.map_data = []
        self.map_weight = 0
        self.map_height = 0
        self.settings_dir = 'settings/settings.txt'

    def start(self):
        self.load_opts_args()

    def load_opts_args(self):
        optlist, args = getopt.getopt(self.text_command, 'hmft', [
            'manual', 'help', 'file', 'test'
        ])
        if not optlist:
            print('You need to choose a parser method. '
                  'Run the script with the "-h" option to see the options included')
        for o, a in optlist:
            if o in ("-h", "--help"):
                print('Options:\n\t-h, --help\t\tShow help.'
                      '\n\t-m, --manual\t\tRun application with manual settings.'
                      '\n\t-f, --file\t\tRun application with manual settings from file. Use relative path.'
                      '\n\t-t, --test\t\tRun tests.')
            elif o in ("-m", "--manual"):
                self.get_input_data()
            elif o in ("-f", "--file"):
                self.get_file_data()
            elif o in ("-t", "--test"):
                self.run_tests()

    def run_tests(self):
        subprocess.call(["py.test -s -v"], shell=True)

    def get_input_data(self):
        self.map_weight = self.get_data('map weight', int)
        self.map_height = self.get_data('map height', int)
        for i in range(1, self.map_height + 1):
            line = self.get_data(f'map line number {i} separate whitespaces',
                                 lambda data: None if len(data.split(' ')) < self.map_weight else
                                 [str(int(x[:2])) for x in data.split(' ')[:self.map_weight]])
            print(f'{Fore.BLUE}Map line number {i} data - {line}{Style.RESET_ALL}')
            self.map_data.extend(line)
        self.run_finder()

    def get_file_data(self):
        settings_dir = self.get_data('settings path', str)
        if self.check_dir(settings_dir):
            self.settings_dir = settings_dir
        print(f'{Fore.BLUE}Used settings {self.settings_dir}{Style.RESET_ALL}')
        with open(self.settings_dir, 'r') as treasure_map:
            for line in treasure_map:
                self.map_height += 1
                if self.map_height == 1:
                    self.map_weight = len(line.split(' '))
                self.map_data.extend([x.strip() for x in line.split(' ')])
        self.run_finder()

    def check_dir(self, dir):
        return os.path.isfile(f'./{dir}')

    def run_finder(self):
        method = self.get_data('needed method ("OOP" or "FP")', lambda x: None if x not in ('OOP', 'FP') else x)
        if method == 'OOP':
            print(f'{Fore.BLUE}Treasure road {self.use_OOP()}{Style.RESET_ALL}')
        elif method == 'FP':
            print(f'{Fore.BLUE}Treasure road {self.use_FP()}{Style.RESET_ALL}')

    def use_OOP(self):
        treasure_map = Treasure_map(self.map_weight, self.map_height, self.map_data)
        return Treasure_road(treasure_map).print_map

    def use_FP(self):
        return find_treasure(self.map_weight, self.map_height, self.map_data)

    def get_data(self, data_name, func):
        data = None
        while not data:
            print(f'{Fore.GREEN}Enter {data_name}:{Style.RESET_ALL}')
            try:
                data = func(input())
                if data:
                    return data
                print(f'{Fore.RED}Incorrect parameters! Try once more.{Style.RESET_ALL}')
            except:
                print(f'{Fore.RED}Incorrect parameters! Try once more.{Style.RESET_ALL}')


if __name__ == "__main__":
    app = Main(sys.argv[1:])
    app.start()
