from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic, Iterator

if TYPE_CHECKING:
    pass

from loguru import logger

from graphics.screens import Screen
from graphics.layers import Layer

T = TypeVar('T', Screen, Layer)


class Stack(Generic[T]):
    
    def __init__(self) -> None:
        self.internal_list: list[tuple[str,T]] = []

    def __iter__(self) -> Iterator:
        return self.internal_list.__iter__()
    
    def get_top(self) -> T:
        return self.internal_list[-1][1]
    
    def get_bottom(self) -> T:
        return self.internal_list[0][1]

    def swap(self, index1: str, index2: str) -> None:
        t1 = (index1, self[index1])
        t2 = (index2, self[index2])

        iindex1 = self.delete(index1)
        iindex2 = self.delete(index2)

        if iindex1 > iindex2:
            iindex1, iindex2 = iindex2, iindex1
            t1, t2 = t2, t1

        self.insert(iindex1, t2)
        self.insert(iindex2, t1)

    def to_top(self, index: str) -> None:
        t = self[index]
        self.delete(index)
        self.push(t, index)

    def push(self, obj: T, name: str) -> None:
        names = [t[0] for t in self.internal_list]
        if name in names:
            logger.error(f'Item with name {name} already exists. Cannot push to stack.')
            raise ValueError(f'Item with name {name} already exists. Cannot push to stack.')
            
        self.internal_list.append((name,obj))
    
    def pop(self) -> T:
        return self.internal_list.pop()

    def delete(self, key: str) -> int:
        for index, x in enumerate(self.internal_list):
            if x[0] == key:
                del self.internal_list[index]
                return index
        else:
            logger.error(f'Key {key} not found')           
            raise ValueError(f'Key {key} not found')
    
    def __getitem__(self, index: int | slice | str) -> T:
        check = lambda x: isinstance(index, x)
        if check(int):
            return self.internal_list[index][1]
        elif check(slice):
            return [x[1] for x in self.internal_list[index]]
        elif check(str):
            return [x for x in self.internal_list if x[0] == index][0][1]
        else:
            logger.error('Indexing not using integer, slice or string')
            raise TypeError('Index must be an integer, slice or string')
