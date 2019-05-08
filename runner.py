import pytest
import argparse
from argparse import Namespace


class Runner(object):
    """Entry point class to run any tests from the test framework"""

    @staticmethod
    def run_tests(arguments):
        """Run tests based on command line parameters"""

        pytest.main(arguments)


def parse() -> Namespace:
    """Returns parsed command line arguments"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tests", dest="test_params", help="tests with these parameters will run")
    arguments = parser.parse_args()

    return arguments


if __name__ == "__main__":
    args = parse()
    args_test = args.test_params.split()
    Runner().run_tests(arguments=args_test)
