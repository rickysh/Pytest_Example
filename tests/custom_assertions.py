import pytest


def is_positive(number):
  """Custom assertion to check if a number is positive."""
  return number > 0

# pytest.py (optional, for automatic registration)
def pytest_configure(config):
  config.add_assertion(is_positive)
