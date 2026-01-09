# (ex. 8_6)

from typing import Any

class Lijst:
    def __init__(self) -> None:
        self.items = []

    def __str__(self) -> str:
        return f"{self.items}"

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, index: int) -> Any:
        return self.items[index]

    def __setitem__(self, index: int, value: Any):
        self.items[index] = value

    def __contains__(self, item: Any) -> bool:
        return item in self.items

    def append(self, item: Any) -> None:
        self.items.append(item)

    def __add__(self, other_list: Lijst):
        if isinstance(other_list, Lijst):
            nieuwe_lijst = Lijst()
            nieuwe_lijst.items = self.items + other_list.items
            return nieuwe_lijst
        return NotImplemented


# for following as input:

# mijn_lijst = Lijst()
# mijn_lijst.append("a")
# mijn_lijst.append("b")
# mijn_lijst.append("c")
# print(mijn_lijst)
# print(len(mijn_lijst))
# mijn_lijst[2] = 30
# print(mijn_lijst[2])
# print(30 in mijn_lijst)
# andere_lijst = Lijst()
# andere_lijst.items.append('d')
# andere_lijst.items.append('e')
# andere_lijst.items.append('f')
# print(mijn_lijst + andere_lijst)

# expected output:

# ['a', 'b', 'c']
# 3
# 30
# True
# ['a', 'b', 30, 'd', 'e', 'f']