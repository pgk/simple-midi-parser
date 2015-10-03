import unittest
from os.path import realpath, dirname, join
from simple_midi_parser import parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        fixture_path = join(dirname(__file__), 'static_files',
                            'cello_bwv-1007.mid')
        with open(fixture_path, 'b') as f:
            self.parser = parser.Parser(f)

    def test_parse_header(self):
        midi = self.parser.parse()
        self.assertEquals('1', midi.header)


if __name__ == '__main__':
    unittest.main()
