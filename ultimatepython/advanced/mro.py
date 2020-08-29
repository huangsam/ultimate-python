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

    This is what we call the diamond problem, where A has multiple child
    classes that are the same as D's parent classes. Python has the MRO to
    determine which `pong` method is applied when calling `super()`.

    For more on the subject, please consult this link:

    https://www.python.org/download/releases/2.3/mro/
    """

    def ping(self):
        print("pINg", self)

    def ping_pong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()


class IndecisivePlayer(NeutralPlayer, PongPlayer):
    """Indecisive player.

    This exhibits the Python MRO as well. Notice that this class was
    created successfully without any conflicts because of `ConfusedPlayer`.
    All is good in the world.
    """

    def pong(self):
        print("pONg", self)

    def ping_pong(self):
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
