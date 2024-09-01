import unittest
from tests.test_convert_date import ConvertDateTests
from tests.test_convert_f_to_c import ConvertTempTests
from tests.test_calculate_mean import CalculateMeanTests
from tests.test_load_data_from_csv import LoadCSVTests
from tests.test_find_min import FindMinTests
from tests.test_find_max import FindMaxTests
from tests.test_generate_summary import GenerateSummaryTests
from tests.test_generate_daily_summary import GenerateDailySummaryTests


def run_tests():
    """Run all unit tests."""
runner = unittest.TextTestRunner()
print("Running Tests...\n")

test_suites = [
        unittest.TestLoader().loadTestsFromTestCase(ConvertDateTests),
        unittest.TestLoader().loadTestsFromTestCase(ConvertTempTests),
        unittest.TestLoader().loadTestsFromTestCase(CalculateMeanTests),
        unittest.TestLoader().loadTestsFromTestCase(LoadCSVTests),
        unittest.TestLoader().loadTestsFromTestCase(FindMinTests),
        unittest.TestLoader().loadTestsFromTestCase(FindMaxTests),
        unittest.TestLoader().loadTestsFromTestCase(GenerateSummaryTests),
        unittest.TestLoader().loadTestsFromTestCase(GenerateDailySummaryTests),
    ]
    
for suite in test_suites:
        runner.run(suite)

if __name__ == '__main__':
    run_tests()


runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(ConvertDateTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(ConvertTempTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(CalculateMeanTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(LoadCSVTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(FindMinTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(FindMaxTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(GenerateSummaryTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(GenerateDailySummaryTests))))
