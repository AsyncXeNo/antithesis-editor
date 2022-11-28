from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from utils import generate_id


class Surface(pygame.surface.Surface):
    """Adds ID and pos attributes to the pygame Surface class"""

    def __init__(self, size: tuple[int, int], pos: list[int]) -> None:
        
        super().__init__(size, pygame.SRCALPHA)


        self.ID: str = f'SURFACE-{generate_id()}'
        self.pos: list[int] = pos

    def copy(self) -> Surface:
        """Returns a copy of the surface"""
        
        new = Surface(self.get_size(), self.pos)
        new.ID = self.ID
        new.blit(self, (0, 0))

        return new