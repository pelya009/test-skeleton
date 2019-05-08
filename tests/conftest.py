import pytest


def get_one():
    return one


def get_two():
    return two


def get_three():
    return three


@pytest.fixture(scope="session", autouse=True)
def prepare_global_data():

    global one
    one = 1

    global two
    two = 2


@pytest.fixture(scope="class", autouse=True)
def prep_class_data():

    global three
    three = 3
