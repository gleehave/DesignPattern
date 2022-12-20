from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class OneCommand(Command):
    def __init__(self, payload: str):
        self._payload = payload

    def execute(self):
        print(f"OneCommand: See, I can do simple things like printing")
        print(f"{self._payload}")

class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str):
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Receiver:
    def do_something(self, a:str):
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b:str):
        print(f"\nReceiver: Also working on ({b}.)", end="")

class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self):
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_finish.execute()

if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """

    invoker = Invoker()
    invoker.set_on_start(OneCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()

