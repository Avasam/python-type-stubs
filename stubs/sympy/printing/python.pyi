from sympy.printing.repr import ReprPrinter
from sympy.printing.str import StrPrinter

STRPRINT = ...
class PythonPrinter(ReprPrinter, StrPrinter):
    def __init__(self, settings=...) -> None:
        ...
    


def python(expr, **settings) -> str:
    ...

def print_python(expr, **settings) -> None:
    ...
