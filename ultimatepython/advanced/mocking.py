from collections import Counter
from unittest.mock import MagicMock, PropertyMock, patch

# Module-level constants
_COUNTER = Counter(pid=1)
_PROTOCOL_HTTP = "http"
_PROTOCOL_HTTPS = "https"
_FAKE_BASE_URL = f"{_PROTOCOL_HTTPS}://www.google.com:443"
_FAKE_PID = 127


class AppServer:
    """Application server.

    Normally this isn't mocked because it is the runtime environment for
    business logic, database endpoints, network sockets and more. But
    this server definition is rather lightweight, so it's acceptable
    in this case.
    """

    def __init__(self, host, port, proto):
        self._host = host
        self._port = port
        self._proto = proto
        self._pid = -1

    @property
    def base_url(self):
        return f"{self._proto}://{self._host}:{self._port}"

    @property
    def started(self):
        return self._get_pid() > 0

    def _get_pid(self):
        return self._pid

    def start_server(self):
        self._pid = _COUNTER["pid"]
        _COUNTER["pid"] += 1
        return f"Started server: {self.base_url}"


class FakeServer(AppServer):
    """Subclass parent and fake some routines."""

    @property
    def base_url(self):
        """Mock output of public URL."""
        return _FAKE_BASE_URL

    def _get_pid(self):
        """Mock output of private PID."""
        return _FAKE_PID


def main():
    # This is the original class and it works as expected
    app_server = AppServer("localhost", 8000, _PROTOCOL_HTTP)
    assert app_server.base_url == "http://localhost:8000"
    assert app_server.start_server() == "Started server: http://localhost:8000"
    assert app_server.started is True

    # But sometimes you cannot test the finer details of a class because
    # its methods depend on the availability of external resources. This
    # is where mocking comes to the rescue. There are a couple approaches
    # that developers use when it comes to mocking

    # Approach 1: Use a `MagicMock` in place of a real class instance
    mock_server = MagicMock()
    assert isinstance(mock_server, MagicMock)
    assert isinstance(mock_server.start_server(), MagicMock)
    mock_server.start_server.assert_called()
    mock_server.base_url.assert_not_called()

    # Approach 2: Patch a method in the original class
    with patch.object(AppServer, "base_url", PropertyMock(return_value=_FAKE_BASE_URL)):
        patch_server = AppServer("localhost", 8080, _PROTOCOL_HTTP)
        assert isinstance(patch_server, AppServer)
        assert patch_server.base_url == _FAKE_BASE_URL
        assert patch_server.started is False

    # Approach 3: Create a new class that inherits the original class
    fake_server = FakeServer("localhost", 8080, _PROTOCOL_HTTP)
    assert isinstance(fake_server, AppServer)
    assert fake_server.base_url == _FAKE_BASE_URL
    assert fake_server.started is True


if __name__ == "__main__":
    main()
