class BasePlayer:
    """Base player."""

    def ping(self):
        return "ping"

    def pong(self):
        return "pong"


class PongPlayer(BasePlayer):
    """Pong player."""

    def pong(self):
        return "PONG"


class NeutralPlayer(BasePlayer):
    """Neutral player."""


class ConfusedPlayer(PongPlayer, NeutralPlayer):
    """Confused player.

    This is what we call the diamond problem, where `BasePlayer` child classes
    are the same as `ConfusedPlayer` parent classes. Python has the MRO to
    determine which `ping` and `pong` methods are called via the `super()`
    call followed by the respective method.

    The `super()` call is usually used without any parameters, which
    means that we start the MRO process from the current class upwards.

    For more on the subject, please consult this link:

    https://www.python.org/download/releases/2.3/mro/
    """

    def ping(self):
        """Override `ping` method."""
        return "pINg"

    def ping_pong(self):
        """Run `ping` and `pong` in different ways."""
        return [
            self.ping(),
            super().ping(),
            self.pong(),
            super().pong()
        ]


class IndecisivePlayer(NeutralPlayer, PongPlayer):
    """Indecisive player.

    Notice that this class was created successfully without any conflicts
    even though the MRO of `ConfusedPlayer` is different.

    Notice that one of the `super()` calls uses additional parameters to
    start the MRO process from another class. This is used for demonstrative
    purposes and is highly discouraged as this bypasses the default method
    resolution process.
    """

    def pong(self):
        """Override `pong` method."""
        return "pONg"

    def ping_pong(self):
        """Run `ping` and `pong` in different ways."""
        return [
            self.ping(),
            super().ping(),
            self.pong(),
            super(PongPlayer, self).pong()  # bypass MRO to `BasePlayer`
        ]


def main():
    # `ConfusedPlayer` methods are resolved from child to parent like this
    assert ConfusedPlayer.mro() == [
        ConfusedPlayer, PongPlayer, NeutralPlayer, BasePlayer, object]

    # `IndecisivePlayer` methods are resolved from child to parent like this
    assert IndecisivePlayer.mro() == [
        IndecisivePlayer, NeutralPlayer, PongPlayer, BasePlayer, object]

    # Show `ConfusedPlayer` method resolution in action
    assert ConfusedPlayer().ping_pong() == ["pINg", "ping", "PONG", "PONG"]

    # Show `IndecisivePlayer` method resolution in action
    assert IndecisivePlayer().ping_pong() == ["ping", "ping", "pONg", "pong"]

    class_creation_failed = False
    try:
        # Creating a new class `ConfusedPlayer` and `IndecisivePlayer`
        # results in a `TypeError` because both classes have mismatched
        # MRO outputs. This means that they cannot be reconciled as
        # one class. Hence `MissingPlayer` will not be created
        type("MissingPlayer", (ConfusedPlayer, IndecisivePlayer), {})
    except TypeError:
        class_creation_failed = True
    assert class_creation_failed is True


if __name__ == "__main__":
    main()
