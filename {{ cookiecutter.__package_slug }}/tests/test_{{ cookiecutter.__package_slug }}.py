"""For testing the {{ cookiecutter.__package_slug }} module."""

from src.{{ cookiecutter.__package_slug }}.{{ cookiecutter.__package_slug }} import hello_world


def test_test():
    """Test test"""
    assert 1 == 1


def test_hello_world():
    """Test hello_world"""
    assert hello_world("Hello world", False) == "Hello world"
