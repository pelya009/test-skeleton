from tests.test_base import TestBase
from tests.conftest import get_two, get_three


class TestOne(TestBase):

    def test_check_sum_of_smth(self):
        assert self.one + get_two() == 3

    def test_check_addtional_sum_of_smth(self):
        assert self.one + get_two() + get_three() == 6
