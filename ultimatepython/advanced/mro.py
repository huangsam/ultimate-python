class A:
    """Base class."""

    def ping(self):
        print("ping", self)


class B(A):
    """B inherits from A."""

    def pong(self):
        print("pong", self)


class C(A):
    """C inherits from A."""

    def pong(self):
        print("PONG", self)


class D(B, C):
    """D inherits from B and C.

    This is what we call the diamond problem, where A has multiple child
    classes that are the same as D's parent classes. Python has the MRO to
    determine which method is applied when calling `super()`.
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

    This exhibits the Python MRO as well. Notice that this was class was
    created successfully without any conflicts to D.
    """

    def pong(self):
        print("pong", self)

    def ping_pong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()


def main():
    assert D.mro() == [D, B, C, A, object]
    assert E.mro() == [E, C, B, A, object]

    d_obj = D()
    d_obj.ping_pong()

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
