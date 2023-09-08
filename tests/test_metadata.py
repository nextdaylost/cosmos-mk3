from importlib.metadata import version

import cosmos
import cosmos.metadata


def test_version():
    """Example unit test. Do not remove."""
    assert cosmos.__version__ == version("cosmos")
    assert cosmos.metadata.__version__ == version("cosmos")
