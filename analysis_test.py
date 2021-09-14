from analysis import Analysis
import unittest
import pandas 

PATH = "./tests_data/example.txt"

class AnalysisTest(unittest.TestCase):
    def setUp(self):
        self.analysis = Analysis(PATH)

    def test_lines(self):
        value = self.analysis.lines
        expect_value = ['{ "foo": "bar" }', '{ "foobar": 1 }']
        self.assertEqual(value, expect_value)
    
    def test_data(self):
        value = self.analysis.data
        expect_value = []
        self.assertEqual(value, expect_value)

    def test_append_data(self):
        value = self.analysis.data
        expect_value = [{'foo': 'bar'}, {'foobar': 1}]
        self.analysis.append_parsed_data()
        self.assertEqual(value, expect_value)

    def test_data_frame(self):
        value = self.analysis.data_frame()
        expect_data_frame = pandas.DataFrame(columns=['authenticated_entity', 'latencies', 'route'])
        pandas.testing.assert_frame_equal(value, expect_data_frame)

if __name__ == '__main__':
    unittest.main(
        failfast=False,
        buffer=False,
        catchbreak=False)