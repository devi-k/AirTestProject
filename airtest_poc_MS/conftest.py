"""Base conftest.py."""
import pytest

@pytest.fixture(scope="session")
def proj_setup_fix():
    """
    Fixture for Setup

    The scope of the fixture is for the entire session of a test run.
    """
    print("Running Setup Fixture")
    yield
    print("Running Teardown Fixture")
    





