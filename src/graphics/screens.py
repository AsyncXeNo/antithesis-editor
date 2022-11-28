from __future__ import annotations

from typing import TYPE_CHECKING
from abc import abstractmethod, ABC

from loguru import logger

if TYPE_CHECKING:
    import pygame
    from level_editor import Editor

from graphics.constants import RESOLUTION


class Screen(ABC):
    
    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        pass
    
    @abstractmethod
    def render(self, editor: Editor) -> None:
        pass
