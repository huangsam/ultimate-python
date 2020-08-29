class BasePlayer:
    """Base player."""

    def ping(self):
        print("ping", self)

    def pong(self):
        print("pong", self)


class PongPlayer(BasePlayer):
    """Pong player."""

    def pong(self):
        print("PONG", self)


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
        print("pINg", self)

    def ping_pong(self):
        """Run `ping` and `pong` in different ways."""
        self.ping()
        super().ping()
        self.pong()
        super().pong()


class IndecisivePlayer(NeutralPlayer, PongPlayer):
    """Indecisive player.

    Notice that this class was created successfully without any conflicts
    despite the fact that the MRO of `ConfusedPlayer` is different.

    Notice that one of the `super()` calls uses additional parameters to
    start the MRO process from another class. This is used for demonstrative
    purposes and is highly discouraged as this bypasses the default
    resolution process.
    """

    def pong(self):
        """Override `pong` method."""
        print("pONg", self)

    def ping_pong(self):
        """Run `ping` and `pong` in different ways."""
        self.ping()
        super().ping()
        self.pong()
        super(PongPlayer, self).pong()  # bypass MRO to `BasePlayer`


def main():
    # Methods in `ConfusedPlayer` are resolved from child to parent
    assert ConfusedPlayer.mro() == [
        ConfusedPlayer, PongPlayer, NeutralPlayer, BasePlayer, object]

    # Methods in `IndecisivePlayer` are resolved from child to parent as well
    assert IndecisivePlayer.mro() == [
        IndecisivePlayer, NeutralPlayer, PongPlayer, BasePlayer, object]

    # Show `ConfusedPlayer` method resolution in action
    ConfusedPlayer().ping_pong()

    # Show `IndecisivePlayer` method resolution in action
    IndecisivePlayer().ping_pong()

    try:
        # Creating a new class `ConfusedPlayer` and `IndecisivePlayer`
        # result in a `TypeError` because both classes have mismatched
        # MRO outputs. This means that they cannot be reconciled as
        # one class. Hence `MissingPlayer` will not be created
        type("MissingPlayer", (ConfusedPlayer, IndecisivePlayer), {})
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
