class A:
    """Base class."""

    def ping(self):
        print("ping", self)

    def pong(self):
        print("pong", self)


class B(A):
    """B inherits from A."""

    def pong(self):
        print("PONG", self)


class C(A):
    """C inherits from A."""


class D(B, C):
    """D inherits from B and C.

    This is what we call the diamond problem, where A has multiple child
    classes that are the same as D's parent classes. Python has the MRO to
    determine which `pong` method is applied when calling `super()`.

    For more on the subject, please consult this link:

    https://www.python.org/download/releases/2.3/mro/
    """

    def ping(self):
        print("PING", self)

    def ping_pong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()


class E(C, B):
    """E inherits from C and B.

    This exhibits the Python MRO as well. Notice that this class was
    created successfully without any conflicts because of D's existence.
    All is good in the world.
    """

    def pong(self):
        print("pong", self)

    def ping_pong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()


def main():
    # Show how methods in class D are resolved from child to parent
    assert D.mro() == [D, B, C, A, object]

    # Show how methods in class E are resolved from child to parent
    assert E.mro() == [E, C, B, A, object]

    # Show D method resolution in action
    d_obj = D()
    d_obj.ping_pong()

    # Show E method resolution in action
    e_obj = E()
    e_obj.ping_pong()

    try:
        # Creating a new class F from D and E result in a type error
        # because D and E have MRO outputs that cannot be merged
        # together as one
        type("F", (D, E), {})
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
