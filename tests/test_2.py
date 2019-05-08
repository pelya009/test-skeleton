from tests.test_base import TestBase


class TestTwo(TestBase):

    def test_check_sum_of_smth_else(self):
        assert self.two * 2 == 4
