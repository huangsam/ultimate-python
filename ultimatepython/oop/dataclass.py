"""
Data classes (PEP 557), introduced in Python 3.7, provide a declarative syntax
for classes that primarily store state.

Before dataclasses, developers wrote repetitive boilerplate for `__init__`,
`__repr__`, and `__eq__` methods. The `@dataclass` decorator inspects type
annotations on class attributes to automatically generate these standard methods.

Advanced capabilities include:
- `field(default_factory=...)` to avoid mutable default argument pitfalls
- `frozen=True` for immutable instances that can be hashed and stored in sets
- `kw_only=True` to enforce keyword-only arguments during initialization
- `__post_init__` for validation and derived attribute computation
"""

from dataclasses import FrozenInstanceError, asdict, dataclass, field


@dataclass
class Point:
    """Simple 2D coordinate with auto-generated constructor and equality."""

    x: float
    y: float


@dataclass
class UserProfile:
    """User profile demonstrating default values and default factories."""

    username: str
    email: str
    tags: list[str] = field(default_factory=list)
    active: bool = True


@dataclass(frozen=True)
class ServerConfig:
    """Immutable server configuration that is safely hashable."""

    host: str
    port: int


@dataclass(kw_only=True)
class InventoryItem:
    """Item demonstrating keyword-only parameters and post-initialization."""

    name: str
    unit_price: float
    quantity: int = 1
    total_cost: float = field(init=False)

    def __post_init__(self) -> None:
        if self.unit_price < 0 or self.quantity < 0:
            raise ValueError("Price and quantity must be non-negative")
        self.total_cost = round(self.unit_price * self.quantity, 2)


def main() -> None:
    # 1. Automatic __init__, __repr__, and __eq__
    p1 = Point(10.0, 20.0)
    p2 = Point(10.0, 20.0)
    p3 = Point(5.0, 15.0)

    assert p1 == p2
    assert p1 != p3
    assert repr(p1) == "Point(x=10.0, y=20.0)"

    # 2. Default factories prevent shared mutable state across instances
    user_a = UserProfile("alice", "alice@example.com")
    user_b = UserProfile("bob", "bob@example.com")
    user_a.tags.append("admin")

    assert user_a.tags == ["admin"]
    assert user_b.tags == []
    assert user_a.tags is not user_b.tags

    # Convert dataclass instance directly to a dictionary
    assert asdict(user_a) == {
        "username": "alice",
        "email": "alice@example.com",
        "tags": ["admin"],
        "active": True,
    }

    # 3. Frozen dataclasses guarantee immutability and allow hashing
    config = ServerConfig("127.0.0.1", 8080)
    mutation_failed = False
    try:
        config.port = 9090  # type: ignore[misc]
    except FrozenInstanceError:
        mutation_failed = True
    assert mutation_failed is True

    # Because config is immutable, it can be used in sets and as dictionary keys
    config_set = {config, ServerConfig("127.0.0.1", 8080)}
    assert len(config_set) == 1

    # 4. Keyword-only instantiation and __post_init__ computation
    item = InventoryItem(name="Mechanical Keyboard", unit_price=99.99, quantity=2)
    assert item.total_cost == 199.98

    # Keyword-only enforcement ensures clear call sites
    positional_failed = False
    try:
        InventoryItem("Monitor", 299.99)  # type: ignore[misc]
    except TypeError:
        positional_failed = True
    assert positional_failed is True

    # Post-init validation prevents invalid state
    invalid_item_failed = False
    try:
        InventoryItem(name="Faulty Item", unit_price=-10.0)
    except ValueError as e:
        invalid_item_failed = True
        assert str(e) == "Price and quantity must be non-negative"
    assert invalid_item_failed is True


if __name__ == "__main__":
    main()
