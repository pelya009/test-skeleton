from tests.conftest import get_one, get_two


class TestBase:

    def setup_class(self):
        self.one = get_one()
        self.two = get_two()
