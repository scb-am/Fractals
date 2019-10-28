import unittest
from collections import Counter


class TestStringMethods(unittest.TestCase):
    def test_dif_cases(self):
        self.assertEqual(most_frequent_characters('ccacccdaababBBBccccdd', 3),
                         'cba')

    def test_characters_count(self):
        self.assertEqual(most_frequent_characters('ccacccdaababBBBccccdd', 4),
                         'cbad')

    def test_whitespaces(self):
        self.assertEqual(most_frequent_characters(' cc  accc  daab   ab   '
                                                  'bbb   ccc  cdd  ', 3),
                         'cba')

    def test_alphabetical_order(self):
        self.assertEqual(most_frequent_characters('ccacccdaababbbccccdd', 3),
                         'cab')

    def test_with_symbols(self):
        self.assertEqual(most_frequent_characters('77c4744c34433a77c3ccd4aa3'
                                                  'b737ab77333bb4ccc3cd77444d',
                                                  3), '734')
        self.assertEqual(most_frequent_characters('!@#^$%^&*()_-+={}[]', 3),
                         '^!#')

    def test_corner_cases(self):
        self.assertEqual(most_frequent_characters('ccacccdaababBBBccccdd', 10),
                         'cbad')
        self.assertEqual(most_frequent_characters('ccacccdaababBBBccccdd', -1),
                         None)
        self.assertEqual(most_frequent_characters('', 3), None)


def most_frequent_characters(string, num_of_characters):
    if not string or num_of_characters < 0:
        return None
    frequent_of_characters = Counter(string.replace(" ", "").lower())
    sorted_frequent = sorted(frequent_of_characters.items(),
                             key=lambda item: (-item[1], item[0]))
    list_of_characters = [x[0] for x in sorted_frequent[:num_of_characters]]
    result_string = ''.join(list_of_characters)
    return result_string


unittest.main()
