from types import NotImplementedType
from typing import Any, LiteralString, Self

from sympy.polys.domains.domainelement import DomainElement
from sympy.polys.polyutils import PicklableWithSlots
from sympy.utilities import public

@public
class ModularInteger(PicklableWithSlots, DomainElement):
    __slots__ = ...
    def parent(self) -> None: ...
    def __init__(self, val) -> None: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> LiteralString: ...
    def __str__(self) -> str: ...
    def __int__(self) -> int: ...
    def to_int(self): ...
    def __pos__(self) -> Self: ...
    def __neg__(self) -> Self: ...
    def __add__(self, other) -> Self | NotImplementedType: ...
    def __radd__(self, other) -> Self | NotImplementedType: ...
    def __sub__(self, other) -> Self | NotImplementedType: ...
    def __rsub__(self, other) -> Self | NotImplementedType: ...
    def __mul__(self, other) -> Self | NotImplementedType: ...
    def __rmul__(self, other) -> Self | NotImplementedType: ...
    def __truediv__(self, other) -> Self | NotImplementedType: ...
    def __rtruediv__(self, other) -> Self | NotImplementedType: ...
    def __mod__(self, other) -> Self | NotImplementedType: ...
    def __rmod__(self, other) -> Self | NotImplementedType: ...
    def __pow__(self, exp) -> Self: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __bool__(self) -> bool: ...
    def invert(self) -> Self: ...

_modular_integer_cache: dict[tuple[Any, Any, Any], type[ModularInteger]] = ...

def ModularIntegerFactory(_mod, _dom, _sym, parent) -> type[Any]: ...
