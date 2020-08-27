import weakref
from datetime import datetime
from uuid import uuid4

# Module-level constants
_PROVIDER = "aws"
_APPS = ["yelp", "pinterest", "uber", "twitter"]
_COMPONENTS = ("db", "web", "cache")


def log(message, log_level="info"):
    """Log a message similar to that of web servers."""
    print(f"{datetime.now()} [{log_level}] - {message}")


class Server:
    """General server."""

    @classmethod
    def create(cls, role, provider=_PROVIDER):
        return cls(uuid4().hex, provider, role)

    def __init__(self, ssid, provider, role):
        self.ssid = ssid
        self.provider = provider
        self.role = role

    def __repr__(self):
        return f"<Server role={self.role}>"

    def __del__(self):
        log(f"{self} has shut down", log_level="warning")


class ServerRegistry:
    """Server registry with weak references."""

    def __init__(self):
        self._servers = weakref.WeakSet()

    @property
    def servers(self):
        return {s for s in self._servers}

    @property
    def server_count(self):
        return len(self.servers)

    def add(self, server):
        log(f"Add {server} to registry")
        self._servers.add(server)


def setup_and_teardown_servers(registry):
    """Explicitly setup and implicitly teardown servers."""
    app_servers = {}

    # Create all of the servers and put them in the registry and the
    # dictionary and we'll tally things at the end
    for app in _APPS:
        app_servers[app] = set()
        for component in _COMPONENTS:
            server = Server.create(f"{app}_{component}")
            registry.add(server)
            app_servers[app].add(server)

    # All of these counts are equivalent and this is no surprise since
    # our for loop unconditionally creates a server for every permutation
    # of apps and components, and adds each server to the registry and
    # dictionary unconditionally
    assert (
        registry.server_count
        == len(_APPS) * len(_COMPONENTS)
        == len([(app, server)
                for app, servers in app_servers.items()
                for server in servers])
    )

    # What's really interesting is that all of this memory goes away after
    # a while. Notice how the __del__ calls start happening once we leave
    # the scope of this function


def main():
    # Initialize a server registry
    registry = ServerRegistry()

    # Setup and teardown servers with the registry
    setup_and_teardown_servers(registry)

    # Notice that our registry has no recollection of the servers. The
    # benefit is that our registry is allowing the garbage collector to do
    # its job effectively and remove orphaned servers from the previous
    # call, keeping our software memory-efficient
    assert registry.servers == set()
    assert registry.server_count == 0


if __name__ == '__main__':
    main()
