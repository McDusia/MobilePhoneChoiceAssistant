from collections import UserDict
from typing import Callable
from typing import Generic
from typing import TypeVar

KT = TypeVar("KT")
VT = TypeVar("VT")


class defaultdict(UserDict, Generic[KT, VT]):

    def __init__(self, initializer: Callable[[KT], VT]):
        super().__init__()
        self._initializer = initializer

    def __getitem__(self, item: KT) -> VT:
        if item not in self.data:
            self.data[item] = self._initializer(item)
        return self.data[item]
